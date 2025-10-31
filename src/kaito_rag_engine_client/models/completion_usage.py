from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.completion_tokens_details import CompletionTokensDetails
    from ..models.prompt_tokens_details import PromptTokensDetails


T = TypeVar("T", bound="CompletionUsage")


@_attrs_define
class CompletionUsage:
    """
    Attributes:
        completion_tokens (int):
        prompt_tokens (int):
        total_tokens (int):
        completion_tokens_details (Union['CompletionTokensDetails', None, Unset]):
        prompt_tokens_details (Union['PromptTokensDetails', None, Unset]):
    """

    completion_tokens: int
    prompt_tokens: int
    total_tokens: int
    completion_tokens_details: Union["CompletionTokensDetails", None, Unset] = UNSET
    prompt_tokens_details: Union["PromptTokensDetails", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.completion_tokens_details import CompletionTokensDetails
        from ..models.prompt_tokens_details import PromptTokensDetails

        completion_tokens = self.completion_tokens

        prompt_tokens = self.prompt_tokens

        total_tokens = self.total_tokens

        completion_tokens_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.completion_tokens_details, Unset):
            completion_tokens_details = UNSET
        elif isinstance(self.completion_tokens_details, CompletionTokensDetails):
            completion_tokens_details = self.completion_tokens_details.to_dict()
        else:
            completion_tokens_details = self.completion_tokens_details

        prompt_tokens_details: Union[None, Unset, dict[str, Any]]
        if isinstance(self.prompt_tokens_details, Unset):
            prompt_tokens_details = UNSET
        elif isinstance(self.prompt_tokens_details, PromptTokensDetails):
            prompt_tokens_details = self.prompt_tokens_details.to_dict()
        else:
            prompt_tokens_details = self.prompt_tokens_details

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "completion_tokens": completion_tokens,
                "prompt_tokens": prompt_tokens,
                "total_tokens": total_tokens,
            }
        )
        if completion_tokens_details is not UNSET:
            field_dict["completion_tokens_details"] = completion_tokens_details
        if prompt_tokens_details is not UNSET:
            field_dict["prompt_tokens_details"] = prompt_tokens_details

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.completion_tokens_details import CompletionTokensDetails
        from ..models.prompt_tokens_details import PromptTokensDetails

        d = dict(src_dict)
        completion_tokens = d.pop("completion_tokens")

        prompt_tokens = d.pop("prompt_tokens")

        total_tokens = d.pop("total_tokens")

        def _parse_completion_tokens_details(data: object) -> Union["CompletionTokensDetails", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                completion_tokens_details_type_0 = CompletionTokensDetails.from_dict(data)

                return completion_tokens_details_type_0
            except:  # noqa: E722
                pass
            return cast(Union["CompletionTokensDetails", None, Unset], data)

        completion_tokens_details = _parse_completion_tokens_details(d.pop("completion_tokens_details", UNSET))

        def _parse_prompt_tokens_details(data: object) -> Union["PromptTokensDetails", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                prompt_tokens_details_type_0 = PromptTokensDetails.from_dict(data)

                return prompt_tokens_details_type_0
            except:  # noqa: E722
                pass
            return cast(Union["PromptTokensDetails", None, Unset], data)

        prompt_tokens_details = _parse_prompt_tokens_details(d.pop("prompt_tokens_details", UNSET))

        completion_usage = cls(
            completion_tokens=completion_tokens,
            prompt_tokens=prompt_tokens,
            total_tokens=total_tokens,
            completion_tokens_details=completion_tokens_details,
            prompt_tokens_details=prompt_tokens_details,
        )

        completion_usage.additional_properties = d
        return completion_usage

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
