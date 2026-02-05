from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    index_name: str,
    *,
    path: None | str | Unset = UNSET,
    overwrite: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_path: None | str | Unset
    if isinstance(path, Unset):
        json_path = UNSET
    else:
        json_path = path
    params["path"] = json_path

    params["overwrite"] = overwrite

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": "/load/{index_name}".format(
            index_name=quote(str(index_name), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Any | HTTPValidationError | None:
    if response.status_code == 200:
        response_200 = response.json()
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
) -> Response[Any | HTTPValidationError]:
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
    path: None | str | Unset = UNSET,
    overwrite: bool | Unset = False,
) -> Response[Any | HTTPValidationError]:
    r"""Load Index Data from Disk

     Load an existing index from disk at a specified location.

        ## Request Example:
        ```
        POST /load/example_index?path=./custom_path/example_index
        ```

        If no path is provided, will attempt to load from the default directory.

        ## Response Example:
        ```json
        {
          \"message\": \"Successfully loaded index example_index from ./custom_path/example_index.\"
        }
        ```

    Args:
        index_name (str):
        path (None | str | Unset): Path to load the index from
        overwrite (bool | Unset): Overwrite the existing index if it already exists Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        index_name=index_name,
        path=path,
        overwrite=overwrite,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    index_name: str,
    *,
    client: AuthenticatedClient | Client,
    path: None | str | Unset = UNSET,
    overwrite: bool | Unset = False,
) -> Any | HTTPValidationError | None:
    r"""Load Index Data from Disk

     Load an existing index from disk at a specified location.

        ## Request Example:
        ```
        POST /load/example_index?path=./custom_path/example_index
        ```

        If no path is provided, will attempt to load from the default directory.

        ## Response Example:
        ```json
        {
          \"message\": \"Successfully loaded index example_index from ./custom_path/example_index.\"
        }
        ```

    Args:
        index_name (str):
        path (None | str | Unset): Path to load the index from
        overwrite (bool | Unset): Overwrite the existing index if it already exists Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return sync_detailed(
        index_name=index_name,
        client=client,
        path=path,
        overwrite=overwrite,
    ).parsed


async def asyncio_detailed(
    index_name: str,
    *,
    client: AuthenticatedClient | Client,
    path: None | str | Unset = UNSET,
    overwrite: bool | Unset = False,
) -> Response[Any | HTTPValidationError]:
    r"""Load Index Data from Disk

     Load an existing index from disk at a specified location.

        ## Request Example:
        ```
        POST /load/example_index?path=./custom_path/example_index
        ```

        If no path is provided, will attempt to load from the default directory.

        ## Response Example:
        ```json
        {
          \"message\": \"Successfully loaded index example_index from ./custom_path/example_index.\"
        }
        ```

    Args:
        index_name (str):
        path (None | str | Unset): Path to load the index from
        overwrite (bool | Unset): Overwrite the existing index if it already exists Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | HTTPValidationError]
    """

    kwargs = _get_kwargs(
        index_name=index_name,
        path=path,
        overwrite=overwrite,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    index_name: str,
    *,
    client: AuthenticatedClient | Client,
    path: None | str | Unset = UNSET,
    overwrite: bool | Unset = False,
) -> Any | HTTPValidationError | None:
    r"""Load Index Data from Disk

     Load an existing index from disk at a specified location.

        ## Request Example:
        ```
        POST /load/example_index?path=./custom_path/example_index
        ```

        If no path is provided, will attempt to load from the default directory.

        ## Response Example:
        ```json
        {
          \"message\": \"Successfully loaded index example_index from ./custom_path/example_index.\"
        }
        ```

    Args:
        index_name (str):
        path (None | str | Unset): Path to load the index from
        overwrite (bool | Unset): Overwrite the existing index if it already exists Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | HTTPValidationError
    """

    return (
        await asyncio_detailed(
            index_name=index_name,
            client=client,
            path=path,
            overwrite=overwrite,
        )
    ).parsed
