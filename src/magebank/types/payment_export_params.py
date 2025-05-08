# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["PaymentExportParams", "DateRange"]


class PaymentExportParams(TypedDict, total=False):
    format: Required[Literal["csv", "xlsx", "pdf"]]
    """Export format"""

    date_range: Annotated[DateRange, PropertyInfo(alias="dateRange")]


class DateRange(TypedDict, total=False):
    end: Annotated[Union[str, date], PropertyInfo(format="iso8601")]

    start: Annotated[Union[str, date], PropertyInfo(format="iso8601")]
