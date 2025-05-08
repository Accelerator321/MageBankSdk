# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List

import httpx

from ..types import agent_create_params, agent_deposit_params, agent_withdraw_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.agent_create_response import AgentCreateResponse
from ..types.agent_deposit_response import AgentDepositResponse
from ..types.agent_retrieve_response import AgentRetrieveResponse
from ..types.agent_withdraw_response import AgentWithdrawResponse

__all__ = ["AgentsResource", "AsyncAgentsResource"]


class AgentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return AgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return AgentsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        userid: str,
        balance: int | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        dailylimit: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        requireapprovalaboveamount: int | NotGiven = NOT_GIVEN,
        requireapprovalforall: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transactionlimit: int | NotGiven = NOT_GIVEN,
        walletaddress: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentCreateResponse:
        """
        Creates a new agent, generates a wallet, and optionally funds the agent's wallet
        from the user's wallet. The operation includes: 1. Creation of a new agent
        record 2. Generation of a secure blockchain wallet 3. Faucet funding of the
        wallet (on supported test networks) 4. Optional transfer of funds from user's
        wallet

        Args:
          name: Name of the agent

          userid: ID of the user creating the agent

          balance: Initial balance to fund the agent (in smallest units)

          currency: Currency type to use (defaults to USDC)

          dailylimit: Maximum amount that can be spent per day

          description: Purpose and functionality of the agent

          requireapprovalaboveamount: Transactions above this amount require approval

          requireapprovalforall: Whether all transactions require approval

          tags: Categories or labels to assign to the agent

          transactionlimit: Maximum amount for a single transaction

          walletaddress: User's wallet address for funding (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agents/create",
            body=maybe_transform(
                {
                    "name": name,
                    "userid": userid,
                    "balance": balance,
                    "currency": currency,
                    "dailylimit": dailylimit,
                    "description": description,
                    "requireapprovalaboveamount": requireapprovalaboveamount,
                    "requireapprovalforall": requireapprovalforall,
                    "tags": tags,
                    "transactionlimit": transactionlimit,
                    "walletaddress": walletaddress,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentRetrieveResponse:
        """
        Returns an array of agents assigned to the user based on the provided user ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/agents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    def deposit(
        self,
        *,
        agentid: str,
        amount: float,
        userid: str,
        currency: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentDepositResponse:
        """Transfers funds from the user's wallet to the specified agent's wallet.

        The
        operation includes: 1. Verification of user and agent existence 2. Validation of
        deposit amount 3. Transfer of funds on blockchain 4. Update of agent balance in
        database 5. Creation of transaction record

        Args:
          agentid: ID of the agent receiving the deposit

          amount: Amount to deposit

          userid: ID of the user initiating the deposit

          currency: Currency type to deposit (defaults to USDC)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agents/deposit",
            body=maybe_transform(
                {
                    "agentid": agentid,
                    "amount": amount,
                    "userid": userid,
                    "currency": currency,
                },
                agent_deposit_params.AgentDepositParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDepositResponse,
        )

    def withdraw(
        self,
        *,
        agentid: str,
        amount: float,
        userid: str,
        currency: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentWithdrawResponse:
        """Transfers funds from the agent's wallet to the user's wallet.

        The operation
        includes: 1. Verification of user and agent existence 2. Validation of
        withdrawal amount against available balance 3. Transfer of funds on
        blockchain 4. Update of agent balance in database 5. Creation of transaction
        record

        Args:
          agentid: ID of the agent sending the funds

          amount: Amount to withdraw

          userid: ID of the user receiving the withdrawal

          currency: Currency type to withdraw (defaults to USDC)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/agents/withdraw",
            body=maybe_transform(
                {
                    "agentid": agentid,
                    "amount": amount,
                    "userid": userid,
                    "currency": currency,
                },
                agent_withdraw_params.AgentWithdrawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentWithdrawResponse,
        )


class AsyncAgentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return AsyncAgentsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        userid: str,
        balance: int | NotGiven = NOT_GIVEN,
        currency: str | NotGiven = NOT_GIVEN,
        dailylimit: int | NotGiven = NOT_GIVEN,
        description: str | NotGiven = NOT_GIVEN,
        requireapprovalaboveamount: int | NotGiven = NOT_GIVEN,
        requireapprovalforall: bool | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        transactionlimit: int | NotGiven = NOT_GIVEN,
        walletaddress: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentCreateResponse:
        """
        Creates a new agent, generates a wallet, and optionally funds the agent's wallet
        from the user's wallet. The operation includes: 1. Creation of a new agent
        record 2. Generation of a secure blockchain wallet 3. Faucet funding of the
        wallet (on supported test networks) 4. Optional transfer of funds from user's
        wallet

        Args:
          name: Name of the agent

          userid: ID of the user creating the agent

          balance: Initial balance to fund the agent (in smallest units)

          currency: Currency type to use (defaults to USDC)

          dailylimit: Maximum amount that can be spent per day

          description: Purpose and functionality of the agent

          requireapprovalaboveamount: Transactions above this amount require approval

          requireapprovalforall: Whether all transactions require approval

          tags: Categories or labels to assign to the agent

          transactionlimit: Maximum amount for a single transaction

          walletaddress: User's wallet address for funding (optional)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agents/create",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "userid": userid,
                    "balance": balance,
                    "currency": currency,
                    "dailylimit": dailylimit,
                    "description": description,
                    "requireapprovalaboveamount": requireapprovalaboveamount,
                    "requireapprovalforall": requireapprovalforall,
                    "tags": tags,
                    "transactionlimit": transactionlimit,
                    "walletaddress": walletaddress,
                },
                agent_create_params.AgentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentRetrieveResponse:
        """
        Returns an array of agents assigned to the user based on the provided user ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/agents/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentRetrieveResponse,
        )

    async def deposit(
        self,
        *,
        agentid: str,
        amount: float,
        userid: str,
        currency: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentDepositResponse:
        """Transfers funds from the user's wallet to the specified agent's wallet.

        The
        operation includes: 1. Verification of user and agent existence 2. Validation of
        deposit amount 3. Transfer of funds on blockchain 4. Update of agent balance in
        database 5. Creation of transaction record

        Args:
          agentid: ID of the agent receiving the deposit

          amount: Amount to deposit

          userid: ID of the user initiating the deposit

          currency: Currency type to deposit (defaults to USDC)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agents/deposit",
            body=await async_maybe_transform(
                {
                    "agentid": agentid,
                    "amount": amount,
                    "userid": userid,
                    "currency": currency,
                },
                agent_deposit_params.AgentDepositParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentDepositResponse,
        )

    async def withdraw(
        self,
        *,
        agentid: str,
        amount: float,
        userid: str,
        currency: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> AgentWithdrawResponse:
        """Transfers funds from the agent's wallet to the user's wallet.

        The operation
        includes: 1. Verification of user and agent existence 2. Validation of
        withdrawal amount against available balance 3. Transfer of funds on
        blockchain 4. Update of agent balance in database 5. Creation of transaction
        record

        Args:
          agentid: ID of the agent sending the funds

          amount: Amount to withdraw

          userid: ID of the user receiving the withdrawal

          currency: Currency type to withdraw (defaults to USDC)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/agents/withdraw",
            body=await async_maybe_transform(
                {
                    "agentid": agentid,
                    "amount": amount,
                    "userid": userid,
                    "currency": currency,
                },
                agent_withdraw_params.AgentWithdrawParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AgentWithdrawResponse,
        )


class AgentsResourceWithRawResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = to_raw_response_wrapper(
            agents.retrieve,
        )
        self.deposit = to_raw_response_wrapper(
            agents.deposit,
        )
        self.withdraw = to_raw_response_wrapper(
            agents.withdraw,
        )


class AsyncAgentsResourceWithRawResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_raw_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            agents.retrieve,
        )
        self.deposit = async_to_raw_response_wrapper(
            agents.deposit,
        )
        self.withdraw = async_to_raw_response_wrapper(
            agents.withdraw,
        )


class AgentsResourceWithStreamingResponse:
    def __init__(self, agents: AgentsResource) -> None:
        self._agents = agents

        self.create = to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.deposit = to_streamed_response_wrapper(
            agents.deposit,
        )
        self.withdraw = to_streamed_response_wrapper(
            agents.withdraw,
        )


class AsyncAgentsResourceWithStreamingResponse:
    def __init__(self, agents: AsyncAgentsResource) -> None:
        self._agents = agents

        self.create = async_to_streamed_response_wrapper(
            agents.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            agents.retrieve,
        )
        self.deposit = async_to_streamed_response_wrapper(
            agents.deposit,
        )
        self.withdraw = async_to_streamed_response_wrapper(
            agents.withdraw,
        )
