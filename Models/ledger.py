"""
Ledger Entry Model
TECH Core adapted for financial records
"""

from decimal import Decimal
from datetime import datetime

class LedgerEntry:
    """Immutable ledger entry"""
    
    def __init__(self, amount: Decimal, entry_type: str, description: str = ""):
        self.amount = amount
        self.type = entry_type
        self.description = description
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        return {
            "amount": float(self.amount),
            "type": self.type,
            "description": self.description,
            "created_at": self.created_at
        }