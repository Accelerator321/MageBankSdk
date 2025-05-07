# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.agent import Agent
from .._base_client import make_request_options

__all__ = ["AgentsWithResource", "AsyncAgentsWithResource"]


class AgentsWithResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AgentsWithResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return AgentsWithResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AgentsWithResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return AgentsWithResourceWithStreamingResponse(self)

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
    ) -> Agent:
        """
        Returns detailed information about a specific agent based on the provided agent
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/agentsWith/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )


class AsyncAgentsWithResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAgentsWithResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAgentsWithResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAgentsWithResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/Accelerator321/MageBankSdk#with_streaming_response
        """
        return AsyncAgentsWithResourceWithStreamingResponse(self)

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
    ) -> Agent:
        """
        Returns detailed information about a specific agent based on the provided agent
        ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/agentsWith/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Agent,
        )


class AgentsWithResourceWithRawResponse:
    def __init__(self, agents_with: AgentsWithResource) -> None:
        self._agents_with = agents_with

        self.retrieve = to_raw_response_wrapper(
            agents_with.retrieve,
        )


class AsyncAgentsWithResourceWithRawResponse:
    def __init__(self, agents_with: AsyncAgentsWithResource) -> None:
        self._agents_with = agents_with

        self.retrieve = async_to_raw_response_wrapper(
            agents_with.retrieve,
        )


class AgentsWithResourceWithStreamingResponse:
    def __init__(self, agents_with: AgentsWithResource) -> None:
        self._agents_with = agents_with

        self.retrieve = to_streamed_response_wrapper(
            agents_with.retrieve,
        )


class AsyncAgentsWithResourceWithStreamingResponse:
    def __init__(self, agents_with: AsyncAgentsWithResource) -> None:
        self._agents_with = agents_with

        self.retrieve = async_to_streamed_response_wrapper(
            agents_with.retrieve,
        )
