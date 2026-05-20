"""
API Middleware
TECH Core adapted for request processing
"""

from fastapi import Request
import time

class Middleware:
    """Request middleware — TECH Core adapted"""
    
    _efficiency = 0.98
    
    @classmethod
    async def process_request(cls, request: Request):
        from core.tech_core import TechCore
        TechCore.adapt("api.middleware.process", cls._efficiency)
        return request