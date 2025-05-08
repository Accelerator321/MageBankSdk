# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SavingGetDashboardResponse", "Agent"]


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

    investment_id: Optional[str] = None
    """Investment ID in short format"""

    total_balance: Optional[float] = FieldInfo(alias="totalBalance", default=None)
    """Total balance including investment value"""


class SavingGetDashboardResponse(BaseModel):
    agents: Optional[List[Agent]] = None
    """Detailed information about investments by agent"""

    interest_rate: Optional[float] = FieldInfo(alias="interestRate", default=None)
    """Current interest rate applied to investments"""

    total_invested: Optional[float] = FieldInfo(alias="totalInvested", default=None)
    """Total principal amount invested by the user"""

    total_savings: Optional[float] = FieldInfo(alias="totalSavings", default=None)
    """Total current value of all investments including interest"""

    year_projection: Optional[float] = FieldInfo(alias="yearProjection", default=None)
    """Projected value of investments after one year at current rate"""
