# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Payment", "Contactdetails", "Paymentdetails"]


class Contactdetails(BaseModel):
    email: Optional[str] = None
    """Contact email for the payment recipient"""

    phone_number: Optional[str] = FieldInfo(alias="phoneNumber", default=None)
    """Contact phone number for the payment recipient"""


class Paymentdetails(BaseModel):
    amount: Optional[float] = None
    """Payment amount"""

    currency: Optional[str] = None
    """Payment currency"""

    method: Optional[str] = None
    """Payment method used"""


class Payment(BaseModel):
    id: Optional[str] = None
    """Unique payment identifier in short ID format"""

    approvalrequired: Optional[bool] = None
    """Whether this payment requires approval"""

    approvalstatus: Optional[str] = None
    """Approval status of the payment"""

    approvedat: Optional[datetime] = None
    """Timestamp when the payment was approved/declined"""

    contactdetails: Optional[Contactdetails] = None

    createdat: Optional[datetime] = None
    """Timestamp when the payment was created"""

    name: Optional[str] = None
    """Name or description of the payment"""

    paymentdetails: Optional[Paymentdetails] = None

    receiveragentid: Optional[str] = None
    """ID of the agent receiving the payment"""

    senderagentid: Optional[str] = None
    """ID of the agent sending the payment"""

    status: Optional[Literal["New", "Confirmed", "Completed", "Failed"]] = None
    """Current status of the payment"""

    tags: Optional[List[str]] = None
    """Tags or categories for the payment"""

    type: Optional[Literal["EXTERNAL", "INTERNAL"]] = None
    """Type of payment (External or Internal)"""
