# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from magebank import Magebank, AsyncMagebank
from tests.utils import assert_matches_type
from magebank.types import UserListPaymentsResponse, UserRetrieveWalletBalanceResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_payments(self, client: Magebank) -> None:
        user = client.user.list_payments()
        assert_matches_type(UserListPaymentsResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_list_payments_with_all_params(self, client: Magebank) -> None:
        user = client.user.list_payments(
            approval_status="Waiting",
        )
        assert_matches_type(UserListPaymentsResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_payments(self, client: Magebank) -> None:
        response = client.user.with_raw_response.list_payments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserListPaymentsResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_payments(self, client: Magebank) -> None:
        with client.user.with_streaming_response.list_payments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserListPaymentsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_wallet_balance(self, client: Magebank) -> None:
        user = client.user.retrieve_wallet_balance()
        assert_matches_type(UserRetrieveWalletBalanceResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_wallet_balance(self, client: Magebank) -> None:
        response = client.user.with_raw_response.retrieve_wallet_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserRetrieveWalletBalanceResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_wallet_balance(self, client: Magebank) -> None:
        with client.user.with_streaming_response.retrieve_wallet_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserRetrieveWalletBalanceResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUser:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_payments(self, async_client: AsyncMagebank) -> None:
        user = await async_client.user.list_payments()
        assert_matches_type(UserListPaymentsResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_payments_with_all_params(self, async_client: AsyncMagebank) -> None:
        user = await async_client.user.list_payments(
            approval_status="Waiting",
        )
        assert_matches_type(UserListPaymentsResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_payments(self, async_client: AsyncMagebank) -> None:
        response = await async_client.user.with_raw_response.list_payments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserListPaymentsResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_payments(self, async_client: AsyncMagebank) -> None:
        async with async_client.user.with_streaming_response.list_payments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserListPaymentsResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_wallet_balance(self, async_client: AsyncMagebank) -> None:
        user = await async_client.user.retrieve_wallet_balance()
        assert_matches_type(UserRetrieveWalletBalanceResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_wallet_balance(self, async_client: AsyncMagebank) -> None:
        response = await async_client.user.with_raw_response.retrieve_wallet_balance()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserRetrieveWalletBalanceResponse, user, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_wallet_balance(self, async_client: AsyncMagebank) -> None:
        async with async_client.user.with_streaming_response.retrieve_wallet_balance() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserRetrieveWalletBalanceResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True
