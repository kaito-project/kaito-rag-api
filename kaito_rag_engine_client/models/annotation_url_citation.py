from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="AnnotationURLCitation")


@_attrs_define
class AnnotationURLCitation:
    """
    Attributes:
        end_index (int):
        start_index (int):
        title (str):
        url (str):
    """

    end_index: int
    start_index: int
    title: str
    url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        end_index = self.end_index

        start_index = self.start_index

        title = self.title

        url = self.url

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "end_index": end_index,
                "start_index": start_index,
                "title": title,
                "url": url,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        end_index = d.pop("end_index")

        start_index = d.pop("start_index")

        title = d.pop("title")

        url = d.pop("url")

        annotation_url_citation = cls(
            end_index=end_index,
            start_index=start_index,
            title=title,
            url=url,
        )

        annotation_url_citation.additional_properties = d
        return annotation_url_citation

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
