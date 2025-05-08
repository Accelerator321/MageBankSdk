# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import user_list_payments_params
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
from ..types.user_list_payments_response import UserListPaymentsResponse
from ..types.user_retrieve_wallet_balance_response import UserRetrieveWalletBalanceResponse

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    def list_payments(
        self,
        *,
        approval_status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListPaymentsResponse:
        """
        Retrieves a list of payments where either the sender or receiver is one of the
        authenticated user's agents. Payments are enhanced with additional
        information: 1. Agent names for both sender and receiver 2. Direction
        (incoming/outgoing) relative to the user's agents 3. Payment status and creation
        timestamp Results can be optionally filtered by approval status.

        Args:
          approval_status: Filter payments by approval status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/user/payments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"approval_status": approval_status}, user_list_payments_params.UserListPaymentsParams
                ),
            ),
            cast_to=UserListPaymentsResponse,
        )

    def retrieve_wallet_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieveWalletBalanceResponse:
        """
        Retrieves the user's wallet balance from the blockchain using their wallet
        address. The endpoint follows a fallback strategy, first attempting to fetch
        USDC balance, then ETH, and finally any other non-zero balance. Requires
        authentication with a valid API key.
        """
        return self._get(
            "/user/wallet-balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveWalletBalanceResponse,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    async def list_payments(
        self,
        *,
        approval_status: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserListPaymentsResponse:
        """
        Retrieves a list of payments where either the sender or receiver is one of the
        authenticated user's agents. Payments are enhanced with additional
        information: 1. Agent names for both sender and receiver 2. Direction
        (incoming/outgoing) relative to the user's agents 3. Payment status and creation
        timestamp Results can be optionally filtered by approval status.

        Args:
          approval_status: Filter payments by approval status

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/user/payments",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"approval_status": approval_status}, user_list_payments_params.UserListPaymentsParams
                ),
            ),
            cast_to=UserListPaymentsResponse,
        )

    async def retrieve_wallet_balance(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> UserRetrieveWalletBalanceResponse:
        """
        Retrieves the user's wallet balance from the blockchain using their wallet
        address. The endpoint follows a fallback strategy, first attempting to fetch
        USDC balance, then ETH, and finally any other non-zero balance. Requires
        authentication with a valid API key.
        """
        return await self._get(
            "/user/wallet-balance",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserRetrieveWalletBalanceResponse,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.list_payments = to_raw_response_wrapper(
            user.list_payments,
        )
        self.retrieve_wallet_balance = to_raw_response_wrapper(
            user.retrieve_wallet_balance,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.list_payments = async_to_raw_response_wrapper(
            user.list_payments,
        )
        self.retrieve_wallet_balance = async_to_raw_response_wrapper(
            user.retrieve_wallet_balance,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.list_payments = to_streamed_response_wrapper(
            user.list_payments,
        )
        self.retrieve_wallet_balance = to_streamed_response_wrapper(
            user.retrieve_wallet_balance,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.list_payments = async_to_streamed_response_wrapper(
            user.list_payments,
        )
        self.retrieve_wallet_balance = async_to_streamed_response_wrapper(
            user.retrieve_wallet_balance,
        )
