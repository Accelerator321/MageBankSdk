# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentDepositParams"]


class AgentDepositParams(TypedDict, total=False):
    agentid: Required[str]
    """ID of the agent receiving the deposit"""

    amount: Required[float]
    """Amount to deposit"""

    userid: Required[str]
    """ID of the user initiating the deposit"""

    currency: str
    """Currency type to deposit (defaults to USDC)"""
