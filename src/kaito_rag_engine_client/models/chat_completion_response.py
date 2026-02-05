from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, Literal, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.chat_completion_response_service_tier_type_0 import ChatCompletionResponseServiceTierType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.choice import Choice
    from ..models.completion_usage import CompletionUsage
    from ..models.node_with_score import NodeWithScore


T = TypeVar("T", bound="ChatCompletionResponse")


@_attrs_define
class ChatCompletionResponse:
    """
    Attributes:
        id (str):
        choices (list[Choice]):
        created (int):
        model (str):
        object_ (Literal['chat.completion']):
        service_tier (ChatCompletionResponseServiceTierType0 | None | Unset):
        system_fingerprint (None | str | Unset):
        usage (CompletionUsage | None | Unset):
        source_nodes (list[NodeWithScore] | None | Unset):
    """

    id: str
    choices: list[Choice]
    created: int
    model: str
    object_: Literal["chat.completion"]
    service_tier: ChatCompletionResponseServiceTierType0 | None | Unset = UNSET
    system_fingerprint: None | str | Unset = UNSET
    usage: CompletionUsage | None | Unset = UNSET
    source_nodes: list[NodeWithScore] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.completion_usage import CompletionUsage

        id = self.id

        choices = []
        for choices_item_data in self.choices:
            choices_item = choices_item_data.to_dict()
            choices.append(choices_item)

        created = self.created

        model = self.model

        object_ = self.object_

        service_tier: None | str | Unset
        if isinstance(self.service_tier, Unset):
            service_tier = UNSET
        elif isinstance(self.service_tier, ChatCompletionResponseServiceTierType0):
            service_tier = self.service_tier.value
        else:
            service_tier = self.service_tier

        system_fingerprint: None | str | Unset
        if isinstance(self.system_fingerprint, Unset):
            system_fingerprint = UNSET
        else:
            system_fingerprint = self.system_fingerprint

        usage: dict[str, Any] | None | Unset
        if isinstance(self.usage, Unset):
            usage = UNSET
        elif isinstance(self.usage, CompletionUsage):
            usage = self.usage.to_dict()
        else:
            usage = self.usage

        source_nodes: list[dict[str, Any]] | None | Unset
        if isinstance(self.source_nodes, Unset):
            source_nodes = UNSET
        elif isinstance(self.source_nodes, list):
            source_nodes = []
            for source_nodes_type_0_item_data in self.source_nodes:
                source_nodes_type_0_item = source_nodes_type_0_item_data.to_dict()
                source_nodes.append(source_nodes_type_0_item)

        else:
            source_nodes = self.source_nodes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "choices": choices,
                "created": created,
                "model": model,
                "object": object_,
            }
        )
        if service_tier is not UNSET:
            field_dict["service_tier"] = service_tier
        if system_fingerprint is not UNSET:
            field_dict["system_fingerprint"] = system_fingerprint
        if usage is not UNSET:
            field_dict["usage"] = usage
        if source_nodes is not UNSET:
            field_dict["source_nodes"] = source_nodes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.choice import Choice
        from ..models.completion_usage import CompletionUsage
        from ..models.node_with_score import NodeWithScore

        d = dict(src_dict)
        id = d.pop("id")

        choices = []
        _choices = d.pop("choices")
        for choices_item_data in _choices:
            choices_item = Choice.from_dict(choices_item_data)

            choices.append(choices_item)

        created = d.pop("created")

        model = d.pop("model")

        object_ = cast(Literal["chat.completion"], d.pop("object"))
        if object_ != "chat.completion":
            raise ValueError(f"object must match const 'chat.completion', got '{object_}'")

        def _parse_service_tier(data: object) -> ChatCompletionResponseServiceTierType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                service_tier_type_0 = ChatCompletionResponseServiceTierType0(data)

                return service_tier_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(ChatCompletionResponseServiceTierType0 | None | Unset, data)

        service_tier = _parse_service_tier(d.pop("service_tier", UNSET))

        def _parse_system_fingerprint(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        system_fingerprint = _parse_system_fingerprint(d.pop("system_fingerprint", UNSET))

        def _parse_usage(data: object) -> CompletionUsage | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                usage_type_0 = CompletionUsage.from_dict(data)

                return usage_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CompletionUsage | None | Unset, data)

        usage = _parse_usage(d.pop("usage", UNSET))

        def _parse_source_nodes(data: object) -> list[NodeWithScore] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                source_nodes_type_0 = []
                _source_nodes_type_0 = data
                for source_nodes_type_0_item_data in _source_nodes_type_0:
                    source_nodes_type_0_item = NodeWithScore.from_dict(source_nodes_type_0_item_data)

                    source_nodes_type_0.append(source_nodes_type_0_item)

                return source_nodes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NodeWithScore] | None | Unset, data)

        source_nodes = _parse_source_nodes(d.pop("source_nodes", UNSET))

        chat_completion_response = cls(
            id=id,
            choices=choices,
            created=created,
            model=model,
            object_=object_,
            service_tier=service_tier,
            system_fingerprint=system_fingerprint,
            usage=usage,
            source_nodes=source_nodes,
        )

        chat_completion_response.additional_properties = d
        return chat_completion_response

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
