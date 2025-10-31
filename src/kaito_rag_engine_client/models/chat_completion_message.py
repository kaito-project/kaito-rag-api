from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.annotation import Annotation
    from ..models.chat_completion_audio import ChatCompletionAudio
    from ..models.chat_completion_message_tool_call import ChatCompletionMessageToolCall
    from ..models.function_call import FunctionCall


T = TypeVar("T", bound="ChatCompletionMessage")


@_attrs_define
class ChatCompletionMessage:
    """
    Attributes:
        role (Literal['assistant']):
        content (Union[None, Unset, str]):
        refusal (Union[None, Unset, str]):
        annotations (Union[None, Unset, list['Annotation']]):
        audio (Union['ChatCompletionAudio', None, Unset]):
        function_call (Union['FunctionCall', None, Unset]):
        tool_calls (Union[None, Unset, list['ChatCompletionMessageToolCall']]):
    """

    role: Literal["assistant"]
    content: Union[None, Unset, str] = UNSET
    refusal: Union[None, Unset, str] = UNSET
    annotations: Union[None, Unset, list["Annotation"]] = UNSET
    audio: Union["ChatCompletionAudio", None, Unset] = UNSET
    function_call: Union["FunctionCall", None, Unset] = UNSET
    tool_calls: Union[None, Unset, list["ChatCompletionMessageToolCall"]] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.chat_completion_audio import ChatCompletionAudio
        from ..models.function_call import FunctionCall

        role = self.role

        content: Union[None, Unset, str]
        if isinstance(self.content, Unset):
            content = UNSET
        else:
            content = self.content

        refusal: Union[None, Unset, str]
        if isinstance(self.refusal, Unset):
            refusal = UNSET
        else:
            refusal = self.refusal

        annotations: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.annotations, Unset):
            annotations = UNSET
        elif isinstance(self.annotations, list):
            annotations = []
            for annotations_type_0_item_data in self.annotations:
                annotations_type_0_item = annotations_type_0_item_data.to_dict()
                annotations.append(annotations_type_0_item)

        else:
            annotations = self.annotations

        audio: Union[None, Unset, dict[str, Any]]
        if isinstance(self.audio, Unset):
            audio = UNSET
        elif isinstance(self.audio, ChatCompletionAudio):
            audio = self.audio.to_dict()
        else:
            audio = self.audio

        function_call: Union[None, Unset, dict[str, Any]]
        if isinstance(self.function_call, Unset):
            function_call = UNSET
        elif isinstance(self.function_call, FunctionCall):
            function_call = self.function_call.to_dict()
        else:
            function_call = self.function_call

        tool_calls: Union[None, Unset, list[dict[str, Any]]]
        if isinstance(self.tool_calls, Unset):
            tool_calls = UNSET
        elif isinstance(self.tool_calls, list):
            tool_calls = []
            for tool_calls_type_0_item_data in self.tool_calls:
                tool_calls_type_0_item = tool_calls_type_0_item_data.to_dict()
                tool_calls.append(tool_calls_type_0_item)

        else:
            tool_calls = self.tool_calls

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "role": role,
            }
        )
        if content is not UNSET:
            field_dict["content"] = content
        if refusal is not UNSET:
            field_dict["refusal"] = refusal
        if annotations is not UNSET:
            field_dict["annotations"] = annotations
        if audio is not UNSET:
            field_dict["audio"] = audio
        if function_call is not UNSET:
            field_dict["function_call"] = function_call
        if tool_calls is not UNSET:
            field_dict["tool_calls"] = tool_calls

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.annotation import Annotation
        from ..models.chat_completion_audio import ChatCompletionAudio
        from ..models.chat_completion_message_tool_call import ChatCompletionMessageToolCall
        from ..models.function_call import FunctionCall

        d = dict(src_dict)
        role = cast(Literal["assistant"], d.pop("role"))
        if role != "assistant":
            raise ValueError(f"role must match const 'assistant', got '{role}'")

        def _parse_content(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        content = _parse_content(d.pop("content", UNSET))

        def _parse_refusal(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        refusal = _parse_refusal(d.pop("refusal", UNSET))

        def _parse_annotations(data: object) -> Union[None, Unset, list["Annotation"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                annotations_type_0 = []
                _annotations_type_0 = data
                for annotations_type_0_item_data in _annotations_type_0:
                    annotations_type_0_item = Annotation.from_dict(annotations_type_0_item_data)

                    annotations_type_0.append(annotations_type_0_item)

                return annotations_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["Annotation"]], data)

        annotations = _parse_annotations(d.pop("annotations", UNSET))

        def _parse_audio(data: object) -> Union["ChatCompletionAudio", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                audio_type_0 = ChatCompletionAudio.from_dict(data)

                return audio_type_0
            except:  # noqa: E722
                pass
            return cast(Union["ChatCompletionAudio", None, Unset], data)

        audio = _parse_audio(d.pop("audio", UNSET))

        def _parse_function_call(data: object) -> Union["FunctionCall", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                function_call_type_0 = FunctionCall.from_dict(data)

                return function_call_type_0
            except:  # noqa: E722
                pass
            return cast(Union["FunctionCall", None, Unset], data)

        function_call = _parse_function_call(d.pop("function_call", UNSET))

        def _parse_tool_calls(data: object) -> Union[None, Unset, list["ChatCompletionMessageToolCall"]]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                tool_calls_type_0 = []
                _tool_calls_type_0 = data
                for tool_calls_type_0_item_data in _tool_calls_type_0:
                    tool_calls_type_0_item = ChatCompletionMessageToolCall.from_dict(tool_calls_type_0_item_data)

                    tool_calls_type_0.append(tool_calls_type_0_item)

                return tool_calls_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, list["ChatCompletionMessageToolCall"]], data)

        tool_calls = _parse_tool_calls(d.pop("tool_calls", UNSET))

        chat_completion_message = cls(
            role=role,
            content=content,
            refusal=refusal,
            annotations=annotations,
            audio=audio,
            function_call=function_call,
            tool_calls=tool_calls,
        )

        chat_completion_message.additional_properties = d
        return chat_completion_message

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
