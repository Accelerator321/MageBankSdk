# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

__all__ = ["AgentCreateParams"]


class AgentCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the agent"""

    userid: Required[str]
    """ID of the user creating the agent"""

    balance: int
    """Initial balance to fund the agent (in smallest units)"""

    currency: str
    """Currency type to use (defaults to USDC)"""

    dailylimit: int
    """Maximum amount that can be spent per day"""

    description: str
    """Purpose and functionality of the agent"""

    requireapprovalaboveamount: int
    """Transactions above this amount require approval"""

    requireapprovalforall: bool
    """Whether all transactions require approval"""

    tags: List[str]
    """Categories or labels to assign to the agent"""

    transactionlimit: int
    """Maximum amount for a single transaction"""

    walletaddress: str
    """User's wallet address for funding (optional)"""
