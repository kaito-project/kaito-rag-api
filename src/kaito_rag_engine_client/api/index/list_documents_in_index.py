from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.list_documents_response import ListDocumentsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    index_name: str,
    *,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    max_text_length: int | None | Unset = 1000,
    metadata_filter: None | str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["limit"] = limit

    params["offset"] = offset

    json_max_text_length: int | None | Unset
    if isinstance(max_text_length, Unset):
        json_max_text_length = UNSET
    else:
        json_max_text_length = max_text_length
    params["max_text_length"] = json_max_text_length

    json_metadata_filter: None | str | Unset
    if isinstance(metadata_filter, Unset):
        json_metadata_filter = UNSET
    else:
        json_metadata_filter = metadata_filter
    params["metadata_filter"] = json_metadata_filter

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/indexes/{index_name}/documents".format(
            index_name=quote(str(index_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | ListDocumentsResponse | None:
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
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[HTTPValidationError | ListDocumentsResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    index_name: str,
    *,
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    max_text_length: int | None | Unset = 1000,
    metadata_filter: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ListDocumentsResponse]:
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
        limit (int | Unset): Maximum number of documents to return Default: 10.
        offset (int | Unset): Starting point for the document list Default: 0.
        max_text_length (int | None | Unset): Maximum text length to return **per document**. This
            does not impose a limit on the total length of all documents returned. Default: 1000.
        metadata_filter (None | str | Unset): Optional metadata filter to apply when listing
            documents. This should be a dictionary with key-value pairs to match against document
            metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListDocumentsResponse]
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
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    max_text_length: int | None | Unset = 1000,
    metadata_filter: None | str | Unset = UNSET,
) -> HTTPValidationError | ListDocumentsResponse | None:
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
        limit (int | Unset): Maximum number of documents to return Default: 10.
        offset (int | Unset): Starting point for the document list Default: 0.
        max_text_length (int | None | Unset): Maximum text length to return **per document**. This
            does not impose a limit on the total length of all documents returned. Default: 1000.
        metadata_filter (None | str | Unset): Optional metadata filter to apply when listing
            documents. This should be a dictionary with key-value pairs to match against document
            metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListDocumentsResponse
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
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    max_text_length: int | None | Unset = 1000,
    metadata_filter: None | str | Unset = UNSET,
) -> Response[HTTPValidationError | ListDocumentsResponse]:
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
        limit (int | Unset): Maximum number of documents to return Default: 10.
        offset (int | Unset): Starting point for the document list Default: 0.
        max_text_length (int | None | Unset): Maximum text length to return **per document**. This
            does not impose a limit on the total length of all documents returned. Default: 1000.
        metadata_filter (None | str | Unset): Optional metadata filter to apply when listing
            documents. This should be a dictionary with key-value pairs to match against document
            metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | ListDocumentsResponse]
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
    client: AuthenticatedClient | Client,
    limit: int | Unset = 10,
    offset: int | Unset = 0,
    max_text_length: int | None | Unset = 1000,
    metadata_filter: None | str | Unset = UNSET,
) -> HTTPValidationError | ListDocumentsResponse | None:
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
        limit (int | Unset): Maximum number of documents to return Default: 10.
        offset (int | Unset): Starting point for the document list Default: 0.
        max_text_length (int | None | Unset): Maximum text length to return **per document**. This
            does not impose a limit on the total length of all documents returned. Default: 1000.
        metadata_filter (None | str | Unset): Optional metadata filter to apply when listing
            documents. This should be a dictionary with key-value pairs to match against document
            metadata.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | ListDocumentsResponse
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
