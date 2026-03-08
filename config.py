"""
Configuration and constants for PROTOCOL Ω
Adheres to strict type safety and environment-based configuration
"""
import os
from dataclasses import dataclass
from typing import Dict, List, Optional
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class ChainConfig:
    """Base L2 chain configuration"""
    CHAIN_ID: int = 8453
    RPC_URL: str = os.getenv("BASE_RPC_URL", "https://mainnet.base.org")
    WS_RPC_URL: str = os.getenv("BASE_WS_RPC_URL", "wss://mainnet.base.org/ws")
    BLOCK_TIME_SECONDS: int = 2
    MAX_BLOCKS_FOR_SIMULATION: int = 100

@dataclass(frozen=True)
class ProtocolConfig:
    """Protocol-specific configuration"""
    # Top 5 protocols by fee revenue on Base (identified via DeFiLlama)
    TOP_PROTOCOLS: Dict[str, Dict[str, str]] = {
        "aerodrome": {
            "type": "AMM/DEX",
            "factory": "0x420DD381b31aEf6683db6B902084cB0FFcEe5dF3",
            "router": "0xcF77a3Ba9A5CA399B7c97c74d54e5b1Beb874E43",
            "fee_tiers": [100, 500, 2500, 10000]  # Basis points
        },
        "uniswap_v3": {
            "type": "Concentrated Liquidity",
            "factory": "0x33128a8fC17869897dcE68Ed026d694621f6FDfD",
            "quoter": "0x3d4e44Eb1374240CE5F1B871ab261CD16335B76a",
            "fee_tiers": [100, 500, 3000, 10000]
        },
        "maverick": {
            "type": "Dynamic AMM",
            "factory": "0xEb6625D65a0553c9dBc64449e56abFe519bd9c9B",
            "router": "0x32AED3Bce901DA12ca8489788F3A99fBe105f6bB",
            "fee_modes": ["static", "dynamic", "boosted"]
        },
        "compound_v3": {
            "type": "Lending",
            "comet": "0x46e6b214b524310239732D51387075E0e70970bf",  # USDC market
            "base_token": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"  # USDC
        },
        "aave_v3": {
            "type": "Lending/Flashloans",
            "pool": "0xA238Dd80C259a72e81d7e4664a9801593F98d1c5",
            "data_provider": "0x2d8A3C5677189723C4cB8873CfC9C8976FDF38Ac"
        }
    }
    
    # Minimum profit thresholds (USD)
    MIN_ARBITRAGE_PROFIT: float = 10.0
    GAS_PRICE_BUFFER_MULTIPLIER: float = 1.5

@dataclass(frozen=True)
class FirebaseConfig:
    """Firebase configuration for state persistence"""
    CREDENTIALS_PATH: str = os.getenv("FIREBASE_CREDENTIALS_PATH", "./firebase-credentials.json")
    PROJECT_ID: str = os.getenv("FIREBASE_PROJECT_ID", "protocol-omega")
    COLLECTIONS: Dict[str, str] = {
        "arbitrage_opportunities": "arbitrage_opportunities",
        "protocol_states": "protocol_states",
        "simulation_results": "simulation_results",
        "performance_metrics": "performance_metrics"
    }

@dataclass(frozen=True)
class SimulationConfig:
    """Shadow chain simulation configuration"""
    MAX_SIMULATION_DEPTH: int = 5
    SIMULATION_BLOCK_RANGE: int = 50
    PARALLEL_SIMULATIONS: int = 3
    STATE_CACHE_TTL_SECONDS: int = 30

# Global instances
CHAIN_CONFIG = ChainConfig()
PROTOCOL_CONFIG = ProtocolConfig()
FIREBASE_CONFIG = FirebaseConfig()
SIMULATION_CONFIG = SimulationConfig()