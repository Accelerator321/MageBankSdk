# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["AgentWithdrawParams"]


class AgentWithdrawParams(TypedDict, total=False):
    agentid: Required[str]
    """ID of the agent sending the funds"""

    amount: Required[float]
    """Amount to withdraw"""

    userid: Required[str]
    """ID of the user receiving the withdrawal"""

    currency: str
    """Currency type to withdraw (defaults to USDC)"""
