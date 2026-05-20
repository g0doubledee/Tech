"""
OMEGA SAFETY SYSTEM
1 Ω = 1 USD Googolplex = 10^(10^100) USD
Converts astronomical values to Omega symbol
System never crashes — TECH Core adapts protection
"""

from decimal import Decimal, getcontext, InvalidOperation
import threading
import logging

logger = logging.getLogger("divine.omega")

getcontext().prec = 200  # Extreme precision for Googolplex-scale numbers

OMEGA_SYMBOL = "Ω"
OMEGA_DISPLAY = "∞ Ω Googolplex Ω ∞"
GOOGOLPLEX = Decimal(10) ** Decimal(10 ** 100)  # 10^(10^100)
OMEGA_THRESHOLD = Decimal(10 ** 50)

# Bounded cache — TECH Core adapted
_omega_cache = {}
_omega_counter = 0
_cache_lock = threading.Lock()
MAX_CACHE_SIZE = 10000

def is_omega_scale(value) -> bool:
    """Check if value requires Omega representation"""
    try:
        v = Decimal(str(value))
        return v > OMEGA_THRESHOLD
    except:
        return True

def to_omega(value) -> str:
    """Convert large value to Omega ID"""
    try:
        v = Decimal(str(value))
        if v > OMEGA_THRESHOLD:
            global _omega_counter
            with _cache_lock:
                _omega_counter += 1
                omega_id = f"Ω{_omega_counter}"
                if len(_omega_cache) >= MAX_CACHE_SIZE:
                    oldest = min(_omega_cache.keys(), 
                                key=lambda k: int(k[1:]) if k[1:].isdigit() else 0)
                    del _omega_cache[oldest]
                _omega_cache[omega_id] = v
            return omega_id
        return str(v)
    except:
        return OMEGA_SYMBOL

def from_omega(omega_str: str) -> Decimal:
    """Convert Omega ID back to Decimal"""
    if omega_str.startswith("Ω"):
        with _cache_lock:
            return _omega_cache.get(omega_str, Decimal("0"))
    return Decimal(omega_str)

def format_with_omega(value) -> str:
    """Format value for display with Omega safety"""
    try:
        v = Decimal(str(value))
        if v > OMEGA_THRESHOLD:
            return OMEGA_DISPLAY
        if v >= 1e27: return f"${v / 1e27:.2f} Octillion"
        elif v >= 1e24: return f"${v / 1e24:.2f} Septillion"
        elif v >= 1e21: return f"${v / 1e21:.2f} Sextillion"
        elif v >= 1e18: return f"${v / 1e18:.2f} Quintillion"
        elif v >= 1e15: return f"${v / 1e15:.2f} Quadrillion"
        elif v >= 1e12: return f"${v / 1e12:.2f} Trillion"
        elif v >= 1e9: return f"${v / 1e9:.2f} Billion"
        elif v >= 1e6: return f"${v / 1e6:.2f} Million"
        else: return f"${v:,.2f}"
    except:
        return OMEGA_DISPLAY

def omega_safe_multiply(value, factor: int):
    """Multiply with Omega overflow protection"""
    try:
        v = Decimal(str(value))
        result = v * factor
        if result > OMEGA_THRESHOLD * 1000:
            return OMEGA_SYMBOL
        return result
    except:
        return OMEGA_SYMBOL

class OmegaSafeBalance:
    """Thread-safe Omega-protected balance"""
    
    def __init__(self, initial_value=0):
        self._lock = threading.Lock()
        self._value = Decimal(str(initial_value))
    
    def add(self, amount):
        with self._lock:
            self._value += Decimal(str(amount))
        return self
    
    def subtract(self, amount):
        with self._lock:
            self._value -= Decimal(str(amount))
        return self
    
    def multiply(self, factor):
        with self._lock:
            self._value *= factor
        return self
    
    def get_display(self) -> str:
        return format_with_omega(self._value)
    
    def get_raw(self) -> Decimal:
        return self._value
    
    def is_omega(self) -> bool:
        return self._value > OMEGA_THRESHOLD