# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SavingCreateWithdrawalParams"]


class SavingCreateWithdrawalParams(TypedDict, total=False):
    investment_id: Required[Annotated[str, PropertyInfo(alias="investmentId")]]
    """The short ID or UUID of the investment"""
