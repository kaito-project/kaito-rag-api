from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="TopLogprob")


@_attrs_define
class TopLogprob:
    """
    Attributes:
        token (str):
        logprob (float):
        bytes_ (list[int] | None | Unset):
    """

    token: str
    logprob: float
    bytes_: list[int] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        token = self.token

        logprob = self.logprob

        bytes_: list[int] | None | Unset
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
            }
        )
        if bytes_ is not UNSET:
            field_dict["bytes"] = bytes_

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        token = d.pop("token")

        logprob = d.pop("logprob")

        def _parse_bytes_(data: object) -> list[int] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                bytes_type_0 = cast(list[int], data)

                return bytes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[int] | None | Unset, data)

        bytes_ = _parse_bytes_(d.pop("bytes", UNSET))

        top_logprob = cls(
            token=token,
            logprob=logprob,
            bytes_=bytes_,
        )

        top_logprob.additional_properties = d
        return top_logprob

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
