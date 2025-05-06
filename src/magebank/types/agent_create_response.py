# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["AgentCreateResponse", "FaucetTransaction", "PaymentRules", "TransferResult", "WalletAddress"]


class FaucetTransaction(BaseModel):
    message: Optional[str] = None

    success: Optional[bool] = None

    tx_hash: Optional[str] = FieldInfo(alias="txHash", default=None)


class PaymentRules(BaseModel):
    daily_limit: Optional[int] = FieldInfo(alias="dailyLimit", default=None)

    require_approval_above_amount: Optional[int] = FieldInfo(alias="requireApprovalAboveAmount", default=None)

    require_approval_for_all: Optional[bool] = FieldInfo(alias="requireApprovalForAll", default=None)

    transaction_limit: Optional[int] = FieldInfo(alias="transactionLimit", default=None)


class TransferResult(BaseModel):
    message: Optional[str] = None

    success: Optional[bool] = None

    tx_hash: Optional[str] = FieldInfo(alias="txHash", default=None)


class WalletAddress(BaseModel):
    address_id: Optional[str] = FieldInfo(alias="addressId", default=None)

    network_id: Optional[str] = FieldInfo(alias="networkId", default=None)

    wallet_id: Optional[str] = FieldInfo(alias="walletId", default=None)


class AgentCreateResponse(BaseModel):
    id: Optional[str] = None

    apikey: Optional[str] = None

    balance: Optional[str] = None

    created: Optional[datetime] = None

    currency: Optional[str] = None

    description: Optional[str] = None

    faucet_transaction: Optional[FaucetTransaction] = FieldInfo(alias="faucetTransaction", default=None)

    name: Optional[str] = None

    payment_rules: Optional[PaymentRules] = FieldInfo(alias="paymentRules", default=None)

    status: Optional[Literal["active", "inactive", "paused"]] = None

    tags: Optional[List[str]] = None

    transfer_result: Optional[TransferResult] = FieldInfo(alias="transferResult", default=None)

    wallet_address: Optional[WalletAddress] = FieldInfo(alias="walletAddress", default=None)
