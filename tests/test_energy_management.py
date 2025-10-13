import pytest
from datetime import datetime
from src.energy.EnergyManagementSystem import SmartEnergyManagementSystem


class TestEnergyManagementSystem:
    def setup_method(self):
        self.system = SmartEnergyManagementSystem()
        self.base_time = datetime(2024, 1, 1, 12, 0, 0)

    def test_tc1_energy_saving_mode_activated_with_low_priority_devices(self):
        """
        TC1: Mode economia ativado com dispositivos de baixa prioridade.
        Cobertura: Aresta nó 3 → nó 4 (current_price > price_threshold)
        Par def-uso: energy_saving_mode definido (linha 26), usado no retorno
        """
        result = self.system.manage_energy(
            current_price=150.0,
            price_threshold=100.0,
            device_priorities={"Light": 2, "Heating": 1},
            current_time=self.base_time,
            current_temperature=20.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[]
        )
        assert result.energy_saving_mode is True
        assert result.device_status["Light"] is False
        assert result.device_status["Heating"] is True

    def test_tc2_no_energy_saving_mode(self):
        """
        TC2: Sem modo economia.
        Cobertura: Aresta nó 3 → nó 6 (current_price <= price_threshold)
        Par def-uso: device_status[device] definido (linha 35),
        usado posteriormente
        """
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Light": 1, "TV": 2},
            current_time=self.base_time,
            current_temperature=20.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[]
        )
        assert result.energy_saving_mode is False
        assert result.device_status["Light"] is True
        assert result.device_status["TV"] is True

    def test_tc3_night_mode_active(self):
        """
        TC3: Modo noturno ativo (23h).
        Cobertura: Aresta nó 5 → nó 15 (current_time.hour >= 23)
        Par def-uso: device_status modificado para dispositivos não essenciais
        """
        night_time = datetime(2024, 1, 1, 23, 30, 0)
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Light": 1,
                               "TV": 2,
                               "Security": 1,
                               "Refrigerator": 1},
            current_time=night_time,
            current_temperature=20.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[]
        )
        assert result.device_status["Light"] is False
        assert result.device_status["TV"] is False
        assert result.device_status["Security"] is True
        assert result.device_status["Refrigerator"] is True

    def test_tc4_night_mode_early_morning(self):
        """
        TC4: Modo noturno na madrugada (< 6h).
        Cobertura: Aresta nó 5 → nó 15 (current_time.hour < 6)
        """
        early_morning = datetime(2024, 1, 1, 3, 0, 0)
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Light": 1, "Security": 1, "Refrigerator": 1},
            current_time=early_morning,
            current_temperature=20.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[]
        )

        assert result.device_status["Light"] is False
        assert result.device_status["Security"] is True
        assert result.device_status["Refrigerator"] is True

    def test_tc5_low_temperature_heating_activated(self):
        """
        TC5: Temperatura baixa - aquecimento ativado.
        Cobertura: Aresta nó 16 → nó 21 (current_temperature < desired_temperature_range[0])
        Par def-uso: temperature_regulation_active definido (linha 46), usado no retorno
        """
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Heating": 1, "Cooling": 1},
            current_time=self.base_time,
            current_temperature=15.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[]
        )
        assert result.device_status["Heating"] is True
        assert result.temperature_regulation_active is True

    def test_tc6_high_temperature_cooling_activated(self):
        """
        TC6: Temperatura alta - resfriamento ativado.
        Cobertura: Aresta nó 16 → nó 23 → nó 24 (current_temperature > desired_temperature_range[1])
        Par def-uso: device_status["Cooling"] definido (linha 48)
        """
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Heating": 1, "Cooling": 1},
            current_time=self.base_time,
            current_temperature=28.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[]
        )
        assert result.device_status["Cooling"] is True
        assert result.temperature_regulation_active is True

    def test_tc7_ideal_temperature_climate_control_off(self):
        """
        TC7: Temperatura ideal - climatização desligada.
        Cobertura: Aresta nó 23 → nó 26 (temperatura na faixa desejada)
        Par def-uso: device_status["Heating"] e ["Cooling"] definidos como False
        """
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Heating": 1, "Cooling": 1},
            current_time=self.base_time,
            current_temperature=21.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[]
        )
        assert result.device_status["Heating"] is False
        assert result.device_status["Cooling"] is False
        assert result.temperature_regulation_active is False

    def test_tc8_energy_limit_loop_devices_turned_off(self):
        """
        TC8: Loop de limite de energia - dispositivos desligados.
        Cobertura: Aresta nó 27 → nó 28 → nó 31 → nó 32 → nó 35
        Par def-uso: total_energy_used_today modificado (linha 70) e usado (linha 67)
        """
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Light": 2, "TV": 3, "Security": 1},
            current_time=self.base_time,
            current_temperature=20.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=120.0,
            scheduled_devices=[]
        )
        assert result.total_energy_used < 120.0

    def test_tc9_energy_limit_loop_exit_by_limit(self):
        """
        TC9: Loop de limite de energia - saída por atingir limite.
        Cobertura: Aresta nó 32 → nó 27 (break do loop quando atinge limite)
        Par def-uso: total_energy_used_today verificado durante loop
        """
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Light": 2, "TV": 3},
            current_time=self.base_time,
            current_temperature=20.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=101.0,  # Apenas 1 acima do limite
            scheduled_devices=[]
        )
        assert result.total_energy_used <= 100.0
