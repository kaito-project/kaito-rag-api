from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.document_metadata_type_0 import DocumentMetadataType0


T = TypeVar("T", bound="Document")


@_attrs_define
class Document:
    """
    Attributes:
        text (str):
        doc_id (Union[Unset, str]):  Default: ''.
        metadata (Union['DocumentMetadataType0', None, Unset]):
        hash_value (Union[None, Unset, str]):
        is_truncated (Union[Unset, bool]):  Default: False.
    """

    text: str
    doc_id: Union[Unset, str] = ""
    metadata: Union["DocumentMetadataType0", None, Unset] = UNSET
    hash_value: Union[None, Unset, str] = UNSET
    is_truncated: Union[Unset, bool] = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.document_metadata_type_0 import DocumentMetadataType0

        text = self.text

        doc_id = self.doc_id

        metadata: Union[None, Unset, dict[str, Any]]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, DocumentMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        hash_value: Union[None, Unset, str]
        if isinstance(self.hash_value, Unset):
            hash_value = UNSET
        else:
            hash_value = self.hash_value

        is_truncated = self.is_truncated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "text": text,
            }
        )
        if doc_id is not UNSET:
            field_dict["doc_id"] = doc_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if hash_value is not UNSET:
            field_dict["hash_value"] = hash_value
        if is_truncated is not UNSET:
            field_dict["is_truncated"] = is_truncated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.document_metadata_type_0 import DocumentMetadataType0

        d = dict(src_dict)
        text = d.pop("text")

        doc_id = d.pop("doc_id", UNSET)

        def _parse_metadata(data: object) -> Union["DocumentMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = DocumentMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["DocumentMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_hash_value(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        hash_value = _parse_hash_value(d.pop("hash_value", UNSET))

        is_truncated = d.pop("is_truncated", UNSET)

        document = cls(
            text=text,
            doc_id=doc_id,
            metadata=metadata,
            hash_value=hash_value,
            is_truncated=is_truncated,
        )

        document.additional_properties = d
        return document

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
