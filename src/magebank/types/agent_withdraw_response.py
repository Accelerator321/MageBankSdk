# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentWithdrawResponse"]


class AgentWithdrawResponse(BaseModel):
    message: Optional[str] = None

    success: Optional[bool] = None

    tx_hash: Optional[str] = FieldInfo(alias="txHash", default=None)

    updated_balance: Optional[str] = FieldInfo(alias="updatedBalance", default=None)
