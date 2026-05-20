"""
Transaction Model
TECH Core adapted — continuously improving
"""

from datetime import datetime
from decimal import Decimal
from typing import Optional


class Transaction:
    """Divine Wallet Transaction Model"""
    
    def __init__(
        self,
        amount: float,
        tx_type: str,
        description: str = "",
        recipient: Optional[str] = None,
        status: str = "completed"
    ):
        self.amount = amount
        self.type = tx_type
        self.description = description
        self.recipient = recipient
        self.status = status
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> dict:
        return {
            "amount": self.amount,
            "type": self.type,
            "description": self.description,
            "recipient": self.recipient,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
    
    @classmethod
    def from_dict(cls, data: dict) -> "Transaction":
        return cls(
            amount=data.get("amount", 0),
            tx_type=data.get("type", "unknown"),
            description=data.get("description", ""),
            recipient=data.get("recipient"),
            status=data.get("status", "completed")
        )
    
    def __repr__(self):
        return f"<Transaction {self.type}: ${self.amount:,.2f} [{self.status}]>"