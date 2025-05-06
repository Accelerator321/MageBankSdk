# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["SavingListInvestmentsByAgentResponse", "Investment"]


class Investment(BaseModel):
    id: Optional[str] = None
    """Unique investment identifier in short ID format"""

    agent_id: Optional[str] = None
    """ID of the agent associated with this investment"""

    amount: Optional[float] = None
    """Principal amount invested"""

    current_value: Optional[str] = None
    """Current value of the investment including earned interest"""

    interest_earned: Optional[str] = None
    """Interest earned on the investment to date"""

    invested_at: Optional[datetime] = None
    """Timestamp when the investment was created"""

    status: Optional[Literal["active", "completed", "cancelled"]] = None
    """Current status of the investment"""


class SavingListInvestmentsByAgentResponse(BaseModel):
    investments: Optional[List[Investment]] = None
    """List of investments for the specified agent"""
