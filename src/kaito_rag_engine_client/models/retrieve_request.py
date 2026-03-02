from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.retrieve_request_metadata_filter_type_0 import RetrieveRequestMetadataFilterType0


T = TypeVar("T", bound="RetrieveRequest")


@_attrs_define
class RetrieveRequest:
    """
    Attributes:
        index_name (str): Name of the index to retrieve from
        query (str): User query string for retrieve
        max_node_count (int | Unset): Maximum number of documents to return (default: 5, max: 300) Default: 5.
        metadata_filter (None | RetrieveRequestMetadataFilterType0 | Unset): Optional metadata filter for retrieve
            results
    """

    index_name: str
    query: str
    max_node_count: int | Unset = 5
    metadata_filter: None | RetrieveRequestMetadataFilterType0 | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.retrieve_request_metadata_filter_type_0 import RetrieveRequestMetadataFilterType0

        index_name = self.index_name

        query = self.query

        max_node_count = self.max_node_count

        metadata_filter: dict[str, Any] | None | Unset
        if isinstance(self.metadata_filter, Unset):
            metadata_filter = UNSET
        elif isinstance(self.metadata_filter, RetrieveRequestMetadataFilterType0):
            metadata_filter = self.metadata_filter.to_dict()
        else:
            metadata_filter = self.metadata_filter

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index_name": index_name,
                "query": query,
            }
        )
        if max_node_count is not UNSET:
            field_dict["max_node_count"] = max_node_count
        if metadata_filter is not UNSET:
            field_dict["metadata_filter"] = metadata_filter

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.retrieve_request_metadata_filter_type_0 import RetrieveRequestMetadataFilterType0

        d = dict(src_dict)
        index_name = d.pop("index_name")

        query = d.pop("query")

        max_node_count = d.pop("max_node_count", UNSET)

        def _parse_metadata_filter(data: object) -> None | RetrieveRequestMetadataFilterType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_filter_type_0 = RetrieveRequestMetadataFilterType0.from_dict(data)

                return metadata_filter_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | RetrieveRequestMetadataFilterType0 | Unset, data)

        metadata_filter = _parse_metadata_filter(d.pop("metadata_filter", UNSET))

        retrieve_request = cls(
            index_name=index_name,
            query=query,
            max_node_count=max_node_count,
            metadata_filter=metadata_filter,
        )

        retrieve_request.additional_properties = d
        return retrieve_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
