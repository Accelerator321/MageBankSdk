# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["InvestmentRetrieveInterestRateResponse"]


class InvestmentRetrieveInterestRateResponse(BaseModel):
    interest_rate: Optional[float] = FieldInfo(alias="interestRate", default=None)
    """Current annual interest rate for investments"""

    last_updated: Optional[datetime] = FieldInfo(alias="lastUpdated", default=None)
    """Timestamp when the interest rate was last updated"""
