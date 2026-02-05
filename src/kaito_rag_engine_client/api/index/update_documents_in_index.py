from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.update_document_request import UpdateDocumentRequest
from ...models.update_document_response import UpdateDocumentResponse
from ...types import Response


def _get_kwargs(
    index_name: str,
    *,
    body: UpdateDocumentRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/indexes/{index_name}/documents".format(
            index_name=quote(str(index_name), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> HTTPValidationError | UpdateDocumentResponse | None:
    if response.status_code == 200:
        response_200 = UpdateDocumentResponse.from_dict(response.json())

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
) -> Response[HTTPValidationError | UpdateDocumentResponse]:
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
    body: UpdateDocumentRequest,
) -> Response[HTTPValidationError | UpdateDocumentResponse]:
    r"""Update documents in an Index

     Update document in an Index.

        ## Request Example:
        ```json
        POST /indexes/test_index/documents
        {\"documents\": [{\"doc_id\": \"sampleid\", \"text\": \"Sample document text.\", \"metadata\":
    {\"author\": \"John Doe\", \"category\": \"example\"}}]}
        ```

        ## Response Example:
        ```json
        {
            \"updated_documents\": [{\"doc_id\": \"sampleid\", \"text\": \"Sample document text.\",
    \"metadata\": {\"author\": \"John Doe\", \"category\": \"example\"}}],
            \"unchanged_documents\": [],
            \"not_found_documents\": []
        },
        ```

    Args:
        index_name (str):
        body (UpdateDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UpdateDocumentResponse]
    """

    kwargs = _get_kwargs(
        index_name=index_name,
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    index_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateDocumentRequest,
) -> HTTPValidationError | UpdateDocumentResponse | None:
    r"""Update documents in an Index

     Update document in an Index.

        ## Request Example:
        ```json
        POST /indexes/test_index/documents
        {\"documents\": [{\"doc_id\": \"sampleid\", \"text\": \"Sample document text.\", \"metadata\":
    {\"author\": \"John Doe\", \"category\": \"example\"}}]}
        ```

        ## Response Example:
        ```json
        {
            \"updated_documents\": [{\"doc_id\": \"sampleid\", \"text\": \"Sample document text.\",
    \"metadata\": {\"author\": \"John Doe\", \"category\": \"example\"}}],
            \"unchanged_documents\": [],
            \"not_found_documents\": []
        },
        ```

    Args:
        index_name (str):
        body (UpdateDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UpdateDocumentResponse
    """

    return sync_detailed(
        index_name=index_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    index_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateDocumentRequest,
) -> Response[HTTPValidationError | UpdateDocumentResponse]:
    r"""Update documents in an Index

     Update document in an Index.

        ## Request Example:
        ```json
        POST /indexes/test_index/documents
        {\"documents\": [{\"doc_id\": \"sampleid\", \"text\": \"Sample document text.\", \"metadata\":
    {\"author\": \"John Doe\", \"category\": \"example\"}}]}
        ```

        ## Response Example:
        ```json
        {
            \"updated_documents\": [{\"doc_id\": \"sampleid\", \"text\": \"Sample document text.\",
    \"metadata\": {\"author\": \"John Doe\", \"category\": \"example\"}}],
            \"unchanged_documents\": [],
            \"not_found_documents\": []
        },
        ```

    Args:
        index_name (str):
        body (UpdateDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError | UpdateDocumentResponse]
    """

    kwargs = _get_kwargs(
        index_name=index_name,
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    index_name: str,
    *,
    client: AuthenticatedClient | Client,
    body: UpdateDocumentRequest,
) -> HTTPValidationError | UpdateDocumentResponse | None:
    r"""Update documents in an Index

     Update document in an Index.

        ## Request Example:
        ```json
        POST /indexes/test_index/documents
        {\"documents\": [{\"doc_id\": \"sampleid\", \"text\": \"Sample document text.\", \"metadata\":
    {\"author\": \"John Doe\", \"category\": \"example\"}}]}
        ```

        ## Response Example:
        ```json
        {
            \"updated_documents\": [{\"doc_id\": \"sampleid\", \"text\": \"Sample document text.\",
    \"metadata\": {\"author\": \"John Doe\", \"category\": \"example\"}}],
            \"unchanged_documents\": [],
            \"not_found_documents\": []
        },
        ```

    Args:
        index_name (str):
        body (UpdateDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError | UpdateDocumentResponse
    """

    return (
        await asyncio_detailed(
            index_name=index_name,
            client=client,
            body=body,
        )
    ).parsed
