# KAITO RAG Engine Client

[![PyPI version](https://img.shields.io/pypi/v/kaito-rag-client)](https://pypi.org/project/kaito-rag-client/)
[![Python Support](https://img.shields.io/pypi/pyversions/kaito-rag-client)](https://pypi.org/project/kaito-rag-client/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A Python client library for interacting with the [KAITO RAGEngine](https://kaito-project.github.io/kaito/docs/rag-api/) API. This client is generated using the [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) project against the [KAITO RAGEngine](https://kaito-project.github.io/kaito/docs/rag/) OpenAPI spec.

## Client Generation
The OpenAPI spec for the KAITO RAGEngine is generated from the FastAPI service the RAGEngine runs. To regenerate this client, first download the openapi.json file from a running RAGEngine Service at <RAG_Engine_Service_Endpoint>/openapi.json. Save the file into the repo and run `make generate-client`

## About KAITO

[KAITO (Kubernetes AI Toolchain Operator)](https://github.com/kaito-project/kaito) is an operator that automates AI/ML model inference workloads in Kubernetes clusters. The [RAGEngine](https://kaito-project.github.io/kaito/docs/rag/) component provides powerful Retrieval-Augmented Generation capabilities, combining large language models with information retrieval systems for enhanced, context-aware responses.

## Features

- 🔍 **Document Management**: Index, update, delete, and list documents
- 📊 **Index Operations**: Create, persist, load, and delete indexes  
- 🤖 **RAG Queries**: Perform retrieval-augmented generation queries
- 💬 **Chat Completions**: OpenAI-compatible chat interface with RAG support
- 🔧 **Code-Aware Splitting**: Support for code documents with language-specific chunking
- 🎯 **Metadata Filtering**: Filter documents by custom metadata
- 📖 **Comprehensive API**: Full coverage of KAITO RAGEngine REST API

## Integration with KAITO

This client is designed to work with [KAITO RAGEngine](https://kaito-project.github.io/kaito/docs/rag/) deployments. To set up a KAITO RAGEngine in your Kubernetes cluster:

1. Install KAITO operator in your cluster
2. Deploy a RAGEngine custom resource
3. Use the service endpoint as your `base_url`

For detailed setup instructions, see the [KAITO documentation](https://kaito-project.github.io/kaito/docs/rag/).


## Usage
For sync usage, you need to create a Client and pass it into the desired api's as follows:

```python
from kaito_rag_engine_client import Client
from kaito_rag_engine_client.api.chat import chat
from kaito_rag_engine_client.models import IndexRequest, Document, UpdateDocumentRequest, DeleteDocumentRequest, ChatRequest
from kaito_rag_engine_client.api.index import list_indexes, create_index, delete_index, list_documents_in_index, delete_documents_in_index, update_documents_in_index, persist_index, load_index

client = Client(base_url="http://api.example.com")

# List all indexes
indexes = list_indexes.sync(client=client)

#Create Index Request
resp = create_index.sync(client=client,body=IndexRequest(
    index_name="test_index",
    documents=[
        Document(
            text="Sample document text",
            metadata={"source": "unit_test"}
        )
    ]
))

# Delete Index Request
delete_resp = delete_index.sync(client=client, index_name="test_index")

# Persist Index Request
persist_index_resp = persist_index.sync(
    client=client,
    index_name="test_index"
)

# Load Index Request
load_index_resp = load_index.sync(
    client=client,
    index_name="test_index",
    overwrite=True
)

# List Documents In Index Request
list_resp = list_documents_in_index.sync(client=client, index_name="test_index")

# Update a Documents text
test_doc = list_resp.documents[0]
test_doc.text = "Updated document text"

# Update Documents Request
update_resp = update_documents_in_index.sync(
    client=client,
    index_name="test_index",
    body=UpdateDocumentRequest(
        documents=[
            test_doc
        ]
    )
)

# Delete Documents Request
delete_doc_resp = delete_documents_in_index.sync(
    client=client,
    index_name="test_index",
    body=DeleteDocumentRequest(
        doc_ids=[
            test_doc.doc_id
        ]
    )
)

# Chat Completions Request
chat_resp = chat.sync(client=client, body=ChatRequest.from_dict({
        "index_name": "test_index",
        "model": "<Your Model>",
        "messages": [{"role": "user", "content": "What can you tell me about AI?"}],
        "temperature": 0.7,
        "max_tokens": 100,
    }
))
```

Or do the same thing with an async version:

```python
from kaito_rag_engine_client import Client
from kaito_rag_engine_client.api.chat import chat
from kaito_rag_engine_client.models import IndexRequest, Document, UpdateDocumentRequest, DeleteDocumentRequest, ChatRequest
from kaito_rag_engine_client.api.index import list_indexes, create_index, delete_index, list_documents_in_index, delete_documents_in_index, update_documents_in_index, persist_index, load_index

client = Client(base_url="http://api.example.com")

# List all indexes
indexes = await list_indexes.asyncio(client=client)

#Create Index Request
resp = await create_index.asyncio(client=client,body=IndexRequest(
    index_name="test_index",
    documents=[
        Document(
            text="Sample document text",
            metadata={"source": "unit_test"}
        )
    ]
))

# Delete Index Request
delete_resp = await delete_index.asyncio(client=client, index_name="test_index")

# Persist Index Request
persist_index_resp = await persist_index.asyncio(
    client=client,
    index_name="test_index"
)

# Load Index Request
load_index_resp = await load_index.asyncio(
    client=client,
    index_name="test_index",
    overwrite=True
)

# List Documents In Index Request
list_resp = await list_documents_in_index.asyncio(client=client, index_name="test_index")

# Update a Documents text
test_doc = list_resp.documents[0]
test_doc.text = "Updated document text"

# Update Documents Request
update_resp = await update_documents_in_index.asyncio(
    client=client,
    index_name="test_index",
    body=UpdateDocumentRequest(
        documents=[
            test_doc
        ]
    )
)

# Delete Documents Request
delete_doc_resp = await delete_documents_in_index.asyncio(
    client=client,
    index_name="test_index",
    body=DeleteDocumentRequest(
        doc_ids=[
            test_doc.doc_id
        ]
    )
)

# Chat Completions Request
chat_resp = await chat.asyncio(client=client, body=ChatRequest.from_dict({
        "index_name": "test_index",
        "model": "<YOUR_MODEL>",
        "messages": [{"role": "user", "content": "What can you tell me about AI?"}],
        "temperature": 0.7,
        "max_tokens": 100,
    }
))
```

By default, when you're calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken",
    verify_ssl="/path/to/certificate_bundle.pem",
)
```

You can also disable certificate validation altogether, but beware that **this is a security risk**.

```python
client = AuthenticatedClient(
    base_url="https://internal_api.example.com", 
    token="SuperSecretToken", 
    verify_ssl=False
)
```

Things to know:
1. Every path/method combo becomes a Python module with four functions:
    1. `sync`: Blocking request that returns parsed data (if successful) or `None`
    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.
    1. `asyncio`: Like `sync` but async instead of blocking
    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking

1. All path/query params, and bodies become method arguments.
1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)
1. Any endpoint which did not have a tag will be in `kaito_rag_client.api.default`

## Advanced customizations

There are more settings on the generated `Client` class which let you control more runtime behavior, check out the docstring on that class for more info. You can also customize the underlying `httpx.Client` or `httpx.AsyncClient` (depending on your use-case):

```python
from kaito_rag_client import Client

def log_request(request):
    print(f"Request event hook: {request.method} {request.url} - Waiting for response")

def log_response(response):
    request = response.request
    print(f"Response event hook: {request.method} {request.url} - Status {response.status_code}")

client = Client(
    base_url="https://api.example.com",
    httpx_args={"event_hooks": {"request": [log_request], "response": [log_response]}},
)

# Or get the underlying httpx client to modify directly with client.get_httpx_client() or client.get_async_httpx_client()
```

You can even set the httpx client directly, but beware that this will override any existing settings (e.g., base_url):

```python
import httpx
from kaito_rag_engine_client import Client

client = Client(
    base_url="https://api.example.com",
)
# Note that base_url needs to be re-set, as would any shared cookies, headers, etc.
client.set_httpx_client(httpx.Client(base_url="https://api.example.com", proxies="http://localhost:8030"))
```

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Support

- 📖 [KAITO Documentation](https://kaito-project.github.io/kaito/docs/)
- 💬 [KAITO Slack Channel](https://cloud-native.slack.com/archives/C09B4EWCZ5M)
- 🐛 [GitHub Issues](https://github.com/kaito-project/kaito/issues)
- 📧 [KAITO Developers](mailto:kaito-dev@microsoft.com)