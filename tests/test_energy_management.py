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
