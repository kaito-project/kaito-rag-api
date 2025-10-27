from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.delete_document_request import DeleteDocumentRequest
from ...models.delete_document_response import DeleteDocumentResponse
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    index_name: str,
    *,
    body: DeleteDocumentRequest,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/indexes/{index_name}/documents/delete",
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[DeleteDocumentResponse, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = DeleteDocumentResponse.from_dict(response.json())

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
) -> Response[Union[DeleteDocumentResponse, HTTPValidationError]]:
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
    body: DeleteDocumentRequest,
) -> Response[Union[DeleteDocumentResponse, HTTPValidationError]]:
    r"""Delete documents in an Index

     Delete document in an Index by their ids.

        ## Request Example:
        ```json
        POST /indexes/test_index/documents/delete
        {\"doc_ids\": [\"doc_id_1\", \"doc_id_2\", \"doc_id_3\"]}
        ```

        ## Response Example:
        ```json
        {
            \"deleted_doc_ids\": [\"doc_id_1\", \"doc_id_2\"],
            \"not_found_doc_ids\": [\"doc_id_3\"]
        },
        ```

    Args:
        index_name (str):
        body (DeleteDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteDocumentResponse, HTTPValidationError]]
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
    client: Union[AuthenticatedClient, Client],
    body: DeleteDocumentRequest,
) -> Optional[Union[DeleteDocumentResponse, HTTPValidationError]]:
    r"""Delete documents in an Index

     Delete document in an Index by their ids.

        ## Request Example:
        ```json
        POST /indexes/test_index/documents/delete
        {\"doc_ids\": [\"doc_id_1\", \"doc_id_2\", \"doc_id_3\"]}
        ```

        ## Response Example:
        ```json
        {
            \"deleted_doc_ids\": [\"doc_id_1\", \"doc_id_2\"],
            \"not_found_doc_ids\": [\"doc_id_3\"]
        },
        ```

    Args:
        index_name (str):
        body (DeleteDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteDocumentResponse, HTTPValidationError]
    """

    return sync_detailed(
        index_name=index_name,
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    index_name: str,
    *,
    client: Union[AuthenticatedClient, Client],
    body: DeleteDocumentRequest,
) -> Response[Union[DeleteDocumentResponse, HTTPValidationError]]:
    r"""Delete documents in an Index

     Delete document in an Index by their ids.

        ## Request Example:
        ```json
        POST /indexes/test_index/documents/delete
        {\"doc_ids\": [\"doc_id_1\", \"doc_id_2\", \"doc_id_3\"]}
        ```

        ## Response Example:
        ```json
        {
            \"deleted_doc_ids\": [\"doc_id_1\", \"doc_id_2\"],
            \"not_found_doc_ids\": [\"doc_id_3\"]
        },
        ```

    Args:
        index_name (str):
        body (DeleteDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[DeleteDocumentResponse, HTTPValidationError]]
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
    client: Union[AuthenticatedClient, Client],
    body: DeleteDocumentRequest,
) -> Optional[Union[DeleteDocumentResponse, HTTPValidationError]]:
    r"""Delete documents in an Index

     Delete document in an Index by their ids.

        ## Request Example:
        ```json
        POST /indexes/test_index/documents/delete
        {\"doc_ids\": [\"doc_id_1\", \"doc_id_2\", \"doc_id_3\"]}
        ```

        ## Response Example:
        ```json
        {
            \"deleted_doc_ids\": [\"doc_id_1\", \"doc_id_2\"],
            \"not_found_doc_ids\": [\"doc_id_3\"]
        },
        ```

    Args:
        index_name (str):
        body (DeleteDocumentRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[DeleteDocumentResponse, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            index_name=index_name,
            client=client,
            body=body,
        )
    ).parsed
