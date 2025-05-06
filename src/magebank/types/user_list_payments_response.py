# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .payment import Payment

__all__ = ["UserListPaymentsResponse", "UserListPaymentsResponseItem"]


class UserListPaymentsResponseItem(Payment):
    direction: Optional[Literal["incoming", "outgoing"]] = None
    """Direction of the payment relative to the user's agents"""

    initiated_by: Optional[str] = FieldInfo(alias="initiatedBy", default=None)
    """Name of the agent that initiated the payment"""

    received_by: Optional[str] = FieldInfo(alias="receivedBy", default=None)
    """Name of the agent that received the payment"""


UserListPaymentsResponse: TypeAlias = List[UserListPaymentsResponseItem]
