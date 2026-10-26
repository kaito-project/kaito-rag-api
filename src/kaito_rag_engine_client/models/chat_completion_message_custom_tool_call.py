from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.custom import Custom


T = TypeVar("T", bound="ChatCompletionMessageCustomToolCall")


@_attrs_define
class ChatCompletionMessageCustomToolCall:
    """
    Attributes:
        id (str):
        custom (Custom):
        type_ (Literal['custom']):
    """

    id: str
    custom: Custom
    type_: Literal["custom"]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        custom = self.custom.to_dict()

        type_ = self.type_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "custom": custom,
                "type": type_,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.custom import Custom  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        custom = Custom.from_dict(d.pop("custom"))

        type_ = cast(Literal["custom"], d.pop("type"))
        if type_ != "custom":
            raise ValueError(f"type must match const 'custom', got '{type_}'")

        chat_completion_message_custom_tool_call = cls(
            id=id,
            custom=custom,
            type_=type_,
        )

        chat_completion_message_custom_tool_call.additional_properties = d
        return chat_completion_message_custom_tool_call

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
