# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import saving_create_deposit_params, saving_create_withdrawal_params
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
from ..types.saving_create_deposit_response import SavingCreateDepositResponse
from ..types.saving_list_investments_response import SavingListInvestmentsResponse
from ..types.saving_create_withdrawal_response import SavingCreateWithdrawalResponse
from ..types.saving_retrieve_dashboard_response import SavingRetrieveDashboardResponse
from ..types.saving_list_investments_by_agent_response import SavingListInvestmentsByAgentResponse

__all__ = ["SavingsResource", "AsyncSavingsResource"]


class SavingsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SavingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return SavingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SavingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return SavingsResourceWithStreamingResponse(self)

    def create_deposit(
        self,
        *,
        agent_id: str,
        amount: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SavingCreateDepositResponse:
        """
        Creates a new investment by depositing funds into an agent's savings account.
        The operation converts the agent ID to UUID format if provided in short format,
        validates the deposit amount, and creates a new investment record.

        Args:
          agent_id: The short ID or UUID of the agent

          amount: Amount to deposit (must be positive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/savings/deposit",
            body=maybe_transform(
                {
                    "agent_id": agent_id,
                    "amount": amount,
                },
                saving_create_deposit_params.SavingCreateDepositParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavingCreateDepositResponse,
        )

    def create_withdrawal(
        self,
        *,
        investment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SavingCreateWithdrawalResponse:
        """Closes an active investment and returns funds to the user's account.

        The
        operation validates the investment ID, converts it to UUID format if needed, and
        processes the withdrawal by updating the investment status.

        Args:
          investment_id: The short ID or UUID of the investment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/savings/withdraw",
            body=maybe_transform(
                {"investment_id": investment_id}, saving_create_withdrawal_params.SavingCreateWithdrawalParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavingCreateWithdrawalResponse,
        )

    def list_investments(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SavingListInvestmentsResponse:
        """Retrieves a list of all active investments made by the authenticated user.

        The
        response includes details about agents associated with investments, the invested
        amount, current value (with interest), and investment duration. Interest
        calculations are based on the central wallet's current interest rate.
        """
        return self._get(
            "/savings/myinvestments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavingListInvestmentsResponse,
        )

    def list_investments_by_agent(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SavingListInvestmentsByAgentResponse:
        """
        Retrieves all investments (both active and completed) associated with a specific
        agent. For active investments, calculates the current value and interest earned
        based on the principal amount, interest rate, and investment duration. Returns
        detailed information including investment status and creation timestamp.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return self._get(
            f"/savings/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavingListInvestmentsByAgentResponse,
        )

    def retrieve_dashboard(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SavingRetrieveDashboardResponse:
        """Provides a comprehensive overview of the user's savings portfolio.

        Includes
        total savings, current interest rate, total invested amount, one-year
        projection, and detailed information about investments by agent. Calculates
        real-time investment values based on the current interest rate and the exact
        duration of each investment.
        """
        return self._get(
            "/savings/dashboard",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavingRetrieveDashboardResponse,
        )


class AsyncSavingsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSavingsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return AsyncSavingsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSavingsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return AsyncSavingsResourceWithStreamingResponse(self)

    async def create_deposit(
        self,
        *,
        agent_id: str,
        amount: float,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SavingCreateDepositResponse:
        """
        Creates a new investment by depositing funds into an agent's savings account.
        The operation converts the agent ID to UUID format if provided in short format,
        validates the deposit amount, and creates a new investment record.

        Args:
          agent_id: The short ID or UUID of the agent

          amount: Amount to deposit (must be positive)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/savings/deposit",
            body=await async_maybe_transform(
                {
                    "agent_id": agent_id,
                    "amount": amount,
                },
                saving_create_deposit_params.SavingCreateDepositParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavingCreateDepositResponse,
        )

    async def create_withdrawal(
        self,
        *,
        investment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SavingCreateWithdrawalResponse:
        """Closes an active investment and returns funds to the user's account.

        The
        operation validates the investment ID, converts it to UUID format if needed, and
        processes the withdrawal by updating the investment status.

        Args:
          investment_id: The short ID or UUID of the investment

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/savings/withdraw",
            body=await async_maybe_transform(
                {"investment_id": investment_id}, saving_create_withdrawal_params.SavingCreateWithdrawalParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavingCreateWithdrawalResponse,
        )

    async def list_investments(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SavingListInvestmentsResponse:
        """Retrieves a list of all active investments made by the authenticated user.

        The
        response includes details about agents associated with investments, the invested
        amount, current value (with interest), and investment duration. Interest
        calculations are based on the central wallet's current interest rate.
        """
        return await self._get(
            "/savings/myinvestments",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavingListInvestmentsResponse,
        )

    async def list_investments_by_agent(
        self,
        agent_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SavingListInvestmentsByAgentResponse:
        """
        Retrieves all investments (both active and completed) associated with a specific
        agent. For active investments, calculates the current value and interest earned
        based on the principal amount, interest rate, and investment duration. Returns
        detailed information including investment status and creation timestamp.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not agent_id:
            raise ValueError(f"Expected a non-empty value for `agent_id` but received {agent_id!r}")
        return await self._get(
            f"/savings/{agent_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavingListInvestmentsByAgentResponse,
        )

    async def retrieve_dashboard(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> SavingRetrieveDashboardResponse:
        """Provides a comprehensive overview of the user's savings portfolio.

        Includes
        total savings, current interest rate, total invested amount, one-year
        projection, and detailed information about investments by agent. Calculates
        real-time investment values based on the current interest rate and the exact
        duration of each investment.
        """
        return await self._get(
            "/savings/dashboard",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavingRetrieveDashboardResponse,
        )


class SavingsResourceWithRawResponse:
    def __init__(self, savings: SavingsResource) -> None:
        self._savings = savings

        self.create_deposit = to_raw_response_wrapper(
            savings.create_deposit,
        )
        self.create_withdrawal = to_raw_response_wrapper(
            savings.create_withdrawal,
        )
        self.list_investments = to_raw_response_wrapper(
            savings.list_investments,
        )
        self.list_investments_by_agent = to_raw_response_wrapper(
            savings.list_investments_by_agent,
        )
        self.retrieve_dashboard = to_raw_response_wrapper(
            savings.retrieve_dashboard,
        )


class AsyncSavingsResourceWithRawResponse:
    def __init__(self, savings: AsyncSavingsResource) -> None:
        self._savings = savings

        self.create_deposit = async_to_raw_response_wrapper(
            savings.create_deposit,
        )
        self.create_withdrawal = async_to_raw_response_wrapper(
            savings.create_withdrawal,
        )
        self.list_investments = async_to_raw_response_wrapper(
            savings.list_investments,
        )
        self.list_investments_by_agent = async_to_raw_response_wrapper(
            savings.list_investments_by_agent,
        )
        self.retrieve_dashboard = async_to_raw_response_wrapper(
            savings.retrieve_dashboard,
        )


class SavingsResourceWithStreamingResponse:
    def __init__(self, savings: SavingsResource) -> None:
        self._savings = savings

        self.create_deposit = to_streamed_response_wrapper(
            savings.create_deposit,
        )
        self.create_withdrawal = to_streamed_response_wrapper(
            savings.create_withdrawal,
        )
        self.list_investments = to_streamed_response_wrapper(
            savings.list_investments,
        )
        self.list_investments_by_agent = to_streamed_response_wrapper(
            savings.list_investments_by_agent,
        )
        self.retrieve_dashboard = to_streamed_response_wrapper(
            savings.retrieve_dashboard,
        )


class AsyncSavingsResourceWithStreamingResponse:
    def __init__(self, savings: AsyncSavingsResource) -> None:
        self._savings = savings

        self.create_deposit = async_to_streamed_response_wrapper(
            savings.create_deposit,
        )
        self.create_withdrawal = async_to_streamed_response_wrapper(
            savings.create_withdrawal,
        )
        self.list_investments = async_to_streamed_response_wrapper(
            savings.list_investments,
        )
        self.list_investments_by_agent = async_to_streamed_response_wrapper(
            savings.list_investments_by_agent,
        )
        self.retrieve_dashboard = async_to_streamed_response_wrapper(
            savings.retrieve_dashboard,
        )
