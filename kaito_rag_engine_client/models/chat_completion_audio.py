from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ChatCompletionAudio")


@_attrs_define
class ChatCompletionAudio:
    """
    Attributes:
        id (str):
        data (str):
        expires_at (int):
        transcript (str):
    """

    id: str
    data: str
    expires_at: int
    transcript: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        data = self.data

        expires_at = self.expires_at

        transcript = self.transcript

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "data": data,
                "expires_at": expires_at,
                "transcript": transcript,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        data = d.pop("data")

        expires_at = d.pop("expires_at")

        transcript = d.pop("transcript")

        chat_completion_audio = cls(
            id=id,
            data=data,
            expires_at=expires_at,
            transcript=transcript,
        )

        chat_completion_audio.additional_properties = d
        return chat_completion_audio

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
