from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.choice_finish_reason import ChoiceFinishReason
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.chat_completion_message import ChatCompletionMessage
    from ..models.choice_logprobs import ChoiceLogprobs


T = TypeVar("T", bound="Choice")


@_attrs_define
class Choice:
    """
    Attributes:
        finish_reason (ChoiceFinishReason):
        index (int):
        message (ChatCompletionMessage):
        logprobs (Union['ChoiceLogprobs', None, Unset]):
    """

    finish_reason: ChoiceFinishReason
    index: int
    message: "ChatCompletionMessage"
    logprobs: Union["ChoiceLogprobs", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.choice_logprobs import ChoiceLogprobs

        finish_reason = self.finish_reason.value

        index = self.index

        message = self.message.to_dict()

        logprobs: Union[None, Unset, dict[str, Any]]
        if isinstance(self.logprobs, Unset):
            logprobs = UNSET
        elif isinstance(self.logprobs, ChoiceLogprobs):
            logprobs = self.logprobs.to_dict()
        else:
            logprobs = self.logprobs

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "finish_reason": finish_reason,
                "index": index,
                "message": message,
            }
        )
        if logprobs is not UNSET:
            field_dict["logprobs"] = logprobs

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.chat_completion_message import ChatCompletionMessage
        from ..models.choice_logprobs import ChoiceLogprobs

        d = dict(src_dict)
        finish_reason = ChoiceFinishReason(d.pop("finish_reason"))

        index = d.pop("index")

        message = ChatCompletionMessage.from_dict(d.pop("message"))

        def _parse_logprobs(data: object) -> Union["ChoiceLogprobs", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                logprobs_type_0 = ChoiceLogprobs.from_dict(data)

                return logprobs_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ChoiceLogprobs", None, Unset], data)

        logprobs = _parse_logprobs(d.pop("logprobs", UNSET))

        choice = cls(
            finish_reason=finish_reason,
            index=index,
            message=message,
            logprobs=logprobs,
        )

        choice.additional_properties = d
        return choice

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
