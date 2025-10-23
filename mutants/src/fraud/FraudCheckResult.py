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
class FraudCheckResult:
    """Armazena os resultados de uma verificação de detecção de fraude."""
    def xǁFraudCheckResultǁ__init____mutmut_orig(self, is_fraudulent: bool, is_blocked: bool, verification_required: bool, risk_score: int):
        self.is_fraudulent = is_fraudulent
        self.is_blocked = is_blocked
        self.verification_required = verification_required
        self.risk_score = risk_score
    def xǁFraudCheckResultǁ__init____mutmut_1(self, is_fraudulent: bool, is_blocked: bool, verification_required: bool, risk_score: int):
        self.is_fraudulent = None
        self.is_blocked = is_blocked
        self.verification_required = verification_required
        self.risk_score = risk_score
    def xǁFraudCheckResultǁ__init____mutmut_2(self, is_fraudulent: bool, is_blocked: bool, verification_required: bool, risk_score: int):
        self.is_fraudulent = is_fraudulent
        self.is_blocked = None
        self.verification_required = verification_required
        self.risk_score = risk_score
    def xǁFraudCheckResultǁ__init____mutmut_3(self, is_fraudulent: bool, is_blocked: bool, verification_required: bool, risk_score: int):
        self.is_fraudulent = is_fraudulent
        self.is_blocked = is_blocked
        self.verification_required = None
        self.risk_score = risk_score
    def xǁFraudCheckResultǁ__init____mutmut_4(self, is_fraudulent: bool, is_blocked: bool, verification_required: bool, risk_score: int):
        self.is_fraudulent = is_fraudulent
        self.is_blocked = is_blocked
        self.verification_required = verification_required
        self.risk_score = None
    
    xǁFraudCheckResultǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁFraudCheckResultǁ__init____mutmut_1': xǁFraudCheckResultǁ__init____mutmut_1, 
        'xǁFraudCheckResultǁ__init____mutmut_2': xǁFraudCheckResultǁ__init____mutmut_2, 
        'xǁFraudCheckResultǁ__init____mutmut_3': xǁFraudCheckResultǁ__init____mutmut_3, 
        'xǁFraudCheckResultǁ__init____mutmut_4': xǁFraudCheckResultǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁFraudCheckResultǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁFraudCheckResultǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁFraudCheckResultǁ__init____mutmut_orig)
    xǁFraudCheckResultǁ__init____mutmut_orig.__name__ = 'xǁFraudCheckResultǁ__init__'

    def __repr__(self) -> str:
        """Retorna uma representação legível do objeto."""
        return (f"FraudCheckResult(is_fraudulent={self.is_fraudulent}, "
                f"is_blocked={self.is_blocked}, "
                f"verification_required={self.verification_required}, "
                f"risk_score={self.risk_score})")