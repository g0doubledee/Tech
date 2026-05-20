""""""
Ledger Entry Model
Immutable financial record — TECH Core adapted
"""

from datetime import datetime
from decimal import Decimal
from typing import Optional


class LedgerEntry:
    """Divine Wallet Ledger Entry — Immutable"""
    
    def __init__(
        self,
        amount: Decimal,
        entry_type: str,
        description: str = "",
        tx_hash: Optional[str] = None
    ):
        self.amount = amount
        self.type = entry_type
        self.description = description
        self.tx_hash = tx_hash
        self.created_at = datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        return {
            "amount": float(self.amount),
            "type": self.type,
            "description": self.description,
            "tx_hash": self.tx_hash,
            "created_at": self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "LedgerEntry":
        return cls(
            amount=Decimal(str(data.get("amount", 0))),
            entry_type=data.get("type", "unknown"),
            description=data.get("description", ""),
            tx_hash=data.get("tx_hash")
        )
    
    def __repr__(self):
        return f"<LedgerEntry {self.type}: {float(self.amount):,.2f} @ {self.created_at}>"
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