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
class BookingResult:
    """
    Uma classe para armazenar o resultado de uma operação de reserva de voo.
    """
    def xǁBookingResultǁ__init____mutmut_orig(self, confirmation, total_price, refund_amount, points_used):
        self.confirmation = confirmation
        self.total_price = total_price
        self.refund_amount = refund_amount
        self.points_used = points_used
    def xǁBookingResultǁ__init____mutmut_1(self, confirmation, total_price, refund_amount, points_used):
        self.confirmation = None
        self.total_price = total_price
        self.refund_amount = refund_amount
        self.points_used = points_used
    def xǁBookingResultǁ__init____mutmut_2(self, confirmation, total_price, refund_amount, points_used):
        self.confirmation = confirmation
        self.total_price = None
        self.refund_amount = refund_amount
        self.points_used = points_used
    def xǁBookingResultǁ__init____mutmut_3(self, confirmation, total_price, refund_amount, points_used):
        self.confirmation = confirmation
        self.total_price = total_price
        self.refund_amount = None
        self.points_used = points_used
    def xǁBookingResultǁ__init____mutmut_4(self, confirmation, total_price, refund_amount, points_used):
        self.confirmation = confirmation
        self.total_price = total_price
        self.refund_amount = refund_amount
        self.points_used = None
    
    xǁBookingResultǁ__init____mutmut_mutants : ClassVar[MutantDict] = {
    'xǁBookingResultǁ__init____mutmut_1': xǁBookingResultǁ__init____mutmut_1, 
        'xǁBookingResultǁ__init____mutmut_2': xǁBookingResultǁ__init____mutmut_2, 
        'xǁBookingResultǁ__init____mutmut_3': xǁBookingResultǁ__init____mutmut_3, 
        'xǁBookingResultǁ__init____mutmut_4': xǁBookingResultǁ__init____mutmut_4
    }
    
    def __init__(self, *args, **kwargs):
        result = _mutmut_trampoline(object.__getattribute__(self, "xǁBookingResultǁ__init____mutmut_orig"), object.__getattribute__(self, "xǁBookingResultǁ__init____mutmut_mutants"), args, kwargs, self)
        return result 
    
    __init__.__signature__ = _mutmut_signature(xǁBookingResultǁ__init____mutmut_orig)
    xǁBookingResultǁ__init____mutmut_orig.__name__ = 'xǁBookingResultǁ__init__'

    def __repr__(self):
        """Retorna uma representação legível do objeto."""
        return (f"BookingResult(confirmation={self.confirmation}, "
                f"total_price={self.total_price:.2f}, "
                f"refund_amount={self.refund_amount:.2f}, "
                f"points_used={self.points_used})")