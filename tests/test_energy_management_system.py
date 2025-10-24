import pytest
from datetime import datetime
from src.energy.EnergyManagementSystem import SmartEnergyManagementSystem
from src.energy.DeviceSchedule import DeviceSchedule


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
            device_priorities={"Light": 2, "Heating": 1, "TV": 3},
            current_time=self.base_time,
            current_temperature=15.0,  # Temperatura baixa para ativar aquecimento
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[]
        )
        assert result.energy_saving_mode is True
        assert result.device_status["Light"] is False
        assert result.device_status["TV"] is False
        assert result.device_status["Heating"] is True  # Mantido ligado por prioridade 1 e necessário para aquecimento

    def test_tc2_no_energy_saving_mode_with_current_equals_threshold_price(self):
        """
        TC2: Mode economia ativado com dispositivos de baixa prioridade.
        Cobertura: Aresta nó 3 → nó 4 (current_price == price_threshold)
        Par def-uso: energy_saving_mode definido (linha 26), usado no retorno
        """
        result = self.system.manage_energy(
            current_price=100.0,
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

    def test_tc3_no_energy_saving_mode(self):
        """
        TC3: Sem modo economia.
        Cobertura: Aresta nó 3 → nó 6 (current_price < price_threshold)
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

    def test_tc4_night_mode_active(self):
        """
        TC4: Modo noturno ativo (23h).
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

    def test_tc5_night_mode_early_morning(self):
        """
        TC5: Modo noturno na madrugada (< 6h).
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

    def test_tc6_night_mode_early_morning_disabled_with_6_hours(self):
        """
        TC6: Modo noturno na madrugada desativado (== 6h).
        Cobertura: Aresta nó 5 → nó 15 (current_time.hour == 6)
        """
        early_morning = datetime(2024, 1, 1, 6, 0, 0)
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

        assert result.device_status["Light"] is True
        assert result.device_status["Security"] is True
        assert result.device_status["Refrigerator"] is True

    def test_tc7_night_mode_early_morning_disabled_with_time_within_6_and_7_hours(self):
        """
        TC7: Modo noturno na madrugada desativado (> 6h e < 7h).
        Cobertura: Aresta nó 5 → nó 15 (current_time.hour > 6 e current_time.hour < 7)
        """
        early_morning = datetime(2024, 1, 1, 6, 30, 0)
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

        assert result.device_status["Light"] is True
        assert result.device_status["Security"] is True
        assert result.device_status["Refrigerator"] is True

    def test_tc8_low_temperature_heating_activated(self):
        """
        TC8: Temperatura baixa - aquecimento ativado.
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

    def test_tc9_low_temperature_heating_and_cooling_not_activated(self):
        """
        TC9: Temperatura baixa, porém nâo atingiu o mínimo para que o aquecimento seja ligado ainda - aquecimento e resfriamento desligado.
        Cobertura: Aresta nó 16 → nó 21 (current_temperature <= desired_temperature_range[0])
        Par def-uso: temperature_regulation_active definido (linha 46), usado no retorno
        """
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Heating": 1, "Cooling": 1},
            current_time=self.base_time,
            current_temperature=18.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[]
        )

        assert result.device_status["Heating"] is False
        assert result.device_status["Cooling"] is False
        assert result.temperature_regulation_active is False


    def test_tc10_high_temperature_cooling_activated(self):
        """
        TC10: Temperatura alta - resfriamento ativado.
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

    def test_tc11_high_temperature_heating_and_cooling_not_activated(self):
        """
        TC11: Temperatura alta, porém nâo atingiu o mínimo para que o resfriamento seja ligado - aquecimento e resfriamento desligado.
        Cobertura: Aresta nó 16 → nó 23 → nó 24 (current_temperature > desired_temperature_range[1])
        Par def-uso: device_status["Cooling"] definido (linha 48)
        """
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Heating": 1, "Cooling": 1},
            current_time=self.base_time,
            current_temperature=24.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[]
        )
        
        assert result.device_status["Heating"] is False
        assert result.device_status["Cooling"] is False
        assert result.temperature_regulation_active is False

    def test_tc12_ideal_temperature_climate_control_off(self):
        """
        TC12: Temperatura ideal - climatização desligada.
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


    def test_tc13_energy_limit_loop_devices_turned_off(self):
        """
        TC13: Loop de limite de energia - dispositivos desligados.
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

    def test_tc14_energy_limit_loop_devices_turned_off_with_equal_energy_limit_and_used_today(self):
        """
        TC14: Loop de limite de energia - dispositivos desligados.
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
            total_energy_used_today=100.0,
            scheduled_devices=[]
        )
        assert result.total_energy_used < 120.0

    def test_tc15_energy_limit_loop_exit_by_limit(self):
        """
        TC15: Loop de limite de energia - saída por atingir limite (break interno).
        Cobertura: Linha 68 (break quando total_energy_used_today < energy_usage_limit)
        Este teste força a condição onde, ao desligar dispositivos para economizar energia,
        o consumo cai abaixo do limite ANTES de processar todos os dispositivos da lista.
        Par def-uso: total_energy_used_today verificado durante loop (linha 67-68)
        """
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Light": 2, "TV": 3, "Radio": 4, "Alarm": 5, "Security": 1, "Heating": 1},
            current_time=self.base_time,
            current_temperature=15.0,  # Ativa aquecimento
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=102.5,  # Acima do limite com valor fracionário
            scheduled_devices=[]
        )
        # Com 102.5: desliga 1 (101.5), desliga 2 (100.5), desliga 3 (99.5 < 100, break!)
        assert result.total_energy_used < 100.0
        # Pelo menos um dispositivo de alta prioridade deve ainda estar ligado (não desligou todos)
        high_priority_devices = [result.device_status.get("Light"), result.device_status.get("TV"),
                                  result.device_status.get("Radio"), result.device_status.get("Alarm")]
        assert True in high_priority_devices  # Pelo menos 1 ainda ligado devido ao break

    def test_tc16_energy_limit_loop_no_devices_to_turn_off(self):
        """
        TC16: Loop de limite de energia - sem dispositivos para desligar.
        Cobertura: Aresta nó 28 → nó 30 (not devices_to_turn_off)
        Par def-uso: devices_were_on definido como False (linha 63)
        """
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Security": 1, "Refrigerator": 1},  # Todos prioridade 1
            current_time=self.base_time,
            current_temperature=20.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=110.0,
            scheduled_devices=[]
        )
        assert result.total_energy_used == 110.0

    def test_tc17_scheduled_devices_correct_time(self):
        """
        TC17: Dispositivos agendados - horário correto.
        Cobertura: Aresta nó 29 → nó 36 → nó 38 (schedule.scheduled_time == current_time)
        Par def-uso: device_status[schedule.device_name] definido (linha 75)
        """
        schedule_time = datetime(2024, 1, 1, 18, 0, 0)
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Light": 2},
            current_time=schedule_time,
            current_temperature=20.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[DeviceSchedule("Light", schedule_time)]
        )

        assert result.device_status["Light"] is True  # Ativado por agendamento

    def test_tc18_scheduled_devices_different_time(self):
        """
        TC18: Dispositivos agendados - horário diferente.
        Cobertura: Aresta nó 36 → nó 29 (schedule.scheduled_time != current_time)
        """
        current_time = datetime(2024, 1, 1, 18, 0, 0)
        schedule_time = datetime(2024, 1, 1, 19, 0, 0)  # 1 hora depois
        result = self.system.manage_energy(
            current_price=50.0,
            price_threshold=100.0,
            device_priorities={"Light": 2},
            current_time=current_time,
            current_temperature=20.0,
            desired_temperature_range=(18.0, 24.0),
            energy_usage_limit=100.0,
            total_energy_used_today=50.0,
            scheduled_devices=[DeviceSchedule("Light", schedule_time)]
        )

        assert result.device_status["Light"] is True

    def test_tc19_complex_combined_case(self):
        """
        TC19: Caso combinado complexo.
        Cobertura: Múltiplas arestas simultaneamente
        Testa interação entre diferentes modos
        """
        schedule_time = datetime(2024, 1, 1, 23, 30, 0)
        result = self.system.manage_energy(
            current_price=150.0,  # Ativa modo economia
            price_threshold=100.0,
            current_time=schedule_time,  # Modo noturno
            current_temperature=15.0,  # Ativa aquecimento
            desired_temperature_range=(18.0, 24.0),
            total_energy_used_today=105.0,  # Acima do limite
            energy_usage_limit=100.0,
            device_priorities={"Light": 2, "Heating": 1, "Security": 1, "TV": 3},
            scheduled_devices=[DeviceSchedule("Radio", schedule_time)]
        )
        assert result.energy_saving_mode is True
        assert result.temperature_regulation_active is True
        assert result.device_status["Heating"] is True
        assert result.device_status["Security"] is True
        assert result.device_status["Radio"] is True
        assert result.device_status["Light"] is False
        assert result.device_status["TV"] is False
