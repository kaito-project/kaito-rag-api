from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.node_with_score import NodeWithScore


T = TypeVar("T", bound="RetrieveResponse")


@_attrs_define
class RetrieveResponse:
    """
    Attributes:
        query (str): The query used for retrieve
        results (list[NodeWithScore]): List of retrieved documents with scores
        count (int): Number of retrieved documents
    """

    query: str
    results: list[NodeWithScore]
    count: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        count = self.count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "results": results,
                "count": count,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.node_with_score import NodeWithScore

        d = dict(src_dict)
        query = d.pop("query")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = NodeWithScore.from_dict(results_item_data)

            results.append(results_item)

        count = d.pop("count")

        retrieve_response = cls(
            query=query,
            results=results,
            count=count,
        )

        retrieve_response.additional_properties = d
        return retrieve_response

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
