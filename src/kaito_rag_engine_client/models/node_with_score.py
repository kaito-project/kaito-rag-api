from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.node_with_score_metadata_type_0 import NodeWithScoreMetadataType0


T = TypeVar("T", bound="NodeWithScore")


@_attrs_define
class NodeWithScore:
    """
    Attributes:
        doc_id (str):
        node_id (str):
        text (str):
        score (float):
        metadata (Union['NodeWithScoreMetadataType0', None, Unset]):
    """

    doc_id: str
    node_id: str
    text: str
    score: float
    metadata: Union["NodeWithScoreMetadataType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.node_with_score_metadata_type_0 import NodeWithScoreMetadataType0

        doc_id = self.doc_id

        node_id = self.node_id

        text = self.text

        score = self.score

        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, NodeWithScoreMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "doc_id": doc_id,
                "node_id": node_id,
                "text": text,
                "score": score,
            }
        )
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_with_score_metadata_type_0 import NodeWithScoreMetadataType0

        d = dict(src_dict)
        doc_id = d.pop("doc_id")

        node_id = d.pop("node_id")

        text = d.pop("text")

        score = d.pop("score")

        def _parse_metadata(data: object) -> Union["NodeWithScoreMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = NodeWithScoreMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NodeWithScoreMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        node_with_score = cls(
            doc_id=doc_id,
            node_id=node_id,
            text=text,
            score=score,
            metadata=metadata,
        )

        node_with_score.additional_properties = d
        return node_with_score

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
