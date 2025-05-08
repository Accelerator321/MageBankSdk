# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from magebank import Magebank, AsyncMagebank
from magebank._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_summary(self, client: Magebank) -> None:
        transaction = client.transactions.retrieve_summary(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert transaction is None

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_summary(self, client: Magebank) -> None:
        response = client.transactions.with_raw_response.retrieve_summary(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert transaction is None

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_summary(self, client: Magebank) -> None:
        with client.transactions.with_streaming_response.retrieve_summary(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_summary(self, async_client: AsyncMagebank) -> None:
        transaction = await async_client.transactions.retrieve_summary(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )
        assert transaction is None

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_summary(self, async_client: AsyncMagebank) -> None:
        response = await async_client.transactions.with_raw_response.retrieve_summary(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert transaction is None

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_summary(self, async_client: AsyncMagebank) -> None:
        async with async_client.transactions.with_streaming_response.retrieve_summary(
            end_date=parse_datetime("2019-12-27T18:11:19.117Z"),
            start_date=parse_datetime("2019-12-27T18:11:19.117Z"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert transaction is None

        assert cast(Any, response.is_closed) is True
