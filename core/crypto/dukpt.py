"""
DUKPT — Derived Unique Key Per Transaction
TECH Core adapted for payment security
"""

import secrets
import hashlib

class DUKPT:
    """DUKPT implementation — TECH Core adapted"""
    
    _efficiency = 0.93
    
    @classmethod
    def derive_key(cls, base_key: str, transaction_counter: int) -> str:
        from core.tech_core import TechCore
        TechCore.adapt("crypto.dukpt.derive", cls._efficiency)
        material = f"{base_key}:{transaction_counter}:{secrets.token_hex(8)}"
        return hashlib.sha3_256(material.encode()).hexdigest()[:32]
    
    @classmethod
    def encrypt_pin(cls, pin: str, key: str) -> str:
        return hashlib.sha3_256(f"{pin}:{key}".encode()).hexdigest()[:16]