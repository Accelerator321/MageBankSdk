# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SavingCreateDepositParams"]


class SavingCreateDepositParams(TypedDict, total=False):
    agent_id: Required[Annotated[str, PropertyInfo(alias="agentId")]]
    """The short ID or UUID of the agent"""

    amount: Required[float]
    """Amount to deposit (must be positive)"""
