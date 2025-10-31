from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.document import Document
from ...models.http_validation_error import HTTPValidationError
from ...models.index_request import IndexRequest
from ...types import Response


def _get_kwargs(
    *,
    body: IndexRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/index",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, list["Document"]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Document.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[HTTPValidationError, list["Document"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IndexRequest,
) -> Response[Union[HTTPValidationError, list["Document"]]]:
    r"""Index Documents

     Add documents to an index or create a new index.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"documents\": [
            {\"text\": \"Sample document text.\", \"metadata\": {\"author\": \"John Doe\", \"category\":
    \"example\"}}
          ]
        }
        ```

        ## Response Example:
        ```json
        [
          {
            \"doc_id\": \"123456\",
            \"text\": \"Sample document text.\",
            \"hash_value\": null,
            \"metadata\": {\"author\": \"John Doe\", \"category\": \"example\"},
            \"is_truncated\": false
          }
        ]
        ```

    Args:
        body (IndexRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['Document']]]
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
    body: IndexRequest,
) -> Optional[Union[HTTPValidationError, list["Document"]]]:
    r"""Index Documents

     Add documents to an index or create a new index.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"documents\": [
            {\"text\": \"Sample document text.\", \"metadata\": {\"author\": \"John Doe\", \"category\":
    \"example\"}}
          ]
        }
        ```

        ## Response Example:
        ```json
        [
          {
            \"doc_id\": \"123456\",
            \"text\": \"Sample document text.\",
            \"hash_value\": null,
            \"metadata\": {\"author\": \"John Doe\", \"category\": \"example\"},
            \"is_truncated\": false
          }
        ]
        ```

    Args:
        body (IndexRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['Document']]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IndexRequest,
) -> Response[Union[HTTPValidationError, list["Document"]]]:
    r"""Index Documents

     Add documents to an index or create a new index.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"documents\": [
            {\"text\": \"Sample document text.\", \"metadata\": {\"author\": \"John Doe\", \"category\":
    \"example\"}}
          ]
        }
        ```

        ## Response Example:
        ```json
        [
          {
            \"doc_id\": \"123456\",
            \"text\": \"Sample document text.\",
            \"hash_value\": null,
            \"metadata\": {\"author\": \"John Doe\", \"category\": \"example\"},
            \"is_truncated\": false
          }
        ]
        ```

    Args:
        body (IndexRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, list['Document']]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Union[AuthenticatedClient, Client],
    body: IndexRequest,
) -> Optional[Union[HTTPValidationError, list["Document"]]]:
    r"""Index Documents

     Add documents to an index or create a new index.

        ## Request Example:
        ```json
        {
          \"index_name\": \"example_index\",
          \"documents\": [
            {\"text\": \"Sample document text.\", \"metadata\": {\"author\": \"John Doe\", \"category\":
    \"example\"}}
          ]
        }
        ```

        ## Response Example:
        ```json
        [
          {
            \"doc_id\": \"123456\",
            \"text\": \"Sample document text.\",
            \"hash_value\": null,
            \"metadata\": {\"author\": \"John Doe\", \"category\": \"example\"},
            \"is_truncated\": false
          }
        ]
        ```

    Args:
        body (IndexRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, list['Document']]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
