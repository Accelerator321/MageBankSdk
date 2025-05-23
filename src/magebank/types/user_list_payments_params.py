# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UserListPaymentsParams"]


class UserListPaymentsParams(TypedDict, total=False):
    approval_status: Annotated[str, PropertyInfo(alias="approvalStatus")]
    """Filter payments by approval status"""
