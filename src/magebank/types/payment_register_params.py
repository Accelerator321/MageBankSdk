# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentRegisterParams", "Paymentdetails", "Contactdetails"]


class PaymentRegisterParams(TypedDict, total=False):
    name: Required[str]
    """Name or description of the payment"""

    paymentdetails: Required[Paymentdetails]

    receiveragentid: Required[str]
    """ID of the agent receiving the payment (short ID or UUID)"""

    senderagentid: Required[str]
    """ID of the agent sending the payment (short ID or UUID)"""

    contactdetails: Contactdetails

    tags: List[str]
    """Tags or categories for the payment"""

    type: Literal["EXTERNAL", "INTERNAL"]
    """Type of payment (EXTERNAL or INTERNAL)"""


class Paymentdetails(TypedDict, total=False):
    amount: Required[float]
    """Payment amount"""

    currency: Required[str]
    """Payment currency"""

    method: Required[Literal["CRYPTO_ADDRESS", "BANK_TRANSFER"]]
    """Payment method to use"""


class Contactdetails(TypedDict, total=False):
    email: str
    """Contact email for the payment recipient"""

    phone_number: Annotated[str, PropertyInfo(alias="phoneNumber")]
    """Contact phone number for the payment recipient"""
