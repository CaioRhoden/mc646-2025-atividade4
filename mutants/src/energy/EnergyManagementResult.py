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
class EnergyManagementResult:
    """Armazena os resultados da lógica de gerenciamento de energia."""
    def xǁEnergyManagementResultǁ__init____mutmut_orig(
        self,
        device_status: dict[str, bool],
        energy_saving_mode: bool,
        temperature_regulation_active: bool,
        total_energy_used: float,
    ):
        self.device_status = device_status
        self.energy_saving_mode = energy_saving_mode
        self.temperature_regulation_active = temperature_regulation_active
        self.total_energy_used = total_energy_used
    def xǁEnergyManagementResultǁ__init____mutmut_1(
        self,
        device_status: dict[str, bool],
        energy_saving_mode: bool,
        temperature_regulation_active: bool,
        total_energy_used: float,
    ):
        self.device_status = None
        self.energy_saving_mode = energy_saving_mode
        self.temperature_regulation_active = temperature_regulation_active
        self.total_energy_used = total_energy_used
    def xǁEnergyManagementResultǁ__init____mutmut_2(
        self,
        device_status: dict[str, bool],
        energy_saving_mode: bool,
        temperature_regulation_active: bool,
        total_energy_used: float,
    ):
        self.device_status = device_status
        self.energy_saving_mode = None
        self.temperature_regulation_active = temperature_regulation_active
        self.total_energy_used = total_energy_used
    def xǁEnergyManagementResultǁ__init____mutmut_3(
        self,
        device_status: dict[str, bool],
        energy_saving_mode: bool,
        temperature_regulation_active: bool,
        total_energy_used: float,
    ):
        self.device_status = device_status
        self.energy_saving_mode = energy_saving_mode
        self.temperature_regulation_active = None
        self.total_energy_used = total_energy_used
    def xǁEnergyManagementResultǁ__init____mutmut_4(
        self,
        device_status: dict[str, bool],
        energy_saving_mode: bool,
        temperature_regulation_active: bool,
        total_energy_used: float,
    ):
        self.device_status = device_status
        self.energy_saving_mode = energy_saving_mode
        self.temperature_regulation_active = temperature_regulation_active
        self.total_energy_used = None
    
    xǁEnergyManagementResultǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁEnergyManagementResultǁ__init____mutmut_1': xǁEnergyManagementResultǁ__init____mutmut_1, 
        'xǁEnergyManagementResultǁ__init____mutmut_2': xǁEnergyManagementResultǁ__init____mutmut_2, 
        'xǁEnergyManagementResultǁ__init____mutmut_3': xǁEnergyManagementResultǁ__init____mutmut_3, 
        'xǁEnergyManagementResultǁ__init____mutmut_4': xǁEnergyManagementResultǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁEnergyManagementResultǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁEnergyManagementResultǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁEnergyManagementResultǁ__init____mutmut_orig)
    xǁEnergyManagementResultǁ__init____mutmut_orig.__name__ = 'xǁEnergyManagementResultǁ__init__'

    def __repr__(self) -> str:
        """Retorna uma representação legível do objeto."""
        return (f"EnergyManagementResult(device_status={self.device_status}, "
                f"energy_saving_mode={self.energy_saving_mode}, "
                f"temperature_regulation_active={self.temperature_regulation_active}, "
                f"total_energy_used={self.total_energy_used})")
