# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UserRetrieveWalletBalanceResponse"]


class UserRetrieveWalletBalanceResponse(BaseModel):
    asset: Optional[str] = None
    """Asset type (cryptocurrency)"""

    balance: Optional[str] = None
    """Current wallet balance"""

    message: Optional[str] = None
    """Additional information about the balance retrieval"""

    source: Optional[str] = None
    """Source of the balance information"""

    success: Optional[bool] = None
    """Whether the operation was successful"""
