from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompletionTokensDetails")


@_attrs_define
class CompletionTokensDetails:
    """
    Attributes:
        accepted_prediction_tokens (Union[None, Unset, int]):
        audio_tokens (Union[None, Unset, int]):
        reasoning_tokens (Union[None, Unset, int]):
        rejected_prediction_tokens (Union[None, Unset, int]):
    """

    accepted_prediction_tokens: Union[None, Unset, int] = UNSET
    audio_tokens: Union[None, Unset, int] = UNSET
    reasoning_tokens: Union[None, Unset, int] = UNSET
    rejected_prediction_tokens: Union[None, Unset, int] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        accepted_prediction_tokens: Union[None, Unset, int]
        if isinstance(self.accepted_prediction_tokens, Unset):
            accepted_prediction_tokens = UNSET
        else:
            accepted_prediction_tokens = self.accepted_prediction_tokens

        audio_tokens: Union[None, Unset, int]
        if isinstance(self.audio_tokens, Unset):
            audio_tokens = UNSET
        else:
            audio_tokens = self.audio_tokens

        reasoning_tokens: Union[None, Unset, int]
        if isinstance(self.reasoning_tokens, Unset):
            reasoning_tokens = UNSET
        else:
            reasoning_tokens = self.reasoning_tokens

        rejected_prediction_tokens: Union[None, Unset, int]
        if isinstance(self.rejected_prediction_tokens, Unset):
            rejected_prediction_tokens = UNSET
        else:
            rejected_prediction_tokens = self.rejected_prediction_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if accepted_prediction_tokens is not UNSET:
            field_dict["accepted_prediction_tokens"] = accepted_prediction_tokens
        if audio_tokens is not UNSET:
            field_dict["audio_tokens"] = audio_tokens
        if reasoning_tokens is not UNSET:
            field_dict["reasoning_tokens"] = reasoning_tokens
        if rejected_prediction_tokens is not UNSET:
            field_dict["rejected_prediction_tokens"] = rejected_prediction_tokens

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_accepted_prediction_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        accepted_prediction_tokens = _parse_accepted_prediction_tokens(d.pop("accepted_prediction_tokens", UNSET))

        def _parse_audio_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        audio_tokens = _parse_audio_tokens(d.pop("audio_tokens", UNSET))

        def _parse_reasoning_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        reasoning_tokens = _parse_reasoning_tokens(d.pop("reasoning_tokens", UNSET))

        def _parse_rejected_prediction_tokens(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rejected_prediction_tokens = _parse_rejected_prediction_tokens(d.pop("rejected_prediction_tokens", UNSET))

        completion_tokens_details = cls(
            accepted_prediction_tokens=accepted_prediction_tokens,
            audio_tokens=audio_tokens,
            reasoning_tokens=reasoning_tokens,
            rejected_prediction_tokens=rejected_prediction_tokens,
        )

        completion_tokens_details.additional_properties = d
        return completion_tokens_details

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
