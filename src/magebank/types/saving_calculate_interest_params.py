# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["SavingCalculateInterestParams"]


class SavingCalculateInterestParams(TypedDict, total=False):
    amount: Required[float]
    """Principal amount to invest"""

    days: Required[float]
    """Investment duration in days"""

    custom_rate: Annotated[float, PropertyInfo(alias="customRate")]
    """Optional custom interest rate (annual percentage)"""
