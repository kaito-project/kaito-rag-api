from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_token_logprob import ChatCompletionTokenLogprob


T = TypeVar("T", bound="ChoiceLogprobs")


@_attrs_define
class ChoiceLogprobs:
    """
    Attributes:
        content (Union[None, Unset, list['ChatCompletionTokenLogprob']]):
        refusal (Union[None, Unset, list['ChatCompletionTokenLogprob']]):
    """

    content: Union[None, Unset, list["ChatCompletionTokenLogprob"]] = UNSET
    refusal: Union[None, Unset, list["ChatCompletionTokenLogprob"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        content: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.content, Unset):
            content = UNSET
        elif isinstance(self.content, list):
            content = []
            for content_type_0_item_data in self.content:
                content_type_0_item = content_type_0_item_data.to_dict()
                content.append(content_type_0_item)

        else:
            content = self.content

        refusal: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.refusal, Unset):
            refusal = UNSET
        elif isinstance(self.refusal, list):
            refusal = []
            for refusal_type_0_item_data in self.refusal:
                refusal_type_0_item = refusal_type_0_item_data.to_dict()
                refusal.append(refusal_type_0_item)

        else:
            refusal = self.refusal

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if content is not UNSET:
            field_dict["content"] = content
        if refusal is not UNSET:
            field_dict["refusal"] = refusal

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_token_logprob import ChatCompletionTokenLogprob

        d = dict(src_dict)

        def _parse_content(data: object) -> Union[None, Unset, list["ChatCompletionTokenLogprob"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                content_type_0 = []
                _content_type_0 = data
                for content_type_0_item_data in _content_type_0:
                    content_type_0_item = ChatCompletionTokenLogprob.from_dict(content_type_0_item_data)

                    content_type_0.append(content_type_0_item)

                return content_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ChatCompletionTokenLogprob"]], data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_refusal(data: object) -> Union[None, Unset, list["ChatCompletionTokenLogprob"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                refusal_type_0 = []
                _refusal_type_0 = data
                for refusal_type_0_item_data in _refusal_type_0:
                    refusal_type_0_item = ChatCompletionTokenLogprob.from_dict(refusal_type_0_item_data)

                    refusal_type_0.append(refusal_type_0_item)

                return refusal_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ChatCompletionTokenLogprob"]], data)

        refusal = _parse_refusal(d.pop("refusal", UNSET))

        choice_logprobs = cls(
            content=content,
            refusal=refusal,
        )

        choice_logprobs.additional_properties = d
        return choice_logprobs

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
