# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from magebank import Magebank, AsyncMagebank
from tests.utils import assert_matches_type
from magebank.types import (
    InvestmentCalculateInterestResponse,
    InvestmentRetrieveInterestRateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvestment:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_calculate_interest(self, client: Magebank) -> None:
        investment = client.investment.calculate_interest(
            amount=1000,
            days=365,
        )
        assert_matches_type(InvestmentCalculateInterestResponse, investment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_calculate_interest_with_all_params(self, client: Magebank) -> None:
        investment = client.investment.calculate_interest(
            amount=1000,
            days=365,
            custom_rate=4.5,
        )
        assert_matches_type(InvestmentCalculateInterestResponse, investment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_calculate_interest(self, client: Magebank) -> None:
        response = client.investment.with_raw_response.calculate_interest(
            amount=1000,
            days=365,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investment = response.parse()
        assert_matches_type(InvestmentCalculateInterestResponse, investment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_calculate_interest(self, client: Magebank) -> None:
        with client.investment.with_streaming_response.calculate_interest(
            amount=1000,
            days=365,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investment = response.parse()
            assert_matches_type(InvestmentCalculateInterestResponse, investment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_interest_rate(self, client: Magebank) -> None:
        investment = client.investment.retrieve_interest_rate()
        assert_matches_type(InvestmentRetrieveInterestRateResponse, investment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_interest_rate(self, client: Magebank) -> None:
        response = client.investment.with_raw_response.retrieve_interest_rate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investment = response.parse()
        assert_matches_type(InvestmentRetrieveInterestRateResponse, investment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_interest_rate(self, client: Magebank) -> None:
        with client.investment.with_streaming_response.retrieve_interest_rate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investment = response.parse()
            assert_matches_type(InvestmentRetrieveInterestRateResponse, investment, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncInvestment:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_calculate_interest(self, async_client: AsyncMagebank) -> None:
        investment = await async_client.investment.calculate_interest(
            amount=1000,
            days=365,
        )
        assert_matches_type(InvestmentCalculateInterestResponse, investment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_calculate_interest_with_all_params(self, async_client: AsyncMagebank) -> None:
        investment = await async_client.investment.calculate_interest(
            amount=1000,
            days=365,
            custom_rate=4.5,
        )
        assert_matches_type(InvestmentCalculateInterestResponse, investment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_calculate_interest(self, async_client: AsyncMagebank) -> None:
        response = await async_client.investment.with_raw_response.calculate_interest(
            amount=1000,
            days=365,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investment = await response.parse()
        assert_matches_type(InvestmentCalculateInterestResponse, investment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_calculate_interest(self, async_client: AsyncMagebank) -> None:
        async with async_client.investment.with_streaming_response.calculate_interest(
            amount=1000,
            days=365,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investment = await response.parse()
            assert_matches_type(InvestmentCalculateInterestResponse, investment, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_interest_rate(self, async_client: AsyncMagebank) -> None:
        investment = await async_client.investment.retrieve_interest_rate()
        assert_matches_type(InvestmentRetrieveInterestRateResponse, investment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_interest_rate(self, async_client: AsyncMagebank) -> None:
        response = await async_client.investment.with_raw_response.retrieve_interest_rate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        investment = await response.parse()
        assert_matches_type(InvestmentRetrieveInterestRateResponse, investment, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_interest_rate(self, async_client: AsyncMagebank) -> None:
        async with async_client.investment.with_streaming_response.retrieve_interest_rate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            investment = await response.parse()
            assert_matches_type(InvestmentRetrieveInterestRateResponse, investment, path=["response"])

        assert cast(Any, response.is_closed) is True
