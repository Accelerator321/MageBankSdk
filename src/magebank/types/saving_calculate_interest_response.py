# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["SavingCalculateInterestResponse", "Calculation"]


class Calculation(BaseModel):
    formula: Optional[str] = None
    """Formula used for calculation"""

    steps: Optional[List[str]] = None
    """Step-by-step calculation process"""


class SavingCalculateInterestResponse(BaseModel):
    annual_yield: Optional[str] = FieldInfo(alias="annualYield", default=None)
    """Effective annual yield as a percentage"""

    calculation: Optional[Calculation] = None
    """Details of the calculation steps"""

    days: Optional[float] = None
    """Investment duration in days"""

    interest_earned: Optional[str] = FieldInfo(alias="interestEarned", default=None)
    """Interest amount earned over the period"""

    interest_rate: Optional[float] = FieldInfo(alias="interestRate", default=None)
    """Annual interest rate applied to the calculation"""

    principal: Optional[float] = None
    """Principal amount for the calculation"""

    total_amount: Optional[str] = FieldInfo(alias="totalAmount", default=None)
    """Total amount including principal and interest"""
