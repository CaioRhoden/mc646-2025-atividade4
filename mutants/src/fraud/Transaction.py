from datetime import datetime
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

class Transaction:
    """Representa uma única transação financeira."""
    def xǁTransactionǁ__init____mutmut_orig(self, amount: float, timestamp: datetime, location: str):
        self.amount = amount
        self.timestamp = timestamp
        self.location = location
    def xǁTransactionǁ__init____mutmut_1(self, amount: float, timestamp: datetime, location: str):
        self.amount = None
        self.timestamp = timestamp
        self.location = location
    def xǁTransactionǁ__init____mutmut_2(self, amount: float, timestamp: datetime, location: str):
        self.amount = amount
        self.timestamp = None
        self.location = location
    def xǁTransactionǁ__init____mutmut_3(self, amount: float, timestamp: datetime, location: str):
        self.amount = amount
        self.timestamp = timestamp
        self.location = None
    
    xǁTransactionǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁTransactionǁ__init____mutmut_1': xǁTransactionǁ__init____mutmut_1, 
        'xǁTransactionǁ__init____mutmut_2': xǁTransactionǁ__init____mutmut_2, 
        'xǁTransactionǁ__init____mutmut_3': xǁTransactionǁ__init____mutmut_3
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁTransactionǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁTransactionǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁTransactionǁ__init____mutmut_orig)
    xǁTransactionǁ__init____mutmut_orig.__name__ = 'xǁTransactionǁ__init__'

    def __repr__(self) -> str:
        """Retorna uma representação legível do objeto."""
        return f"Transaction(amount={self.amount}, timestamp='{self.timestamp}', location='{self.location}')"