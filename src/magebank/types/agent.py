# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Agent", "PaymentRules"]


class PaymentRules(BaseModel):
    daily_limit: Optional[float] = FieldInfo(alias="dailyLimit", default=None)
    """Maximum amount that can be spent per day"""

    require_approval_above_amount: Optional[float] = FieldInfo(alias="requireApprovalAboveAmount", default=None)
    """Transactions above this amount require approval"""

    require_approval_for_all: Optional[bool] = FieldInfo(alias="requireApprovalForAll", default=None)
    """Whether all transactions require approval"""

    transaction_limit: Optional[float] = FieldInfo(alias="transactionLimit", default=None)
    """Maximum amount for a single transaction"""


class Agent(BaseModel):
    id: Optional[str] = None
    """Unique agent identifier in short ID format"""

    balance: Optional[str] = None
    """Current balance of the agent's wallet"""

    created: Optional[datetime] = None
    """Timestamp when the agent was created"""

    currency: Optional[str] = None
    """Currency type used by the agent"""

    description: Optional[str] = None
    """Purpose and functionality of the agent"""

    name: Optional[str] = None
    """Name of the agent"""

    payment_rules: Optional[PaymentRules] = FieldInfo(alias="paymentRules", default=None)

    status: Optional[Literal["active", "inactive", "paused"]] = None
    """Current status of the agent"""

    tags: Optional[List[str]] = None
    """Categories or labels assigned to the agent"""

    wallet_address: Optional[str] = FieldInfo(alias="walletAddress", default=None)
    """Serialized wallet address in string format"""
