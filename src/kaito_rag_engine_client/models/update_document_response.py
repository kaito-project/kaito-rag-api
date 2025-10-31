from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.document import Document


T = TypeVar("T", bound="UpdateDocumentResponse")


@_attrs_define
class UpdateDocumentResponse:
    """
    Attributes:
        updated_documents (list['Document']):
        unchanged_documents (list['Document']):
        not_found_documents (list['Document']):
    """

    updated_documents: list["Document"]
    unchanged_documents: list["Document"]
    not_found_documents: list["Document"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        updated_documents = []
        for updated_documents_item_data in self.updated_documents:
            updated_documents_item = updated_documents_item_data.to_dict()
            updated_documents.append(updated_documents_item)

        unchanged_documents = []
        for unchanged_documents_item_data in self.unchanged_documents:
            unchanged_documents_item = unchanged_documents_item_data.to_dict()
            unchanged_documents.append(unchanged_documents_item)

        not_found_documents = []
        for not_found_documents_item_data in self.not_found_documents:
            not_found_documents_item = not_found_documents_item_data.to_dict()
            not_found_documents.append(not_found_documents_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "updated_documents": updated_documents,
                "unchanged_documents": unchanged_documents,
                "not_found_documents": not_found_documents,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document import Document

        d = dict(src_dict)
        updated_documents = []
        _updated_documents = d.pop("updated_documents")
        for updated_documents_item_data in _updated_documents:
            updated_documents_item = Document.from_dict(updated_documents_item_data)

            updated_documents.append(updated_documents_item)

        unchanged_documents = []
        _unchanged_documents = d.pop("unchanged_documents")
        for unchanged_documents_item_data in _unchanged_documents:
            unchanged_documents_item = Document.from_dict(unchanged_documents_item_data)

            unchanged_documents.append(unchanged_documents_item)

        not_found_documents = []
        _not_found_documents = d.pop("not_found_documents")
        for not_found_documents_item_data in _not_found_documents:
            not_found_documents_item = Document.from_dict(not_found_documents_item_data)

            not_found_documents.append(not_found_documents_item)

        update_document_response = cls(
            updated_documents=updated_documents,
            unchanged_documents=unchanged_documents,
            not_found_documents=not_found_documents,
        )

        update_document_response.additional_properties = d
        return update_document_response

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
