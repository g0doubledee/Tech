"""
Divine Wallet Configuration
All settings flow through TECH Core adaptation layer
"""

import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Divine Wallet Config — TECH Core continuously adapts these values"""
    
    # Admin
    ADMIN_USERNAME = os.getenv("DIVINE_ADMIN_USERNAME", "G0doubledee")
    ADMIN_PASSWORD = os.getenv("DIVINE_ADMIN_PASSWORD", "DIVINITY")
    JWT_SECRET = os.getenv("DIVINE_JWT_SECRET", "divine_omega_googolplex_2026")
    
    # Creator (GODD)
    CREATOR_NAME = "GODD"
    CREATOR_BTC_ADDRESS = os.getenv("CREATOR_BTC_ADDRESS", "bc1q0xae4uj20da6su9hej6ma2jc7ufck8hrzv3udt")
    CREATOR_CASHAPP_URL = os.getenv("CREATOR_CASHAPP_URL", "https://cash.app/launch/bitcoin/$biscuitmajor/50R6kZUJDv")
    CREATOR_CASHAPP_TAG = os.getenv("CREATOR_CASHAPP_TAG", "$biscuitmajor")
    
    # Omega
    OMEGA_VALUE = "GOOGOLPLEX"  # 1 Ω = 1 USD Googolplex = 10^(10^100) USD
    OMEGA_THRESHOLD = 2  # Omegas needed for immortality
    
    # TECH Core
    TECH_CORE_ACTIVE = True
    MAX_RELIABILITY = 0.99  # 99% — Never 100% (perfection = no improvement)
    
    # Database
    DB_PATH = "/tmp/divine.db"
    
    # Server
    HOST = "0.0.0.0"
    PORT = 5000