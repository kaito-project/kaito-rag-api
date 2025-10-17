# KAITO RAG Engine Client

[![PyPI version](https://img.shields.io/pypi/v/kaito-rag-client)](https://pypi.org/project/kaito-rag-client/)
[![Python Support](https://img.shields.io/pypi/pyversions/kaito-rag-client)](https://pypi.org/project/kaito-rag-client/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

A Python client library for interacting with the [KAITO RAGEngine](https://kaito-project.github.io/kaito/docs/rag-api/) API. This client provides a simple and intuitive interface for managing Retrieval-Augmented Generation (RAG) workflows using the KAITO project's RAG capabilities.

## About KAITO

[KAITO (Kubernetes AI Toolchain Operator)](https://github.com/kaito-project/kaito) is an operator that automates AI/ML model inference workloads in Kubernetes clusters. The RAGEngine component provides powerful Retrieval-Augmented Generation capabilities, combining large language models with information retrieval systems for enhanced, context-aware responses.

## Features

- 🔍 **Document Management**: Index, update, delete, and list documents
- 📊 **Index Operations**: Create, persist, load, and delete indexes  
- 🤖 **RAG Queries**: Perform retrieval-augmented generation queries
- 💬 **Chat Completions**: OpenAI-compatible chat interface with RAG support
- 🔧 **Code-Aware Splitting**: Support for code documents with language-specific chunking
- 🎯 **Metadata Filtering**: Filter documents by custom metadata
- 📖 **Comprehensive API**: Full coverage of KAITO RAGEngine REST API

## Installation

```bash
pip install kaito-rag-client
```

### Development Installation

```bash
git clone https://github.com/your-repo/kaito-rag-client.git
cd kaito-rag-client
pip install -e .
```

## Quick Start

```python
from kaito_rag_client import KAITORAGClient

# Initialize the client
client = KAITORAGClient(
    base_url="http://your-ragengine-service:80",
    model_name="your-model-name"
)

# Index some documents
documents = [
    {
        "text": "Retrieval Augmented Generation (RAG) is an architecture that augments the capabilities of a Large Language Model (LLM) by adding an information retrieval system.",
        "metadata": {"source": "documentation", "topic": "rag"}
    },
    {
        "text": "KAITO is a Kubernetes operator for AI/ML workloads, providing automated model deployment and scaling.",
        "metadata": {"source": "documentation", "topic": "kaito"}
    }
]

# Create an index with documents
result = client.index_documents("my_knowledge_base", documents)
print(f"Indexed {len(result)} documents")

# Query the index
response = client.query(
    index_name="my_knowledge_base",
    query="What is RAG?",
    llm_temperature=0.7,
    llm_max_tokens=200,
    top_k=3
)

print("Answer:", response["response"])
print("Sources:", len(response["source_nodes"]))

# Use chat completions with RAG
chat_response = client.chat(
    query="How does KAITO help with AI workloads?",
    index_name="my_knowledge_base",
    llm_temperature=0.7,
    llm_max_tokens=150
)

print("Chat Response:", chat_response["choices"][0]["message"]["content"])
```

## API Reference

### Client Initialization

```python
client = KAITORAGClient(base_url, model_name)
```

**Parameters:**
- `base_url` (str): The base URL of your KAITO RAGEngine service
- `model_name` (str): The name of the LLM model to use

### Document Management

#### Index Documents

```python
client.index_documents(index_name, documents)
```

Create or update an index with documents. Documents are automatically split into chunks for efficient retrieval.

**Parameters:**
- `index_name` (str): Name of the index
- `documents` (list): List of document dictionaries with `text` and optional `metadata`

**Example:**
```python
documents = [
    {
        "text": "Your document content here...",
        "metadata": {
            "author": "John Doe",
            "category": "technical",
            "split_type": "code",  # Optional: use code-aware splitting
            "language": "python"   # Required if split_type is "code"
        }
    }
]

result = client.index_documents("tech_docs", documents)
```

#### Update Documents

```python
client.update_documents(index_name, documents)
```

Update existing documents by their `doc_id`.

#### Delete Documents

```python
client.delete_documents(index_name, document_ids)
```

Delete documents by their IDs.

#### List Documents

```python
client.list_documents(index_name, metadata_filter, limit=10, offset=0)
```

Retrieve a paginated list of documents with optional metadata filtering.

**Example:**
```python
# List documents with specific metadata
docs = client.list_documents(
    index_name="tech_docs",
    metadata_filter={"category": "technical"},
    limit=20,
    offset=0
)
```

### Index Management

#### List Indexes

```python
client.list_indexes()
```

Get all available indexes.

#### Persist Index

```python
client.persist_index(index_name, path="/tmp")
```

Save an index to disk for persistence.

#### Load Index

```python
client.load_index(index_name, path="/tmp", overwrite=True)
```

Load a previously persisted index from disk.

#### Delete Index

```python
client.delete_index(index_name)
```

Permanently delete an index and all its documents.

### Querying and Chat

#### RAG Query

```python
client.query(index_name, query, llm_temperature, llm_max_tokens, top_k=5)
```

Perform a retrieval-augmented generation query.

**Parameters:**
- `index_name` (str): Name of the index to query
- `query` (str): The search query
- `llm_temperature` (float): Temperature for LLM generation (0.0-1.0)
- `llm_max_tokens` (int): Maximum tokens to generate
- `top_k` (int): Number of top documents to retrieve

#### Chat Completions

```python
client.chat(
    query,
    chat_history=None,
    index_name=None,
    llm_temperature=0.7,
    llm_max_tokens=-1,
    top_p=-1
)
```

OpenAI-compatible chat completions with optional RAG enhancement.

**Parameters:**
- `query` (str): The user's message
- `chat_history` (list, optional): Previous conversation messages
- `index_name` (str, optional): Index to use for RAG (if omitted, uses base LLM)
- `llm_temperature` (float): Generation temperature
- `llm_max_tokens` (int): Maximum tokens to generate (-1 for unlimited)
- `top_p` (float): Top-p sampling (-1 to disable, overrides temperature)

**Example with conversation history:**
```python
chat_history = [
    {"role": "user", "content": "What is KAITO?"},
    {"role": "assistant", "content": "KAITO is a Kubernetes AI Toolchain Operator..."}
]

response = client.chat(
    query="How does it handle model deployment?",
    chat_history=chat_history,
    index_name="kaito_docs",
    llm_temperature=0.7
)
```

## Advanced Features

### Code-Aware Document Splitting

For code documents, you can use specialized splitting that understands code structure:

```python
code_documents = [
    {
        "text": """
def calculate_fibonacci(n):
    if n <= 1:
        return n
    return calculate_fibonacci(n-1) + calculate_fibonacci(n-2)

# Example usage
result = calculate_fibonacci(10)
print(f"Fibonacci(10) = {result}")
        """,
        "metadata": {
            "split_type": "code",
            "language": "python",
            "file_name": "fibonacci.py"
        }
    }
]

client.index_documents("code_examples", code_documents)
```

### Metadata Filtering

Use metadata to organize and filter your documents:

```python
# Index documents with rich metadata
documents = [
    {
        "text": "Machine learning documentation...",
        "metadata": {
            "category": "ml",
            "difficulty": "beginner",
            "tags": ["supervised", "classification"]
        }
    }
]

client.index_documents("ml_docs", documents)

# Query with metadata filtering
docs = client.list_documents(
    index_name="ml_docs",
    metadata_filter={"category": "ml", "difficulty": "beginner"}
)
```

## Error Handling

The client raises `requests.HTTPError` for HTTP-related errors. Wrap your calls in try-catch blocks:

```python
try:
    result = client.index_documents("my_index", documents)
except requests.HTTPError as e:
    print(f"HTTP Error: {e}")
    print(f"Status Code: {e.response.status_code}")
    print(f"Response: {e.response.text}")
```

## Configuration

### Environment Variables

You can set default values using environment variables:

```bash
export KAITO_RAG_BASE_URL="http://my-ragengine:80"
export KAITO_RAG_MODEL_NAME="my-model"
```

```python
import os
from kaito_rag_client import KAITORAGClient

client = KAITORAGClient(
    base_url=os.getenv("KAITO_RAG_BASE_URL"),
    model_name=os.getenv("KAITO_RAG_MODEL_NAME")
)
```

## Testing

The project includes comprehensive tests using pytest:

```bash
# Install test dependencies
pip install -r test-requirements.txt

# Run tests
pytest kaito_rag_client/tests/ -v

# Run with coverage
pytest kaito_rag_client/tests/ --cov=kaito_rag_client --cov-report=html
```

## Examples

Check out the [examples](examples/) directory for complete usage examples:

- **Basic RAG Workflow**: Document indexing and querying
- **Chat Interface**: Building conversational AI with RAG
- **Code Documentation**: Indexing and searching code repositories
- **Multi-Index Management**: Working with multiple knowledge bases

## Integration with KAITO

This client is designed to work with [KAITO RAGEngine](https://kaito-project.github.io/kaito/docs/rag/) deployments. To set up a KAITO RAGEngine in your Kubernetes cluster:

1. Install KAITO operator in your cluster
2. Deploy a RAGEngine custom resource
3. Use the service endpoint as your `base_url`

For detailed setup instructions, see the [KAITO documentation](https://kaito-project.github.io/kaito/docs/rag/).

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests for new functionality
5. Run the test suite
6. Submit a pull request

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details.

## Support

- 📖 [KAITO Documentation](https://kaito-project.github.io/kaito/docs/)
- 💬 [KAITO Slack Channel](https://cloud-native.slack.com/archives/C09B4EWCZ5M)
- 🐛 [GitHub Issues](https://github.com/kaito-project/kaito/issues)
- 📧 [KAITO Developers](mailto:kaito-dev@microsoft.com)

## Related Projects

- [KAITO](https://github.com/kaito-project/kaito) - Kubernetes AI Toolchain Operator
- [LlamaIndex](https://github.com/run-llama/llama_index) - Data framework for LLM applications
- [FAISS](https://github.com/facebookresearch/faiss) - Vector similarity search library
