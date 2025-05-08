# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import transaction_retrieve_summary_params
from .._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
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

__all__ = ["TransactionsResource", "AsyncTransactionsResource"]


class TransactionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return TransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return TransactionsResourceWithStreamingResponse(self)

    def retrieve_summary(
        self,
        *,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Provides a summary of financial activity within the specified date range,
        including total amounts earned (deposits, interest) and spent (withdrawals,
        payments).

        Args:
          end_date: End date for summary calculation (ISO format)

          start_date: Start date for summary calculation (ISO format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            "/transactions/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    transaction_retrieve_summary_params.TransactionRetrieveSummaryParams,
                ),
            ),
            cast_to=NoneType,
        )


class AsyncTransactionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTransactionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return AsyncTransactionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTransactionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return AsyncTransactionsResourceWithStreamingResponse(self)

    async def retrieve_summary(
        self,
        *,
        end_date: Union[str, datetime],
        start_date: Union[str, datetime],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> None:
        """
        Provides a summary of financial activity within the specified date range,
        including total amounts earned (deposits, interest) and spent (withdrawals,
        payments).

        Args:
          end_date: End date for summary calculation (ISO format)

          start_date: Start date for summary calculation (ISO format)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            "/transactions/summary",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    transaction_retrieve_summary_params.TransactionRetrieveSummaryParams,
                ),
            ),
            cast_to=NoneType,
        )


class TransactionsResourceWithRawResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.retrieve_summary = to_raw_response_wrapper(
            transactions.retrieve_summary,
        )


class AsyncTransactionsResourceWithRawResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.retrieve_summary = async_to_raw_response_wrapper(
            transactions.retrieve_summary,
        )


class TransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: TransactionsResource) -> None:
        self._transactions = transactions

        self.retrieve_summary = to_streamed_response_wrapper(
            transactions.retrieve_summary,
        )


class AsyncTransactionsResourceWithStreamingResponse:
    def __init__(self, transactions: AsyncTransactionsResource) -> None:
        self._transactions = transactions

        self.retrieve_summary = async_to_streamed_response_wrapper(
            transactions.retrieve_summary,
        )
