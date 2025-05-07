# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from magebank import Magebank, AsyncMagebank
from tests.utils import assert_matches_type
from magebank.types import (
    AgentCreateResponse,
    AgentDepositResponse,
    AgentRetrieveResponse,
    AgentWithdrawResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAgents:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: Magebank) -> None:
        agent = client.agents.create(
            name="Payment Assistant",
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: Magebank) -> None:
        agent = client.agents.create(
            name="Payment Assistant",
            userid="user_piXARPaD2jefNBGxzb84Qd",
            balance=6,
            currency="USDC",
            dailylimit=1000,
            description="Handles payment processing for customer support",
            requireapprovalaboveamount=50,
            requireapprovalforall=False,
            tags=["customer-support", "payments"],
            transactionlimit=100,
            walletaddress="0xa55B42bA7B639bB9CEc2dB2520aC8Cff588895f6",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: Magebank) -> None:
        response = client.agents.with_raw_response.create(
            name="Payment Assistant",
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: Magebank) -> None:
        with client.agents.with_streaming_response.create(
            name="Payment Assistant",
            userid="user_piXARPaD2jefNBGxzb84Qd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: Magebank) -> None:
        agent = client.agents.retrieve(
            "id",
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Magebank) -> None:
        response = client.agents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Magebank) -> None:
        with client.agents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Magebank) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.agents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    def test_method_deposit(self, client: Magebank) -> None:
        agent = client.agents.deposit(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )
        assert_matches_type(AgentDepositResponse, agent, path=["response"])

    @parametrize
    def test_method_deposit_with_all_params(self, client: Magebank) -> None:
        agent = client.agents.deposit(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
            currency="USDC",
        )
        assert_matches_type(AgentDepositResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_deposit(self, client: Magebank) -> None:
        response = client.agents.with_raw_response.deposit(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentDepositResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_deposit(self, client: Magebank) -> None:
        with client.agents.with_streaming_response.deposit(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentDepositResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_withdraw(self, client: Magebank) -> None:
        agent = client.agents.withdraw(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )
        assert_matches_type(AgentWithdrawResponse, agent, path=["response"])

    @parametrize
    def test_method_withdraw_with_all_params(self, client: Magebank) -> None:
        agent = client.agents.withdraw(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
            currency="USDC",
        )
        assert_matches_type(AgentWithdrawResponse, agent, path=["response"])

    @parametrize
    def test_raw_response_withdraw(self, client: Magebank) -> None:
        response = client.agents.with_raw_response.withdraw(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = response.parse()
        assert_matches_type(AgentWithdrawResponse, agent, path=["response"])

    @parametrize
    def test_streaming_response_withdraw(self, client: Magebank) -> None:
        with client.agents.with_streaming_response.withdraw(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = response.parse()
            assert_matches_type(AgentWithdrawResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAgents:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_create(self, async_client: AsyncMagebank) -> None:
        agent = await async_client.agents.create(
            name="Payment Assistant",
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMagebank) -> None:
        agent = await async_client.agents.create(
            name="Payment Assistant",
            userid="user_piXARPaD2jefNBGxzb84Qd",
            balance=6,
            currency="USDC",
            dailylimit=1000,
            description="Handles payment processing for customer support",
            requireapprovalaboveamount=50,
            requireapprovalforall=False,
            tags=["customer-support", "payments"],
            transactionlimit=100,
            walletaddress="0xa55B42bA7B639bB9CEc2dB2520aC8Cff588895f6",
        )
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMagebank) -> None:
        response = await async_client.agents.with_raw_response.create(
            name="Payment Assistant",
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentCreateResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMagebank) -> None:
        async with async_client.agents.with_streaming_response.create(
            name="Payment Assistant",
            userid="user_piXARPaD2jefNBGxzb84Qd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentCreateResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMagebank) -> None:
        agent = await async_client.agents.retrieve(
            "id",
        )
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMagebank) -> None:
        response = await async_client.agents.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMagebank) -> None:
        async with async_client.agents.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentRetrieveResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMagebank) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.agents.with_raw_response.retrieve(
                "",
            )

    @parametrize
    async def test_method_deposit(self, async_client: AsyncMagebank) -> None:
        agent = await async_client.agents.deposit(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )
        assert_matches_type(AgentDepositResponse, agent, path=["response"])

    @parametrize
    async def test_method_deposit_with_all_params(self, async_client: AsyncMagebank) -> None:
        agent = await async_client.agents.deposit(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
            currency="USDC",
        )
        assert_matches_type(AgentDepositResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_deposit(self, async_client: AsyncMagebank) -> None:
        response = await async_client.agents.with_raw_response.deposit(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentDepositResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_deposit(self, async_client: AsyncMagebank) -> None:
        async with async_client.agents.with_streaming_response.deposit(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentDepositResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_withdraw(self, async_client: AsyncMagebank) -> None:
        agent = await async_client.agents.withdraw(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )
        assert_matches_type(AgentWithdrawResponse, agent, path=["response"])

    @parametrize
    async def test_method_withdraw_with_all_params(self, async_client: AsyncMagebank) -> None:
        agent = await async_client.agents.withdraw(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
            currency="USDC",
        )
        assert_matches_type(AgentWithdrawResponse, agent, path=["response"])

    @parametrize
    async def test_raw_response_withdraw(self, async_client: AsyncMagebank) -> None:
        response = await async_client.agents.with_raw_response.withdraw(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        agent = await response.parse()
        assert_matches_type(AgentWithdrawResponse, agent, path=["response"])

    @parametrize
    async def test_streaming_response_withdraw(self, async_client: AsyncMagebank) -> None:
        async with async_client.agents.with_streaming_response.withdraw(
            agentid="agent_k77NTwxp2Ym3JCmVsKtXQA",
            amount=50,
            userid="user_piXARPaD2jefNBGxzb84Qd",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            agent = await response.parse()
            assert_matches_type(AgentWithdrawResponse, agent, path=["response"])

        assert cast(Any, response.is_closed) is True
