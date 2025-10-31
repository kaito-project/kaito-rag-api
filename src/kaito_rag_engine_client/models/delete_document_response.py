from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="DeleteDocumentResponse")


@_attrs_define
class DeleteDocumentResponse:
    """
    Attributes:
        deleted_doc_ids (list[str]):
        not_found_doc_ids (list[str]):
    """

    deleted_doc_ids: list[str]
    not_found_doc_ids: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deleted_doc_ids = self.deleted_doc_ids

        not_found_doc_ids = self.not_found_doc_ids

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "deleted_doc_ids": deleted_doc_ids,
                "not_found_doc_ids": not_found_doc_ids,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        deleted_doc_ids = cast(list[str], d.pop("deleted_doc_ids"))

        not_found_doc_ids = cast(list[str], d.pop("not_found_doc_ids"))

        delete_document_response = cls(
            deleted_doc_ids=deleted_doc_ids,
            not_found_doc_ids=not_found_doc_ids,
        )

        delete_document_response.additional_properties = d
        return delete_document_response

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
