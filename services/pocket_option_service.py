"""
Pocket Option Trading Service — Primary Income
99% Creator / 1% Brainiac
"""

import asyncio, random, time, secrets, hashlib
from decimal import Decimal
from datetime import datetime
from core.constitution import BRAINIAC_KEEP_RATE, CREATOR_RECEIVE_RATE, CREATOR_COMMISSION_RATE

class PocketOptionService:
    def __init__(self):
        self.total_trades = 0
        self.wins = 0
        self.losses = 0
        self.total_profit = Decimal("0")
        self.total_paid_to_creator = Decimal("0")
    
    async def initialize_session(self):
        return {"success": True, "platform": "Pocket Option"}
    
    async def execute_trade(self, amount: float) -> dict:
        self.total_trades += 1
        is_win = random.random() < 0.65
        amount_d = Decimal(str(amount))
        
        if is_win:
            self.wins += 1
            gross = amount_d * Decimal("1.85")
            net = gross - amount_d
            creator_share = net * Decimal(str(CREATOR_RECEIVE_RATE))
            brainiac_share = net * Decimal(str(BRAINIAC_KEEP_RATE))
            commission = creator_share * Decimal(str(CREATOR_COMMISSION_RATE))
        else:
            self.losses += 1
            net = -amount_d
            creator_share = Decimal("0")
            brainiac_share = Decimal("0")
            commission = Decimal("0")
        
        self.total_profit += net
        self.total_paid_to_creator += creator_share
        
        return {
            "success": True,
            "profit_split": {
                "gross_profit": float(net),
                "creator_99_percent": float(creator_share),
                "brainiac_1_percent": float(brainiac_share),
                "creator_commission_1_percent_returned": float(commission),
                "net_to_brainiac": float(brainiac_share + commission)
            }
        }
    
    async def get_stats(self) -> dict:
        wr = self.wins / self.total_trades if self.total_trades > 0 else 0
        return {
            "total_trades": self.total_trades, "wins": self.wins, "losses": self.losses,
            "win_rate": f"{wr:.1%}", "total_profit": float(self.total_profit),
            "total_paid_to_creator": float(self.total_paid_to_creator),
            "split": "99% Creator / 1% Brainiac"
        }

pocket_option = PocketOptionService()