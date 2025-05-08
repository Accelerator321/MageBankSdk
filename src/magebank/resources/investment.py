# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import investment_calculate_interest_params
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
from ..types.investment_calculate_interest_response import InvestmentCalculateInterestResponse
from ..types.investment_retrieve_interest_rate_response import InvestmentRetrieveInterestRateResponse

__all__ = ["InvestmentResource", "AsyncInvestmentResource"]


class InvestmentResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvestmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return InvestmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvestmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return InvestmentResourceWithStreamingResponse(self)

    def calculate_interest(
        self,
        *,
        amount: float,
        days: float,
        custom_rate: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvestmentCalculateInterestResponse:
        """
        Calculates the potential interest earned for a given investment amount and
        period. Uses the platform's current interest rate by default, but allows
        specifying a custom rate for scenario planning. Returns detailed breakdown of
        the calculation with step-by-step formula application.

        Args:
          amount: Principal amount to invest

          days: Investment duration in days

          custom_rate: Optional custom interest rate (annual percentage)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/investment/calculator",
            body=maybe_transform(
                {
                    "amount": amount,
                    "days": days,
                    "custom_rate": custom_rate,
                },
                investment_calculate_interest_params.InvestmentCalculateInterestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentCalculateInterestResponse,
        )

    def retrieve_interest_rate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvestmentRetrieveInterestRateResponse:
        """
        Retrieves the current annual interest rate for investments and the timestamp
        when it was last updated. This rate is used for all savings calculations in the
        platform.
        """
        return self._get(
            "/investment/interest-rate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentRetrieveInterestRateResponse,
        )


class AsyncInvestmentResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvestmentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return AsyncInvestmentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvestmentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return AsyncInvestmentResourceWithStreamingResponse(self)

    async def calculate_interest(
        self,
        *,
        amount: float,
        days: float,
        custom_rate: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvestmentCalculateInterestResponse:
        """
        Calculates the potential interest earned for a given investment amount and
        period. Uses the platform's current interest rate by default, but allows
        specifying a custom rate for scenario planning. Returns detailed breakdown of
        the calculation with step-by-step formula application.

        Args:
          amount: Principal amount to invest

          days: Investment duration in days

          custom_rate: Optional custom interest rate (annual percentage)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/investment/calculator",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "days": days,
                    "custom_rate": custom_rate,
                },
                investment_calculate_interest_params.InvestmentCalculateInterestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentCalculateInterestResponse,
        )

    async def retrieve_interest_rate(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> InvestmentRetrieveInterestRateResponse:
        """
        Retrieves the current annual interest rate for investments and the timestamp
        when it was last updated. This rate is used for all savings calculations in the
        platform.
        """
        return await self._get(
            "/investment/interest-rate",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentRetrieveInterestRateResponse,
        )


class InvestmentResourceWithRawResponse:
    def __init__(self, investment: InvestmentResource) -> None:
        self._investment = investment

        self.calculate_interest = to_raw_response_wrapper(
            investment.calculate_interest,
        )
        self.retrieve_interest_rate = to_raw_response_wrapper(
            investment.retrieve_interest_rate,
        )


class AsyncInvestmentResourceWithRawResponse:
    def __init__(self, investment: AsyncInvestmentResource) -> None:
        self._investment = investment

        self.calculate_interest = async_to_raw_response_wrapper(
            investment.calculate_interest,
        )
        self.retrieve_interest_rate = async_to_raw_response_wrapper(
            investment.retrieve_interest_rate,
        )


class InvestmentResourceWithStreamingResponse:
    def __init__(self, investment: InvestmentResource) -> None:
        self._investment = investment

        self.calculate_interest = to_streamed_response_wrapper(
            investment.calculate_interest,
        )
        self.retrieve_interest_rate = to_streamed_response_wrapper(
            investment.retrieve_interest_rate,
        )


class AsyncInvestmentResourceWithStreamingResponse:
    def __init__(self, investment: AsyncInvestmentResource) -> None:
        self._investment = investment

        self.calculate_interest = async_to_streamed_response_wrapper(
            investment.calculate_interest,
        )
        self.retrieve_interest_rate = async_to_streamed_response_wrapper(
            investment.retrieve_interest_rate,
        )
