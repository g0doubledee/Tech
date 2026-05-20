"""
Auth Module — JWT Authentication
TECH Core adapted for security
"""

import time
import jwt
from datetime import datetime, timedelta
from core.config import Config

class Auth:
    """Authentication — TECH Core adapted"""
    
    _efficiency = 0.97
    
    @classmethod
    def create_token(cls, username: str) -> str:
        from core.tech_core import TechCore
        TechCore.adapt("api.auth.create_token", cls._efficiency)
        
        return jwt.encode(
            {"sub": username, "exp": time.time() + 86400},
            Config.JWT_SECRET,
            algorithm="HS256"
        )
    
    @classmethod
    def verify_token(cls, token: str) -> dict:
        return jwt.decode(token, Config.JWT_SECRET, algorithms=["HS256"])