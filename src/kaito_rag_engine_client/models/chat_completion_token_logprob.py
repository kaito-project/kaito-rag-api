from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.top_logprob import TopLogprob


T = TypeVar("T", bound="ChatCompletionTokenLogprob")


@_attrs_define
class ChatCompletionTokenLogprob:
    """
    Attributes:
        token (str):
        logprob (float):
        top_logprobs (list['TopLogprob']):
        bytes_ (Union[None, Unset, list[int]]):
    """

    token: str
    logprob: float
    top_logprobs: list["TopLogprob"]
    bytes_: Union[None, Unset, list[int]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        logprob = self.logprob

        top_logprobs = []
        for top_logprobs_item_data in self.top_logprobs:
            top_logprobs_item = top_logprobs_item_data.to_dict()
            top_logprobs.append(top_logprobs_item)

        bytes_: Union[None, Unset, list[int]]
        if isinstance(self.bytes_, Unset):
            bytes_ = UNSET
        elif isinstance(self.bytes_, list):
            bytes_ = self.bytes_

        else:
            bytes_ = self.bytes_

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "logprob": logprob,
                "top_logprobs": top_logprobs,
            }
        )
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.top_logprob import TopLogprob

        d = dict(src_dict)
        token = d.pop("token")

        logprob = d.pop("logprob")

        top_logprobs = []
        _top_logprobs = d.pop("top_logprobs")
        for top_logprobs_item_data in _top_logprobs:
            top_logprobs_item = TopLogprob.from_dict(top_logprobs_item_data)

            top_logprobs.append(top_logprobs_item)

        def _parse_bytes_(data: object) -> Union[None, Unset, list[int]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bytes_type_0 = cast(list[int], data)

                return bytes_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list[int]], data)

        bytes_ = _parse_bytes_(d.pop("bytes", UNSET))

        chat_completion_token_logprob = cls(
            token=token,
            logprob=logprob,
            top_logprobs=top_logprobs,
            bytes_=bytes_,
        )

        chat_completion_token_logprob.additional_properties = d
        return chat_completion_token_logprob

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
