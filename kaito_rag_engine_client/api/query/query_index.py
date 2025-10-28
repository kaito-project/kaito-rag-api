from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.query_request import QueryRequest
from ...models.query_response import QueryResponse
from ...types import Response


def _get_kwargs(
    *,
    body: QueryRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/query",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, QueryResponse]]:
    if response.status_code == 200:
        response_200 = QueryResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, QueryResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QueryRequest,
) -> Response[Union[HTTPValidationError, QueryResponse]]:
    r"""Query an Index

     Query a specific index for documents and optionally rerank with an LLM.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"query\": \"What is RAG?\",
          \"llm_params\": {\"temperature\": 0.7, \"max_tokens\": 2048},
          \"rerank_params\": {\"top_n\": 3}  # ⚠️ Experimental Feature
        }
        ```

        ## Experimental Warning:
        - The `rerank_params` option is **experimental** and may cause the query to fail.
        - If `LLMRerank` produces an invalid or unparsable response, an **error will be raised**.
        - Expected format:
          ```
          Answer:
          Doc: 9, Relevance: 7
          Doc: 3, Relevance: 4
          Doc: 7, Relevance: 3
          ```
        - If reranking fails, the request will not return results and will instead raise an error.

        ## Response Example:
        ```json
        {
          \"response\": \"...\",
          \"source_nodes\": [{\"doc_id\": \"doc1\", \"node_id\": \"node1\", \"text\": \"RAG
    explanation...\", \"score\": 0.95, \"metadata\": {}}],
          \"metadata\": {}
        }
        ```

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, QueryResponse]]
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
    body: QueryRequest,
) -> Optional[Union[HTTPValidationError, QueryResponse]]:
    r"""Query an Index

     Query a specific index for documents and optionally rerank with an LLM.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"query\": \"What is RAG?\",
          \"llm_params\": {\"temperature\": 0.7, \"max_tokens\": 2048},
          \"rerank_params\": {\"top_n\": 3}  # ⚠️ Experimental Feature
        }
        ```

        ## Experimental Warning:
        - The `rerank_params` option is **experimental** and may cause the query to fail.
        - If `LLMRerank` produces an invalid or unparsable response, an **error will be raised**.
        - Expected format:
          ```
          Answer:
          Doc: 9, Relevance: 7
          Doc: 3, Relevance: 4
          Doc: 7, Relevance: 3
          ```
        - If reranking fails, the request will not return results and will instead raise an error.

        ## Response Example:
        ```json
        {
          \"response\": \"...\",
          \"source_nodes\": [{\"doc_id\": \"doc1\", \"node_id\": \"node1\", \"text\": \"RAG
    explanation...\", \"score\": 0.95, \"metadata\": {}}],
          \"metadata\": {}
        }
        ```

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, QueryResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QueryRequest,
) -> Response[Union[HTTPValidationError, QueryResponse]]:
    r"""Query an Index

     Query a specific index for documents and optionally rerank with an LLM.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"query\": \"What is RAG?\",
          \"llm_params\": {\"temperature\": 0.7, \"max_tokens\": 2048},
          \"rerank_params\": {\"top_n\": 3}  # ⚠️ Experimental Feature
        }
        ```

        ## Experimental Warning:
        - The `rerank_params` option is **experimental** and may cause the query to fail.
        - If `LLMRerank` produces an invalid or unparsable response, an **error will be raised**.
        - Expected format:
          ```
          Answer:
          Doc: 9, Relevance: 7
          Doc: 3, Relevance: 4
          Doc: 7, Relevance: 3
          ```
        - If reranking fails, the request will not return results and will instead raise an error.

        ## Response Example:
        ```json
        {
          \"response\": \"...\",
          \"source_nodes\": [{\"doc_id\": \"doc1\", \"node_id\": \"node1\", \"text\": \"RAG
    explanation...\", \"score\": 0.95, \"metadata\": {}}],
          \"metadata\": {}
        }
        ```

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, QueryResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: QueryRequest,
) -> Optional[Union[HTTPValidationError, QueryResponse]]:
    r"""Query an Index

     Query a specific index for documents and optionally rerank with an LLM.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"query\": \"What is RAG?\",
          \"llm_params\": {\"temperature\": 0.7, \"max_tokens\": 2048},
          \"rerank_params\": {\"top_n\": 3}  # ⚠️ Experimental Feature
        }
        ```

        ## Experimental Warning:
        - The `rerank_params` option is **experimental** and may cause the query to fail.
        - If `LLMRerank` produces an invalid or unparsable response, an **error will be raised**.
        - Expected format:
          ```
          Answer:
          Doc: 9, Relevance: 7
          Doc: 3, Relevance: 4
          Doc: 7, Relevance: 3
          ```
        - If reranking fails, the request will not return results and will instead raise an error.

        ## Response Example:
        ```json
        {
          \"response\": \"...\",
          \"source_nodes\": [{\"doc_id\": \"doc1\", \"node_id\": \"node1\", \"text\": \"RAG
    explanation...\", \"score\": 0.95, \"metadata\": {}}],
          \"metadata\": {}
        }
        ```

    Args:
        body (QueryRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, QueryResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
