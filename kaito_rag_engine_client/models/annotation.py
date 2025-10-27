from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.annotation_url_citation import AnnotationURLCitation


T = TypeVar("T", bound="Annotation")


@_attrs_define
class Annotation:
    """
    Attributes:
        type_ (Literal['url_citation']):
        url_citation (AnnotationURLCitation):
    """

    type_: Literal["url_citation"]
    url_citation: "AnnotationURLCitation"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_

        url_citation = self.url_citation.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "url_citation": url_citation,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.annotation_url_citation import AnnotationURLCitation

        d = dict(src_dict)
        type_ = cast(Literal["url_citation"], d.pop("type"))
        if type_ != "url_citation":
            raise ValueError(f"type must match const 'url_citation', got '{type_}'")

        url_citation = AnnotationURLCitation.from_dict(d.pop("url_citation"))

        annotation = cls(
            type_=type_,
            url_citation=url_citation,
        )

        annotation.additional_properties = d
        return annotation

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
