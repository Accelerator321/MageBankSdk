# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SavingListInvestmentsResponse", "Agent"]


class Agent(BaseModel):
    agent: Optional[str] = None
    """Name of the agent"""

    current: Optional[float] = None
    """Current balance in agent's account"""

    current_value: Optional[float] = FieldInfo(alias="currentValue", default=None)
    """Current value with interest"""

    days_invested: Optional[float] = FieldInfo(alias="daysInvested", default=None)
    """Days the investment has been active"""

    interest: Optional[float] = None
    """Interest earned to date"""

    invested_amount: Optional[float] = FieldInfo(alias="investedAmount", default=None)
    """Principal amount invested"""

    total_balance: Optional[float] = FieldInfo(alias="totalBalance", default=None)
    """Total balance including investment value"""


class SavingListInvestmentsResponse(BaseModel):
    agents: Optional[List[Agent]] = None
    """List of agents with active investments"""
