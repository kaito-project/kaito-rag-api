from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_with_score import NodeWithScore
    from ..models.query_response_metadata_type_0 import QueryResponseMetadataType0


T = TypeVar("T", bound="QueryResponse")


@_attrs_define
class QueryResponse:
    """
    Attributes:
        response (str):
        source_nodes (list['NodeWithScore']):
        metadata (Union['QueryResponseMetadataType0', None, Unset]):
    """

    response: str
    source_nodes: list["NodeWithScore"]
    metadata: Union["QueryResponseMetadataType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.query_response_metadata_type_0 import QueryResponseMetadataType0

        response = self.response

        source_nodes = []
        for source_nodes_item_data in self.source_nodes:
            source_nodes_item = source_nodes_item_data.to_dict()
            source_nodes.append(source_nodes_item)

        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, QueryResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "response": response,
                "source_nodes": source_nodes,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_with_score import NodeWithScore
        from ..models.query_response_metadata_type_0 import QueryResponseMetadataType0

        d = dict(src_dict)
        response = d.pop("response")

        source_nodes = []
        _source_nodes = d.pop("source_nodes")
        for source_nodes_item_data in _source_nodes:
            source_nodes_item = NodeWithScore.from_dict(source_nodes_item_data)

            source_nodes.append(source_nodes_item)

        def _parse_metadata(data: object) -> Union["QueryResponseMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = QueryResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["QueryResponseMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        query_response = cls(
            response=response,
            source_nodes=source_nodes,
            metadata=metadata,
        )

        query_response.additional_properties = d
        return query_response

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
