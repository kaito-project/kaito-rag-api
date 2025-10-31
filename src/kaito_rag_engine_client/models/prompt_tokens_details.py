from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PromptTokensDetails")


@_attrs_define
class PromptTokensDetails:
    """
    Attributes:
        audio_tokens (Union[None, Unset, int]):
        cached_tokens (Union[None, Unset, int]):
    """

    audio_tokens: Union[None, Unset, int] = UNSET
    cached_tokens: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        audio_tokens: Union[None, Unset, int]
        if isinstance(self.audio_tokens, Unset):
            audio_tokens = UNSET
        else:
            audio_tokens = self.audio_tokens

        cached_tokens: Union[None, Unset, int]
        if isinstance(self.cached_tokens, Unset):
            cached_tokens = UNSET
        else:
            cached_tokens = self.cached_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if audio_tokens is not UNSET:
            field_dict["audio_tokens"] = audio_tokens
        if cached_tokens is not UNSET:
            field_dict["cached_tokens"] = cached_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_audio_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        audio_tokens = _parse_audio_tokens(d.pop("audio_tokens", UNSET))

        def _parse_cached_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        cached_tokens = _parse_cached_tokens(d.pop("cached_tokens", UNSET))

        prompt_tokens_details = cls(
            audio_tokens=audio_tokens,
            cached_tokens=cached_tokens,
        )

        prompt_tokens_details.additional_properties = d
        return prompt_tokens_details

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
