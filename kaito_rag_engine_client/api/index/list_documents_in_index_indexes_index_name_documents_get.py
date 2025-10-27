from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_documents_response import ListDocumentsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    index_name: str,
    *,
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 0,
    max_text_length: Union[None, Unset, int] = 1000,
    metadata_filter: Union[None, Unset, str] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_max_text_length: Union[None, Unset, int]
    if isinstance(max_text_length, Unset):
        json_max_text_length = UNSET
    else:
        json_max_text_length = max_text_length
    params["max_text_length"] = json_max_text_length

    json_metadata_filter: Union[None, Unset, str]
    if isinstance(metadata_filter, Unset):
        json_metadata_filter = UNSET
    else:
        json_metadata_filter = metadata_filter
    params["metadata_filter"] = json_metadata_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/indexes/{index_name}/documents",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, ListDocumentsResponse]]:
    if response.status_code == 200:
        response_200 = ListDocumentsResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, ListDocumentsResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    index_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 0,
    max_text_length: Union[None, Unset, int] = 1000,
    metadata_filter: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ListDocumentsResponse]]:
    r"""List Documents in an Index

     Retrieve a paginated list of documents for a given index.

        ## Request Example:
        ```
        GET /indexes/test_index/documents?limit=5&offset=5&max_text_length=500
        ```

        ## Response Example:
        ```json
        {
          \"documents\": [
            {
              \"doc_id\": \"123456\",
              \"text\": \"Sample document text.\",
              \"metadata\": {\"author\": \"John Doe\"},
              \"is_truncated\": true
            },
            {
              \"doc_id\": \"123457\",
              \"text\": \"Another document text.\",
              \"metadata\": {\"author\": \"Jane Doe\"},
              \"is_truncated\": false
            }
          ],
          \"count\": 5
        }
        ```

    Args:
        index_name (str):
        limit (Union[Unset, int]): Maximum number of documents to return Default: 10.
        offset (Union[Unset, int]): Starting point for the document list Default: 0.
        max_text_length (Union[None, Unset, int]): Maximum text length to return **per document**.
            This does not impose a limit on the total length of all documents returned. Default: 1000.
        metadata_filter (Union[None, Unset, str]): Optional metadata filter to apply when listing
            documents. This should be a dictionary with key-value pairs to match against document
            metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ListDocumentsResponse]]
    """

    kwargs = _get_kwargs(
        index_name=index_name,
        limit=limit,
        offset=offset,
        max_text_length=max_text_length,
        metadata_filter=metadata_filter,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    index_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 0,
    max_text_length: Union[None, Unset, int] = 1000,
    metadata_filter: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ListDocumentsResponse]]:
    r"""List Documents in an Index

     Retrieve a paginated list of documents for a given index.

        ## Request Example:
        ```
        GET /indexes/test_index/documents?limit=5&offset=5&max_text_length=500
        ```

        ## Response Example:
        ```json
        {
          \"documents\": [
            {
              \"doc_id\": \"123456\",
              \"text\": \"Sample document text.\",
              \"metadata\": {\"author\": \"John Doe\"},
              \"is_truncated\": true
            },
            {
              \"doc_id\": \"123457\",
              \"text\": \"Another document text.\",
              \"metadata\": {\"author\": \"Jane Doe\"},
              \"is_truncated\": false
            }
          ],
          \"count\": 5
        }
        ```

    Args:
        index_name (str):
        limit (Union[Unset, int]): Maximum number of documents to return Default: 10.
        offset (Union[Unset, int]): Starting point for the document list Default: 0.
        max_text_length (Union[None, Unset, int]): Maximum text length to return **per document**.
            This does not impose a limit on the total length of all documents returned. Default: 1000.
        metadata_filter (Union[None, Unset, str]): Optional metadata filter to apply when listing
            documents. This should be a dictionary with key-value pairs to match against document
            metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ListDocumentsResponse]
    """

    return sync_detailed(
        index_name=index_name,
        client=client,
        limit=limit,
        offset=offset,
        max_text_length=max_text_length,
        metadata_filter=metadata_filter,
    ).parsed


async def asyncio_detailed(
    index_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 0,
    max_text_length: Union[None, Unset, int] = 1000,
    metadata_filter: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, ListDocumentsResponse]]:
    r"""List Documents in an Index

     Retrieve a paginated list of documents for a given index.

        ## Request Example:
        ```
        GET /indexes/test_index/documents?limit=5&offset=5&max_text_length=500
        ```

        ## Response Example:
        ```json
        {
          \"documents\": [
            {
              \"doc_id\": \"123456\",
              \"text\": \"Sample document text.\",
              \"metadata\": {\"author\": \"John Doe\"},
              \"is_truncated\": true
            },
            {
              \"doc_id\": \"123457\",
              \"text\": \"Another document text.\",
              \"metadata\": {\"author\": \"Jane Doe\"},
              \"is_truncated\": false
            }
          ],
          \"count\": 5
        }
        ```

    Args:
        index_name (str):
        limit (Union[Unset, int]): Maximum number of documents to return Default: 10.
        offset (Union[Unset, int]): Starting point for the document list Default: 0.
        max_text_length (Union[None, Unset, int]): Maximum text length to return **per document**.
            This does not impose a limit on the total length of all documents returned. Default: 1000.
        metadata_filter (Union[None, Unset, str]): Optional metadata filter to apply when listing
            documents. This should be a dictionary with key-value pairs to match against document
            metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, ListDocumentsResponse]]
    """

    kwargs = _get_kwargs(
        index_name=index_name,
        limit=limit,
        offset=offset,
        max_text_length=max_text_length,
        metadata_filter=metadata_filter,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    index_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    limit: Union[Unset, int] = 10,
    offset: Union[Unset, int] = 0,
    max_text_length: Union[None, Unset, int] = 1000,
    metadata_filter: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, ListDocumentsResponse]]:
    r"""List Documents in an Index

     Retrieve a paginated list of documents for a given index.

        ## Request Example:
        ```
        GET /indexes/test_index/documents?limit=5&offset=5&max_text_length=500
        ```

        ## Response Example:
        ```json
        {
          \"documents\": [
            {
              \"doc_id\": \"123456\",
              \"text\": \"Sample document text.\",
              \"metadata\": {\"author\": \"John Doe\"},
              \"is_truncated\": true
            },
            {
              \"doc_id\": \"123457\",
              \"text\": \"Another document text.\",
              \"metadata\": {\"author\": \"Jane Doe\"},
              \"is_truncated\": false
            }
          ],
          \"count\": 5
        }
        ```

    Args:
        index_name (str):
        limit (Union[Unset, int]): Maximum number of documents to return Default: 10.
        offset (Union[Unset, int]): Starting point for the document list Default: 0.
        max_text_length (Union[None, Unset, int]): Maximum text length to return **per document**.
            This does not impose a limit on the total length of all documents returned. Default: 1000.
        metadata_filter (Union[None, Unset, str]): Optional metadata filter to apply when listing
            documents. This should be a dictionary with key-value pairs to match against document
            metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, ListDocumentsResponse]
    """

    return (
        await asyncio_detailed(
            index_name=index_name,
            client=client,
            limit=limit,
            offset=offset,
            max_text_length=max_text_length,
            metadata_filter=metadata_filter,
        )
    ).parsed
