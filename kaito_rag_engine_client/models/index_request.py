from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.document import Document


T = TypeVar("T", bound="IndexRequest")


@_attrs_define
class IndexRequest:
    """
    Attributes:
        index_name (str):
        documents (list['Document']):
    """

    index_name: str
    documents: list["Document"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        index_name = self.index_name

        documents = []
        for documents_item_data in self.documents:
            documents_item = documents_item_data.to_dict()
            documents.append(documents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index_name": index_name,
                "documents": documents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document import Document

        d = dict(src_dict)
        index_name = d.pop("index_name")

        documents = []
        _documents = d.pop("documents")
        for documents_item_data in _documents:
            documents_item = Document.from_dict(documents_item_data)

            documents.append(documents_item)

        index_request = cls(
            index_name=index_name,
            documents=documents,
        )

        index_request.additional_properties = d
        return index_request

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
