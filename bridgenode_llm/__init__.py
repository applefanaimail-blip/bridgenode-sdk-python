"""bridgenode_llm — BridgeNode Python SDK (, ).

LLMClient: automatic x402 V2 handshake (402 → partial TX → PAYMENT-SIGNATURE
→ 200). Key from `.env` (`BRIDGENODE_WALLET_KEY`) — no arguments, no
interactive prompts ().
"""

from .client import BRIDGENODE_BASE_URL, BridgenodeError, LLMClient

__all__ = ["LLMClient", "BridgenodeError", "BRIDGENODE_BASE_URL"]
__version__ = "0.2.7"
