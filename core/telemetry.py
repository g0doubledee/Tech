"""
Divine Wallet Telemetry
Monitors system health — TECH Core uses this data to adapt
"""

import time
from datetime import datetime
from typing import Dict, List

class Telemetry:
    """System telemetry — feeds TECH Core adaptation loop"""
    
    _metrics = {
        "requests_total": 0,
        "requests_success": 0,
        "requests_failed": 0,
        "payments_processed": 0,
        "omega_payments_sent": 0,
        "tech_adaptations": 0,
        "errors_caught": 0,
        "system_uptime_start": time.time(),
        "reliability_score": 0.99
    }
    
    _history = []
    
    @classmethod
    def record_request(cls, success: bool):
        cls._metrics["requests_total"] += 1
        if success:
            cls._metrics["requests_success"] += 1
        else:
            cls._metrics["requests_failed"] += 1
        cls._adapt()
    
    @classmethod
    def record_payment(cls):
        cls._metrics["payments_processed"] += 1
        cls._adapt()
    
    @classmethod
    def record_omega(cls):
        cls._metrics["omega_payments_sent"] += 1
    
    @classmethod
    def record_adaptation(cls):
        cls._metrics["tech_adaptations"] += 1
    
    @classmethod
    def record_error(cls):
        cls._metrics["errors_caught"] += 1
        cls._adapt()
    
    @classmethod
    def _adapt(cls):
        """TECH Core adaptation — never reaches 100%"""
        total = cls._metrics["requests_total"]
        if total > 0:
            success_rate = cls._metrics["requests_success"] / total
            # Adapt toward 99% — never 100%
            cls._metrics["reliability_score"] = min(0.99, success_rate + 0.001)
            cls._metrics["tech_adaptations"] += 1
    
    @classmethod
    def get_metrics(cls) -> Dict:
        uptime = time.time() - cls._metrics["system_uptime_start"]
        return {
            **cls._metrics,
            "uptime_seconds": uptime,
            "uptime_formatted": f"{uptime/3600:.1f} hours",
            "reliability_target": "99%",
            "message": "Never 100% — perfection means no improvement"
        }
    
    @classmethod
    def get_reliability(cls) -> float:
        return cls._metrics["reliability_score"]