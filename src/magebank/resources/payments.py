# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from ..types import payment_approve_params, payment_decline_params, payment_register_params
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
from ..types.payment import Payment
from ..types.payment_approve_response import PaymentApproveResponse
from ..types.payment_decline_response import PaymentDeclineResponse
from ..types.payment_register_response import PaymentRegisterResponse

__all__ = ["PaymentsResource", "AsyncPaymentsResource"]


class PaymentsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/magebank-python#accessing-raw-response-data-eg-headers
        """
        return PaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/magebank-python#with_streaming_response
        """
        return PaymentsResourceWithStreamingResponse(self)

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
    ) -> Payment:
        """
        Retrieves detailed information about a specific payment based on its ID.
        Converts short ID format to UUID format internally before querying the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    def approve(
        self,
        *,
        payment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentApproveResponse:
        """
        Updates the approval status of a payment to "Approved" and sets the approval
        timestamp. This allows the payment to proceed to the next stage in the payment
        flow.

        Args:
          payment_id: The short ID of the payment to approve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payments/setApprove",
            body=maybe_transform({"payment_id": payment_id}, payment_approve_params.PaymentApproveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentApproveResponse,
        )

    def decline(
        self,
        *,
        payment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentDeclineResponse:
        """
        Updates the approval status of a payment to "Decline" and sets its status to
        "Confirmed". This effectively rejects the payment and prevents it from being
        processed. The operation also records the timestamp when the payment was
        declined.

        Args:
          payment_id: The short ID of the payment to decline

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payments/setDecline",
            body=maybe_transform({"payment_id": payment_id}, payment_decline_params.PaymentDeclineParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentDeclineResponse,
        )

    def register(
        self,
        *,
        name: str,
        paymentdetails: payment_register_params.Paymentdetails,
        receiveragentid: str,
        senderagentid: str,
        contactdetails: payment_register_params.Contactdetails | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: Literal["EXTERNAL", "INTERNAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRegisterResponse:
        """Creates a new payment record between a sender agent and a receiver agent.

        The
        operation automatically determines if approval is required based on: 1. The
        sender agent's approval configuration (requireapprovalforall) 2. Whether the
        payment amount exceeds the approval threshold (requireapprovalaboveamount) All
        payments start with an approval status of "Waiting".

        Args:
          name: Name or description of the payment

          receiveragentid: ID of the agent receiving the payment (short ID or UUID)

          senderagentid: ID of the agent sending the payment (short ID or UUID)

          tags: Tags or categories for the payment

          type: Type of payment (EXTERNAL or INTERNAL)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payments/register",
            body=maybe_transform(
                {
                    "name": name,
                    "paymentdetails": paymentdetails,
                    "receiveragentid": receiveragentid,
                    "senderagentid": senderagentid,
                    "contactdetails": contactdetails,
                    "tags": tags,
                    "type": type,
                },
                payment_register_params.PaymentRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRegisterResponse,
        )


class AsyncPaymentsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPaymentsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/magebank-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPaymentsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPaymentsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/magebank-python#with_streaming_response
        """
        return AsyncPaymentsResourceWithStreamingResponse(self)

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
    ) -> Payment:
        """
        Retrieves detailed information about a specific payment based on its ID.
        Converts short ID format to UUID format internally before querying the database.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/payments/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Payment,
        )

    async def approve(
        self,
        *,
        payment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentApproveResponse:
        """
        Updates the approval status of a payment to "Approved" and sets the approval
        timestamp. This allows the payment to proceed to the next stage in the payment
        flow.

        Args:
          payment_id: The short ID of the payment to approve

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payments/setApprove",
            body=await async_maybe_transform({"payment_id": payment_id}, payment_approve_params.PaymentApproveParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentApproveResponse,
        )

    async def decline(
        self,
        *,
        payment_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentDeclineResponse:
        """
        Updates the approval status of a payment to "Decline" and sets its status to
        "Confirmed". This effectively rejects the payment and prevents it from being
        processed. The operation also records the timestamp when the payment was
        declined.

        Args:
          payment_id: The short ID of the payment to decline

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payments/setDecline",
            body=await async_maybe_transform({"payment_id": payment_id}, payment_decline_params.PaymentDeclineParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentDeclineResponse,
        )

    async def register(
        self,
        *,
        name: str,
        paymentdetails: payment_register_params.Paymentdetails,
        receiveragentid: str,
        senderagentid: str,
        contactdetails: payment_register_params.Contactdetails | NotGiven = NOT_GIVEN,
        tags: List[str] | NotGiven = NOT_GIVEN,
        type: Literal["EXTERNAL", "INTERNAL"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PaymentRegisterResponse:
        """Creates a new payment record between a sender agent and a receiver agent.

        The
        operation automatically determines if approval is required based on: 1. The
        sender agent's approval configuration (requireapprovalforall) 2. Whether the
        payment amount exceeds the approval threshold (requireapprovalaboveamount) All
        payments start with an approval status of "Waiting".

        Args:
          name: Name or description of the payment

          receiveragentid: ID of the agent receiving the payment (short ID or UUID)

          senderagentid: ID of the agent sending the payment (short ID or UUID)

          tags: Tags or categories for the payment

          type: Type of payment (EXTERNAL or INTERNAL)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payments/register",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "paymentdetails": paymentdetails,
                    "receiveragentid": receiveragentid,
                    "senderagentid": senderagentid,
                    "contactdetails": contactdetails,
                    "tags": tags,
                    "type": type,
                },
                payment_register_params.PaymentRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PaymentRegisterResponse,
        )


class PaymentsResourceWithRawResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.retrieve = to_raw_response_wrapper(
            payments.retrieve,
        )
        self.approve = to_raw_response_wrapper(
            payments.approve,
        )
        self.decline = to_raw_response_wrapper(
            payments.decline,
        )
        self.register = to_raw_response_wrapper(
            payments.register,
        )


class AsyncPaymentsResourceWithRawResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.retrieve = async_to_raw_response_wrapper(
            payments.retrieve,
        )
        self.approve = async_to_raw_response_wrapper(
            payments.approve,
        )
        self.decline = async_to_raw_response_wrapper(
            payments.decline,
        )
        self.register = async_to_raw_response_wrapper(
            payments.register,
        )


class PaymentsResourceWithStreamingResponse:
    def __init__(self, payments: PaymentsResource) -> None:
        self._payments = payments

        self.retrieve = to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.approve = to_streamed_response_wrapper(
            payments.approve,
        )
        self.decline = to_streamed_response_wrapper(
            payments.decline,
        )
        self.register = to_streamed_response_wrapper(
            payments.register,
        )


class AsyncPaymentsResourceWithStreamingResponse:
    def __init__(self, payments: AsyncPaymentsResource) -> None:
        self._payments = payments

        self.retrieve = async_to_streamed_response_wrapper(
            payments.retrieve,
        )
        self.approve = async_to_streamed_response_wrapper(
            payments.approve,
        )
        self.decline = async_to_streamed_response_wrapper(
            payments.decline,
        )
        self.register = async_to_streamed_response_wrapper(
            payments.register,
        )
