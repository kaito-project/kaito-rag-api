from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.query_request_llm_params_type_0 import QueryRequestLlmParamsType0
    from ..models.query_request_rerank_params_type_0 import QueryRequestRerankParamsType0


T = TypeVar("T", bound="QueryRequest")


@_attrs_define
class QueryRequest:
    """
    Attributes:
        index_name (str):
        query (str):
        top_k (Union[Unset, int]):  Default: 5.
        llm_params (Union['QueryRequestLlmParamsType0', None, Unset]): Optional parameters for the language model, e.g.,
            temperature, top_p
        rerank_params (Union['QueryRequestRerankParamsType0', None, Unset]): Experimental: Optional parameters for
            reranking. Only 'top_n' and 'choice_batch_size' are supported.
    """

    index_name: str
    query: str
    top_k: Union[Unset, int] = 5
    llm_params: Union["QueryRequestLlmParamsType0", None, Unset] = UNSET
    rerank_params: Union["QueryRequestRerankParamsType0", None, Unset] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.query_request_llm_params_type_0 import QueryRequestLlmParamsType0
        from ..models.query_request_rerank_params_type_0 import QueryRequestRerankParamsType0

        index_name = self.index_name

        query = self.query

        top_k = self.top_k

        llm_params: Union[None, Unset, dict[str, Any]]
        if isinstance(self.llm_params, Unset):
            llm_params = UNSET
        elif isinstance(self.llm_params, QueryRequestLlmParamsType0):
            llm_params = self.llm_params.to_dict()
        else:
            llm_params = self.llm_params

        rerank_params: Union[None, Unset, dict[str, Any]]
        if isinstance(self.rerank_params, Unset):
            rerank_params = UNSET
        elif isinstance(self.rerank_params, QueryRequestRerankParamsType0):
            rerank_params = self.rerank_params.to_dict()
        else:
            rerank_params = self.rerank_params

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "index_name": index_name,
                "query": query,
            }
        )
        if top_k is not UNSET:
            field_dict["top_k"] = top_k
        if llm_params is not UNSET:
            field_dict["llm_params"] = llm_params
        if rerank_params is not UNSET:
            field_dict["rerank_params"] = rerank_params

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_request_llm_params_type_0 import QueryRequestLlmParamsType0
        from ..models.query_request_rerank_params_type_0 import QueryRequestRerankParamsType0

        d = dict(src_dict)
        index_name = d.pop("index_name")

        query = d.pop("query")

        top_k = d.pop("top_k", UNSET)

        def _parse_llm_params(data: object) -> Union["QueryRequestLlmParamsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                llm_params_type_0 = QueryRequestLlmParamsType0.from_dict(data)

                return llm_params_type_0
            except:  # noqa: E722
                pass
            return cast(Union["QueryRequestLlmParamsType0", None, Unset], data)

        llm_params = _parse_llm_params(d.pop("llm_params", UNSET))

        def _parse_rerank_params(data: object) -> Union["QueryRequestRerankParamsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                rerank_params_type_0 = QueryRequestRerankParamsType0.from_dict(data)

                return rerank_params_type_0
            except:  # noqa: E722
                pass
            return cast(Union["QueryRequestRerankParamsType0", None, Unset], data)

        rerank_params = _parse_rerank_params(d.pop("rerank_params", UNSET))

        query_request = cls(
            index_name=index_name,
            query=query,
            top_k=top_k,
            llm_params=llm_params,
            rerank_params=rerank_params,
        )

        query_request.additional_properties = d
        return query_request

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
