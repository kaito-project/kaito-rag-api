from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    index_name: str,
    *,
    path: Union[None, Unset, str] = UNSET,
    overwrite: Union[Unset, bool] = False,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_path: Union[None, Unset, str]
    if isinstance(path, Unset):
        json_path = UNSET
    else:
        json_path = path
    params["path"] = json_path

    params["overwrite"] = overwrite

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "post",
        "url": f"/load/{index_name}",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
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
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
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
    path: Union[None, Unset, str] = UNSET,
    overwrite: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
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
        path (Union[None, Unset, str]): Path to load the index from
        overwrite (Union[Unset, bool]): Overwrite the existing index if it already exists Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
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
    client: Union[AuthenticatedClient, Client],
    path: Union[None, Unset, str] = UNSET,
    overwrite: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
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
        path (Union[None, Unset, str]): Path to load the index from
        overwrite (Union[Unset, bool]): Overwrite the existing index if it already exists Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
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
    client: Union[AuthenticatedClient, Client],
    path: Union[None, Unset, str] = UNSET,
    overwrite: Union[Unset, bool] = False,
) -> Response[Union[Any, HTTPValidationError]]:
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
        path (Union[None, Unset, str]): Path to load the index from
        overwrite (Union[Unset, bool]): Overwrite the existing index if it already exists Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
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
    client: Union[AuthenticatedClient, Client],
    path: Union[None, Unset, str] = UNSET,
    overwrite: Union[Unset, bool] = False,
) -> Optional[Union[Any, HTTPValidationError]]:
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
        path (Union[None, Unset, str]): Path to load the index from
        overwrite (Union[Unset, bool]): Overwrite the existing index if it already exists Default:
            False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            index_name=index_name,
            client=client,
            path=path,
            overwrite=overwrite,
        )
    ).parsed
