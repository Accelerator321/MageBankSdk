# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from magebank import Magebank, AsyncMagebank
from tests.utils import assert_matches_type
from magebank.types import (
    SavingDepositResponse,
    SavingWithdrawResponse,
    SavingListInvestmentsResponse,
    SavingCalculateInterestResponse,
    SavingRetrieveDashboardResponse,
    SavingRetrieveInterestRateResponse,
    SavingListInvestmentsByAgentResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSavings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    def test_method_calculate_interest(self, client: Magebank) -> None:
        saving = client.savings.calculate_interest(
            amount=1000,
            days=365,
        )
        assert_matches_type(SavingCalculateInterestResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_method_calculate_interest_with_all_params(self, client: Magebank) -> None:
        saving = client.savings.calculate_interest(
            amount=1000,
            days=365,
            custom_rate=4.5,
        )
        assert_matches_type(SavingCalculateInterestResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_calculate_interest(self, client: Magebank) -> None:
        response = client.savings.with_raw_response.calculate_interest(
            amount=1000,
            days=365,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = response.parse()
        assert_matches_type(SavingCalculateInterestResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_calculate_interest(self, client: Magebank) -> None:
        with client.savings.with_streaming_response.calculate_interest(
            amount=1000,
            days=365,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = response.parse()
            assert_matches_type(SavingCalculateInterestResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_deposit(self, client: Magebank) -> None:
        saving = client.savings.deposit(
            agent_id="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=100.5,
        )
        assert_matches_type(SavingDepositResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_deposit(self, client: Magebank) -> None:
        response = client.savings.with_raw_response.deposit(
            agent_id="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=100.5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = response.parse()
        assert_matches_type(SavingDepositResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_deposit(self, client: Magebank) -> None:
        with client.savings.with_streaming_response.deposit(
            agent_id="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=100.5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = response.parse()
            assert_matches_type(SavingDepositResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_investments(self, client: Magebank) -> None:
        saving = client.savings.list_investments()
        assert_matches_type(SavingListInvestmentsResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_investments(self, client: Magebank) -> None:
        response = client.savings.with_raw_response.list_investments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = response.parse()
        assert_matches_type(SavingListInvestmentsResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_investments(self, client: Magebank) -> None:
        with client.savings.with_streaming_response.list_investments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = response.parse()
            assert_matches_type(SavingListInvestmentsResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_list_investments_by_agent(self, client: Magebank) -> None:
        saving = client.savings.list_investments_by_agent(
            "agentId",
        )
        assert_matches_type(SavingListInvestmentsByAgentResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_list_investments_by_agent(self, client: Magebank) -> None:
        response = client.savings.with_raw_response.list_investments_by_agent(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = response.parse()
        assert_matches_type(SavingListInvestmentsByAgentResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_list_investments_by_agent(self, client: Magebank) -> None:
        with client.savings.with_streaming_response.list_investments_by_agent(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = response.parse()
            assert_matches_type(SavingListInvestmentsByAgentResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_path_params_list_investments_by_agent(self, client: Magebank) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            client.savings.with_raw_response.list_investments_by_agent(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_dashboard(self, client: Magebank) -> None:
        saving = client.savings.retrieve_dashboard()
        assert_matches_type(SavingRetrieveDashboardResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_dashboard(self, client: Magebank) -> None:
        response = client.savings.with_raw_response.retrieve_dashboard()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = response.parse()
        assert_matches_type(SavingRetrieveDashboardResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_dashboard(self, client: Magebank) -> None:
        with client.savings.with_streaming_response.retrieve_dashboard() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = response.parse()
            assert_matches_type(SavingRetrieveDashboardResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_retrieve_interest_rate(self, client: Magebank) -> None:
        saving = client.savings.retrieve_interest_rate()
        assert_matches_type(SavingRetrieveInterestRateResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_retrieve_interest_rate(self, client: Magebank) -> None:
        response = client.savings.with_raw_response.retrieve_interest_rate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = response.parse()
        assert_matches_type(SavingRetrieveInterestRateResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_retrieve_interest_rate(self, client: Magebank) -> None:
        with client.savings.with_streaming_response.retrieve_interest_rate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = response.parse()
            assert_matches_type(SavingRetrieveInterestRateResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    def test_method_withdraw(self, client: Magebank) -> None:
        saving = client.savings.withdraw(
            investment_id="inv_k77NTwxp2Ym3JCmVsKtXQA",
        )
        assert_matches_type(SavingWithdrawResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_raw_response_withdraw(self, client: Magebank) -> None:
        response = client.savings.with_raw_response.withdraw(
            investment_id="inv_k77NTwxp2Ym3JCmVsKtXQA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = response.parse()
        assert_matches_type(SavingWithdrawResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    def test_streaming_response_withdraw(self, client: Magebank) -> None:
        with client.savings.with_streaming_response.withdraw(
            investment_id="inv_k77NTwxp2Ym3JCmVsKtXQA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = response.parse()
            assert_matches_type(SavingWithdrawResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSavings:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_calculate_interest(self, async_client: AsyncMagebank) -> None:
        saving = await async_client.savings.calculate_interest(
            amount=1000,
            days=365,
        )
        assert_matches_type(SavingCalculateInterestResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_method_calculate_interest_with_all_params(self, async_client: AsyncMagebank) -> None:
        saving = await async_client.savings.calculate_interest(
            amount=1000,
            days=365,
            custom_rate=4.5,
        )
        assert_matches_type(SavingCalculateInterestResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_calculate_interest(self, async_client: AsyncMagebank) -> None:
        response = await async_client.savings.with_raw_response.calculate_interest(
            amount=1000,
            days=365,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = await response.parse()
        assert_matches_type(SavingCalculateInterestResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_calculate_interest(self, async_client: AsyncMagebank) -> None:
        async with async_client.savings.with_streaming_response.calculate_interest(
            amount=1000,
            days=365,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = await response.parse()
            assert_matches_type(SavingCalculateInterestResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_deposit(self, async_client: AsyncMagebank) -> None:
        saving = await async_client.savings.deposit(
            agent_id="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=100.5,
        )
        assert_matches_type(SavingDepositResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_deposit(self, async_client: AsyncMagebank) -> None:
        response = await async_client.savings.with_raw_response.deposit(
            agent_id="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=100.5,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = await response.parse()
        assert_matches_type(SavingDepositResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_deposit(self, async_client: AsyncMagebank) -> None:
        async with async_client.savings.with_streaming_response.deposit(
            agent_id="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=100.5,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = await response.parse()
            assert_matches_type(SavingDepositResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_investments(self, async_client: AsyncMagebank) -> None:
        saving = await async_client.savings.list_investments()
        assert_matches_type(SavingListInvestmentsResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_investments(self, async_client: AsyncMagebank) -> None:
        response = await async_client.savings.with_raw_response.list_investments()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = await response.parse()
        assert_matches_type(SavingListInvestmentsResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_investments(self, async_client: AsyncMagebank) -> None:
        async with async_client.savings.with_streaming_response.list_investments() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = await response.parse()
            assert_matches_type(SavingListInvestmentsResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_list_investments_by_agent(self, async_client: AsyncMagebank) -> None:
        saving = await async_client.savings.list_investments_by_agent(
            "agentId",
        )
        assert_matches_type(SavingListInvestmentsByAgentResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_list_investments_by_agent(self, async_client: AsyncMagebank) -> None:
        response = await async_client.savings.with_raw_response.list_investments_by_agent(
            "agentId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = await response.parse()
        assert_matches_type(SavingListInvestmentsByAgentResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_list_investments_by_agent(self, async_client: AsyncMagebank) -> None:
        async with async_client.savings.with_streaming_response.list_investments_by_agent(
            "agentId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = await response.parse()
            assert_matches_type(SavingListInvestmentsByAgentResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_path_params_list_investments_by_agent(self, async_client: AsyncMagebank) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `agent_id` but received ''"):
            await async_client.savings.with_raw_response.list_investments_by_agent(
                "",
            )

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_dashboard(self, async_client: AsyncMagebank) -> None:
        saving = await async_client.savings.retrieve_dashboard()
        assert_matches_type(SavingRetrieveDashboardResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_dashboard(self, async_client: AsyncMagebank) -> None:
        response = await async_client.savings.with_raw_response.retrieve_dashboard()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = await response.parse()
        assert_matches_type(SavingRetrieveDashboardResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_dashboard(self, async_client: AsyncMagebank) -> None:
        async with async_client.savings.with_streaming_response.retrieve_dashboard() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = await response.parse()
            assert_matches_type(SavingRetrieveDashboardResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_retrieve_interest_rate(self, async_client: AsyncMagebank) -> None:
        saving = await async_client.savings.retrieve_interest_rate()
        assert_matches_type(SavingRetrieveInterestRateResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_retrieve_interest_rate(self, async_client: AsyncMagebank) -> None:
        response = await async_client.savings.with_raw_response.retrieve_interest_rate()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = await response.parse()
        assert_matches_type(SavingRetrieveInterestRateResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_retrieve_interest_rate(self, async_client: AsyncMagebank) -> None:
        async with async_client.savings.with_streaming_response.retrieve_interest_rate() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = await response.parse()
            assert_matches_type(SavingRetrieveInterestRateResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip()
    @parametrize
    async def test_method_withdraw(self, async_client: AsyncMagebank) -> None:
        saving = await async_client.savings.withdraw(
            investment_id="inv_k77NTwxp2Ym3JCmVsKtXQA",
        )
        assert_matches_type(SavingWithdrawResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_raw_response_withdraw(self, async_client: AsyncMagebank) -> None:
        response = await async_client.savings.with_raw_response.withdraw(
            investment_id="inv_k77NTwxp2Ym3JCmVsKtXQA",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saving = await response.parse()
        assert_matches_type(SavingWithdrawResponse, saving, path=["response"])

    @pytest.mark.skip()
    @parametrize
    async def test_streaming_response_withdraw(self, async_client: AsyncMagebank) -> None:
        async with async_client.savings.with_streaming_response.withdraw(
            investment_id="inv_k77NTwxp2Ym3JCmVsKtXQA",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saving = await response.parse()
            assert_matches_type(SavingWithdrawResponse, saving, path=["response"])

        assert cast(Any, response.is_closed) is True
