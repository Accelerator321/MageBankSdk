# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["PaymentRegisterResponse"]


class PaymentRegisterResponse(BaseModel):
    id: Optional[str] = None
    """Unique payment identifier in short ID format"""

    approval_required: Optional[bool] = FieldInfo(alias="approvalRequired", default=None)
    """Whether this payment requires approval"""

    createdat: Optional[datetime] = None
    """Timestamp when the payment was created"""

    name: Optional[str] = None
    """Name or description of the payment"""

    status: Optional[str] = None
    """Current status of the payment"""

    type: Optional[str] = None
    """Type of payment (External or Internal)"""
