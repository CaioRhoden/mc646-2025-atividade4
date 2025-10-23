from datetime import datetime
from energy.DeviceSchedule import DeviceSchedule
from energy.EnergyManagementResult import EnergyManagementResult
from inspect import signature as _mutmut_signature
from typing import Annotated
from typing import Callable
from typing import ClassVar


MutantDict = Annotated[dict[str, Callable], "Mutant"]


def _mutmut_trampoline(orig, mutants, call_args, call_kwargs, self_arg = None):
    """Forward call to original or mutated function, depending on the environment"""
    import os
    mutant_under_test = os.environ['MUTANT_UNDER_TEST']
    if mutant_under_test == 'fail':
        from mutmut.__main__ import MutmutProgrammaticFailException
        raise MutmutProgrammaticFailException('Failed programmatically')      
    elif mutant_under_test == 'stats':
        from mutmut.__main__ import record_trampoline_hit
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__)
        result = orig(*call_args, **call_kwargs)
        return result
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_'
    if not mutant_under_test.startswith(prefix):
        result = orig(*call_args, **call_kwargs)
        return result
    mutant_name = mutant_under_test.rpartition('.')[-1]
    if self_arg:
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs)
    else:
        result = mutants[mutant_name](*call_args, **call_kwargs)
    return result

class SmartEnergyManagementSystem:
    """Um sistema para gerenciar inteligentemente o consumo de energia."""
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_orig(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_1(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = None
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_2(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = None
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_3(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = True
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_4(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = None

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_5(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = True

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_6(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price >= price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_7(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = None
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_8(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = False
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_9(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority >= 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_10(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 2:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_11(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = None
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_12(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = True
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_13(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = None 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_14(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = False 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_15(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = None

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_16(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = False

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_17(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 and current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_18(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour > 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_19(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 24 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_20(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour <= 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_21(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 7:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_22(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_23(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("XXSecurityXX", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_24(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_25(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("SECURITY", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_26(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "XXRefrigeratorXX"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_27(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_28(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "REFRIGERATOR"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_29(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = None

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_30(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = True

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_31(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature <= desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_32(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[1]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_33(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = None
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_34(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["XXHeatingXX"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_35(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_36(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["HEATING"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_37(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = False
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_38(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = None
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_39(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = False
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_40(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature >= desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_41(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[2]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_42(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = None
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_43(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["XXCoolingXX"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_44(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_45(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["COOLING"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_46(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = False
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_47(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = None
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_48(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = False
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_49(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = None
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_50(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["XXHeatingXX"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_51(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_52(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["HEATING"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_53(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = True
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_54(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = None


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_55(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["XXCoolingXX"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_56(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_57(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["COOLING"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_58(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = True


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_59(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = None
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_60(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = False
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_61(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit or devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_62(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today > energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_63(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = None
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_64(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) or priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_65(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(None, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_66(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, None) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_67(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_68(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, ) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_69(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, True) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_70(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority >= 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_71(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 2
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_72(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_73(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = None
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_74(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = True
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_75(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                break

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_76(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today <= energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_77(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     return
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_78(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = None
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_79(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = True
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_80(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today = 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_81(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today += 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_82(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 2

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_83(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time != current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_84(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = None

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_85(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = False

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_86(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(None, energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_87(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, None, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_88(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, None, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_89(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, None)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_90(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(energy_saving_mode, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_91(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, temperature_regulation_active, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_92(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, total_energy_used_today)
    def xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_93(
        self,
        current_price: float,
        price_threshold: float,
        device_priorities: dict[str, int],
        current_time: datetime,
        current_temperature: float,
        desired_temperature_range: tuple[float, float],
        energy_usage_limit: float,
        total_energy_used_today: float,
        scheduled_devices: list[DeviceSchedule],
    ) -> EnergyManagementResult:

        device_status: dict[str, bool] = {}
        energy_saving_mode = False
        temperature_regulation_active = False

        # 1. Ativa o modo de economia de energia se o preço exceder o limite
        if current_price > price_threshold:
            energy_saving_mode = True
            for device, priority in device_priorities.items():
                if priority > 1:  
                    device_status[device] = False
                else:
                    device_status[device] = True 
        else:
            # Sem modo de economia; mantém todos os dispositivos ligados inicialmente
            for device in device_priorities:
                device_status[device] = True

        # 2. Modo noturno entre 23h e 6h
        if current_time.hour >= 23 or current_time.hour < 6:
            for device in device_priorities:
                if device not in ("Security", "Refrigerator"):
                    device_status[device] = False

        # 3. Regulação de temperatura
        if current_temperature < desired_temperature_range[0]:
            device_status["Heating"] = True
            temperature_regulation_active = True
        elif current_temperature > desired_temperature_range[1]:
            device_status["Cooling"] = True
            temperature_regulation_active = True
        else:
            device_status["Heating"] = False
            device_status["Cooling"] = False


        devices_were_on = True
        while total_energy_used_today >= energy_usage_limit and devices_were_on:
            devices_to_turn_off = [
                device for device, priority in device_priorities.items()
                if device_status.get(device, False) and priority > 1
            ]
            
            if not devices_to_turn_off:
                devices_were_on = False
                continue

            for device in devices_to_turn_off:
                 if total_energy_used_today < energy_usage_limit:
                     break
                 device_status[device] = False
                 total_energy_used_today -= 1

        # 5. Lida com dispositivos agendados
        for schedule in scheduled_devices:
            if schedule.scheduled_time == current_time:
                device_status[schedule.device_name] = True

        return EnergyManagementResult(device_status, energy_saving_mode, temperature_regulation_active, )
    
    xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_mutants : ClassVar[MutantDict] = {
    'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_1': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_1, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_2': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_2, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_3': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_3, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_4': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_4, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_5': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_5, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_6': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_6, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_7': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_7, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_8': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_8, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_9': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_9, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_10': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_10, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_11': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_11, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_12': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_12, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_13': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_13, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_14': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_14, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_15': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_15, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_16': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_16, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_17': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_17, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_18': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_18, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_19': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_19, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_20': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_20, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_21': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_21, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_22': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_22, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_23': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_23, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_24': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_24, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_25': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_25, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_26': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_26, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_27': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_27, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_28': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_28, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_29': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_29, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_30': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_30, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_31': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_31, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_32': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_32, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_33': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_33, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_34': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_34, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_35': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_35, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_36': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_36, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_37': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_37, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_38': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_38, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_39': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_39, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_40': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_40, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_41': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_41, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_42': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_42, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_43': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_43, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_44': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_44, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_45': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_45, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_46': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_46, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_47': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_47, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_48': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_48, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_49': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_49, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_50': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_50, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_51': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_51, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_52': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_52, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_53': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_53, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_54': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_54, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_55': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_55, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_56': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_56, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_57': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_57, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_58': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_58, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_59': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_59, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_60': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_60, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_61': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_61, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_62': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_62, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_63': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_63, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_64': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_64, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_65': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_65, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_66': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_66, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_67': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_67, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_68': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_68, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_69': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_69, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_70': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_70, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_71': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_71, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_72': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_72, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_73': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_73, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_74': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_74, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_75': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_75, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_76': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_76, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_77': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_77, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_78': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_78, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_79': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_79, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_80': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_80, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_81': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_81, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_82': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_82, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_83': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_83, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_84': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_84, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_85': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_85, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_86': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_86, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_87': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_87, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_88': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_88, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_89': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_89, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_90': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_90, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_91': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_91, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_92': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_92, 
        'xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_93': xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_93
    }
    
    def manage_energy(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_orig"), object.__getattribute__(self, "xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_mutants"), args, kwargs, self)
        return result 
    
    manage_energy.__signature__ = _mutmut_signature(xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_orig)
    xǁSmartEnergyManagementSystemǁmanage_energy__mutmut_orig.__name__ = 'xǁSmartEnergyManagementSystemǁmanage_energy'
