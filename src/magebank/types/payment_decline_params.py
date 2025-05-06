# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentDeclineParams"]


class PaymentDeclineParams(TypedDict, total=False):
    payment_id: Required[Annotated[str, PropertyInfo(alias="paymentId")]]
    """The short ID of the payment to decline"""
