# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from magebank import Magebank, AsyncMagebank
from tests.utils import assert_matches_type
from magebank.types import (
    Payment,
    PaymentApproveResponse,
    PaymentDeclineResponse,
    PaymentRegisterResponse,
)
from magebank._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPayments:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server cannot handle dynamic path parameters")
    @parametrize
    def test_method_retrieve(self, client: Magebank) -> None:
        payment = client.payments.retrieve(
            "id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server cannot handle dynamic path parameters")
    @parametrize
    def test_raw_response_retrieve(self, client: Magebank) -> None:
        response = client.payments.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server cannot handle dynamic path parameters")
    @parametrize
    def test_streaming_response_retrieve(self, client: Magebank) -> None:
        with client.payments.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server cannot handle dynamic path parameters")
    @parametrize
    def test_path_params_retrieve(self, client: Magebank) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_approve(self, client: Magebank) -> None:
        payment = client.payments.approve(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        )
        assert_matches_type(PaymentApproveResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_approve(self, client: Magebank) -> None:
        response = client.payments.with_raw_response.approve(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentApproveResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_approve(self, client: Magebank) -> None:
        with client.payments.with_streaming_response.approve(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentApproveResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_decline(self, client: Magebank) -> None:
        payment = client.payments.decline(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        )
        assert_matches_type(PaymentDeclineResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_decline(self, client: Magebank) -> None:
        response = client.payments.with_raw_response.decline(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentDeclineResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_decline(self, client: Magebank) -> None:
        with client.payments.with_streaming_response.decline(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentDeclineResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_export(self, client: Magebank) -> None:
        payment = client.payments.export(
            format="csv",
        )
        assert payment is None

    @pytest.mark.skip()
    @parametrize
    def test_method_export_with_all_params(self, client: Magebank) -> None:
        payment = client.payments.export(
            format="csv",
            date_range={
                "end": parse_date("2019-12-27"),
                "start": parse_date("2019-12-27"),
            },
        )
        assert payment is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_export(self, client: Magebank) -> None:
        response = client.payments.with_raw_response.export(
            format="csv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert payment is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_export(self, client: Magebank) -> None:
        with client.payments.with_streaming_response.export(
            format="csv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert payment is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_register(self, client: Magebank) -> None:
        payment = client.payments.register(
            name="Vendor XYZ2",
            paymentdetails={
                "amount": 6,
                "currency": "USDC",
                "method": "CRYPTO_ADDRESS",
            },
            receiveragentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            senderagentid="agent_eC6ZezevNsqxvoKmQrUuoU",
        )
        assert_matches_type(PaymentRegisterResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_register_with_all_params(self, client: Magebank) -> None:
        payment = client.payments.register(
            name="Vendor XYZ2",
            paymentdetails={
                "amount": 6,
                "currency": "USDC",
                "method": "CRYPTO_ADDRESS",
            },
            receiveragentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            senderagentid="agent_eC6ZezevNsqxvoKmQrUuoU",
            contactdetails={
                "email": "contact@vendorxyz.com",
                "phone_number": "+1234567890",
            },
            tags=["vendor", "regular"],
            type="EXTERNAL",
        )
        assert_matches_type(PaymentRegisterResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_register(self, client: Magebank) -> None:
        response = client.payments.with_raw_response.register(
            name="Vendor XYZ2",
            paymentdetails={
                "amount": 6,
                "currency": "USDC",
                "method": "CRYPTO_ADDRESS",
            },
            receiveragentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            senderagentid="agent_eC6ZezevNsqxvoKmQrUuoU",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = response.parse()
        assert_matches_type(PaymentRegisterResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_register(self, client: Magebank) -> None:
        with client.payments.with_streaming_response.register(
            name="Vendor XYZ2",
            paymentdetails={
                "amount": 6,
                "currency": "USDC",
                "method": "CRYPTO_ADDRESS",
            },
            receiveragentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            senderagentid="agent_eC6ZezevNsqxvoKmQrUuoU",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = response.parse()
            assert_matches_type(PaymentRegisterResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPayments:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server cannot handle dynamic path parameters")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMagebank) -> None:
        payment = await async_client.payments.retrieve(
            "id",
        )
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server cannot handle dynamic path parameters")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMagebank) -> None:
        response = await async_client.payments.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(Payment, payment, path=["response"])

    @pytest.mark.skip(reason="Mock server cannot handle dynamic path parameters")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMagebank) -> None:
        async with async_client.payments.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(Payment, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server cannot handle dynamic path parameters")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMagebank) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.payments.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_approve(self, async_client: AsyncMagebank) -> None:
        payment = await async_client.payments.approve(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        )
        assert_matches_type(PaymentApproveResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_approve(self, async_client: AsyncMagebank) -> None:
        response = await async_client.payments.with_raw_response.approve(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentApproveResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_approve(self, async_client: AsyncMagebank) -> None:
        async with async_client.payments.with_streaming_response.approve(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentApproveResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_decline(self, async_client: AsyncMagebank) -> None:
        payment = await async_client.payments.decline(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        )
        assert_matches_type(PaymentDeclineResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_decline(self, async_client: AsyncMagebank) -> None:
        response = await async_client.payments.with_raw_response.decline(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentDeclineResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_decline(self, async_client: AsyncMagebank) -> None:
        async with async_client.payments.with_streaming_response.decline(
            payment_id="payee_c7m5fdJAfaV3R7VVpWk2MT",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentDeclineResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_export(self, async_client: AsyncMagebank) -> None:
        payment = await async_client.payments.export(
            format="csv",
        )
        assert payment is None

    @pytest.mark.skip()
    @parametrize
    async def test_method_export_with_all_params(self, async_client: AsyncMagebank) -> None:
        payment = await async_client.payments.export(
            format="csv",
            date_range={
                "end": parse_date("2019-12-27"),
                "start": parse_date("2019-12-27"),
            },
        )
        assert payment is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_export(self, async_client: AsyncMagebank) -> None:
        response = await async_client.payments.with_raw_response.export(
            format="csv",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert payment is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_export(self, async_client: AsyncMagebank) -> None:
        async with async_client.payments.with_streaming_response.export(
            format="csv",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert payment is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_register(self, async_client: AsyncMagebank) -> None:
        payment = await async_client.payments.register(
            name="Vendor XYZ2",
            paymentdetails={
                "amount": 6,
                "currency": "USDC",
                "method": "CRYPTO_ADDRESS",
            },
            receiveragentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            senderagentid="agent_eC6ZezevNsqxvoKmQrUuoU",
        )
        assert_matches_type(PaymentRegisterResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncMagebank) -> None:
        payment = await async_client.payments.register(
            name="Vendor XYZ2",
            paymentdetails={
                "amount": 6,
                "currency": "USDC",
                "method": "CRYPTO_ADDRESS",
            },
            receiveragentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            senderagentid="agent_eC6ZezevNsqxvoKmQrUuoU",
            contactdetails={
                "email": "contact@vendorxyz.com",
                "phone_number": "+1234567890",
            },
            tags=["vendor", "regular"],
            type="EXTERNAL",
        )
        assert_matches_type(PaymentRegisterResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_register(self, async_client: AsyncMagebank) -> None:
        response = await async_client.payments.with_raw_response.register(
            name="Vendor XYZ2",
            paymentdetails={
                "amount": 6,
                "currency": "USDC",
                "method": "CRYPTO_ADDRESS",
            },
            receiveragentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            senderagentid="agent_eC6ZezevNsqxvoKmQrUuoU",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        payment = await response.parse()
        assert_matches_type(PaymentRegisterResponse, payment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncMagebank) -> None:
        async with async_client.payments.with_streaming_response.register(
            name="Vendor XYZ2",
            paymentdetails={
                "amount": 6,
                "currency": "USDC",
                "method": "CRYPTO_ADDRESS",
            },
            receiveragentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            senderagentid="agent_eC6ZezevNsqxvoKmQrUuoU",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            payment = await response.parse()
            assert_matches_type(PaymentRegisterResponse, payment, path=["response"])

        assert cast(Any, response.is_closed) is True
