from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.chat_completion_response import ChatCompletionResponse
from ...models.chat_request import ChatRequest
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    body: ChatRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/v1/chat/completions",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[ChatCompletionResponse, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = ChatCompletionResponse.from_dict(response.json())

        return response_200

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[ChatCompletionResponse, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChatRequest,
) -> Response[Union[ChatCompletionResponse, HTTPValidationError]]:
    r"""OpenAI-Compatible Chat Completions API

     OpenAI-compatible chat completions endpoint with RAG capabilities.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"model\": \"example_model\",
          \"messages\": [
            {\"role\": \"system\", \"content\": \"You are a knowledgeable assistant.\"},
            {\"role\": \"user\", \"content\": \"What is RAG?\"}
          ],
          \"temperature\": 0.7,
          \"max_tokens\": 2048,
          \"context_token_ratio\": 0.5
        }
        ```

        ## Response Example:
        ```json
        {
          \"id\": \"chatcmpl-123\",
          \"object\": \"chat.completion\",
          \"created\": 1677652288,
          \"model\": \"example_model\",
          \"choices\": [
            {
              \"index\": 0,
              \"message\": {
                \"role\": \"assistant\",
                \"content\": \"RAG stands for Retrieval-Augmented Generation...\"
              },
              \"finish_reason\": \"stop\"
            }
          ],
          \"usage\": {
            \"prompt_tokens\": 56,
            \"completion_tokens\": 31,
            \"total_tokens\": 87
          },
          \"source_nodes\": [...]
        }
        ```

    Args:
        body (ChatRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChatCompletionResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChatRequest,
) -> Optional[Union[ChatCompletionResponse, HTTPValidationError]]:
    r"""OpenAI-Compatible Chat Completions API

     OpenAI-compatible chat completions endpoint with RAG capabilities.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"model\": \"example_model\",
          \"messages\": [
            {\"role\": \"system\", \"content\": \"You are a knowledgeable assistant.\"},
            {\"role\": \"user\", \"content\": \"What is RAG?\"}
          ],
          \"temperature\": 0.7,
          \"max_tokens\": 2048,
          \"context_token_ratio\": 0.5
        }
        ```

        ## Response Example:
        ```json
        {
          \"id\": \"chatcmpl-123\",
          \"object\": \"chat.completion\",
          \"created\": 1677652288,
          \"model\": \"example_model\",
          \"choices\": [
            {
              \"index\": 0,
              \"message\": {
                \"role\": \"assistant\",
                \"content\": \"RAG stands for Retrieval-Augmented Generation...\"
              },
              \"finish_reason\": \"stop\"
            }
          ],
          \"usage\": {
            \"prompt_tokens\": 56,
            \"completion_tokens\": 31,
            \"total_tokens\": 87
          },
          \"source_nodes\": [...]
        }
        ```

    Args:
        body (ChatRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChatCompletionResponse, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChatRequest,
) -> Response[Union[ChatCompletionResponse, HTTPValidationError]]:
    r"""OpenAI-Compatible Chat Completions API

     OpenAI-compatible chat completions endpoint with RAG capabilities.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"model\": \"example_model\",
          \"messages\": [
            {\"role\": \"system\", \"content\": \"You are a knowledgeable assistant.\"},
            {\"role\": \"user\", \"content\": \"What is RAG?\"}
          ],
          \"temperature\": 0.7,
          \"max_tokens\": 2048,
          \"context_token_ratio\": 0.5
        }
        ```

        ## Response Example:
        ```json
        {
          \"id\": \"chatcmpl-123\",
          \"object\": \"chat.completion\",
          \"created\": 1677652288,
          \"model\": \"example_model\",
          \"choices\": [
            {
              \"index\": 0,
              \"message\": {
                \"role\": \"assistant\",
                \"content\": \"RAG stands for Retrieval-Augmented Generation...\"
              },
              \"finish_reason\": \"stop\"
            }
          ],
          \"usage\": {
            \"prompt_tokens\": 56,
            \"completion_tokens\": 31,
            \"total_tokens\": 87
          },
          \"source_nodes\": [...]
        }
        ```

    Args:
        body (ChatRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[ChatCompletionResponse, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: ChatRequest,
) -> Optional[Union[ChatCompletionResponse, HTTPValidationError]]:
    r"""OpenAI-Compatible Chat Completions API

     OpenAI-compatible chat completions endpoint with RAG capabilities.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"model\": \"example_model\",
          \"messages\": [
            {\"role\": \"system\", \"content\": \"You are a knowledgeable assistant.\"},
            {\"role\": \"user\", \"content\": \"What is RAG?\"}
          ],
          \"temperature\": 0.7,
          \"max_tokens\": 2048,
          \"context_token_ratio\": 0.5
        }
        ```

        ## Response Example:
        ```json
        {
          \"id\": \"chatcmpl-123\",
          \"object\": \"chat.completion\",
          \"created\": 1677652288,
          \"model\": \"example_model\",
          \"choices\": [
            {
              \"index\": 0,
              \"message\": {
                \"role\": \"assistant\",
                \"content\": \"RAG stands for Retrieval-Augmented Generation...\"
              },
              \"finish_reason\": \"stop\"
            }
          ],
          \"usage\": {
            \"prompt_tokens\": 56,
            \"completion_tokens\": 31,
            \"total_tokens\": 87
          },
          \"source_nodes\": [...]
        }
        ```

    Args:
        body (ChatRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[ChatCompletionResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
