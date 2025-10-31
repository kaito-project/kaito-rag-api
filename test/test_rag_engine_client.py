"""
Comprehensive tests for the RAG Engine API Client.

This module contains tests for all API endpoints in the RAG engine client,
focusing on sync methods for chat, index management, document management,
query, and monitoring functionality.
"""

import pytest
from unittest.mock import Mock, patch
import httpx
from http import HTTPStatus

from kaito_rag_engine_client.client import Client, AuthenticatedClient
from kaito_rag_engine_client.models.chat_request import ChatRequest
from kaito_rag_engine_client.models.chat_completion_response import ChatCompletionResponse
from kaito_rag_engine_client.models.index_request import IndexRequest
from kaito_rag_engine_client.models.document import Document
from kaito_rag_engine_client.models.delete_document_request import DeleteDocumentRequest
from kaito_rag_engine_client.models.update_document_request import UpdateDocumentRequest
from kaito_rag_engine_client.models.health_status import HealthStatus
from kaito_rag_engine_client.models.http_validation_error import HTTPValidationError

from kaito_rag_engine_client.api.chat import chat
from kaito_rag_engine_client.api.index import (
    create_index,
    delete_index,
    list_indexes,
    load_index,
    persist_index,
    delete_documents_in_index,
    list_documents_in_index,
    update_documents_in_index,
)
from kaito_rag_engine_client.api.monitoring import get_health, get_metrics


class TestClientSetup:
    """Test basic client setup and configuration."""

    def test_client_initialization(self):
        """Test basic client initialization."""
        client = Client(base_url="http://localhost:5789")
        assert client._base_url == "http://localhost:5789"
        assert client.raise_on_unexpected_status is False

    def test_authenticated_client_initialization(self):
        """Test authenticated client initialization."""
        auth_client = AuthenticatedClient(
            base_url="http://localhost:5789",
            token="test-token"
        )
        assert auth_client._base_url == "http://localhost:5789"
        assert auth_client.token == "test-token"
        assert auth_client.prefix == "Bearer"

    def test_client_with_headers(self):
        """Test client header customization."""
        client = Client(base_url="http://localhost:5789")
        client_with_headers = client.with_headers({"Custom-Header": "test-value"})
        assert "Custom-Header" in client_with_headers._headers
        assert client_with_headers._headers["Custom-Header"] == "test-value"

    def test_client_with_timeout(self):
        """Test client timeout configuration."""
        client = Client(base_url="http://localhost:5789")
        timeout = httpx.Timeout(30.0)
        client_with_timeout = client.with_timeout(timeout)
        assert client_with_timeout._timeout == timeout


class TestChatAPI:
    """Test chat completion API endpoints."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock client for testing."""
        return Client(base_url="http://localhost:5789")

    @pytest.fixture
    def sample_chat_request(self):
        """Create a sample chat request."""
        request = ChatRequest()
        request.additional_properties = {
            "model": "test-model",
            "messages": [
                {"role": "user", "content": "What is RAG?"}
            ],
            "temperature": 0.7,
            "max_tokens": 100
        }
        return request

    @pytest.fixture
    def sample_chat_response_data(self):
        """Create sample chat response data."""
        return {
            "id": "chatcmpl-123",
            "object": "chat.completion",
            "created": 1677652288,
            "model": "test-model",
            "choices": [
                {
                    "index": 0,
                    "message": {
                        "role": "assistant",
                        "content": "RAG stands for Retrieval-Augmented Generation."
                    },
                    "finish_reason": "stop"
                }
            ],
            "usage": {
                "prompt_tokens": 10,
                "completion_tokens": 15,
                "total_tokens": 25
            }
        }

    @patch('httpx.Client.request')
    def test_chat_sync_successful_response(self, mock_request, mock_client, sample_chat_request, sample_chat_response_data):
        """Test successful chat completion request."""
        # Mock successful response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_chat_response_data
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        # Execute the request
        response = chat.sync_detailed(client=mock_client, body=sample_chat_request)

        # Verify the request was made correctly
        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]["method"] == "post"
        assert call_args[1]["url"] == "/v1/chat/completions"
        assert "json" in call_args[1]

        # Verify response
        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.parsed, ChatCompletionResponse)

    @patch('httpx.Client.request')
    def test_chat_sync_validation_error(self, mock_request, mock_client, sample_chat_request):
        """Test chat completion with validation error."""
        # Mock validation error response
        mock_response = Mock()
        mock_response.status_code = 422
        mock_response.json.return_value = {
            "detail": [
                {
                    "loc": ["body", "messages"],
                    "msg": "field required",
                    "type": "value_error.missing"
                }
            ]
        }
        mock_response.content = b"validation error"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = chat.sync_detailed(client=mock_client, body=sample_chat_request)

        assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY
        assert isinstance(response.parsed, HTTPValidationError)

    @patch('httpx.Client.request')
    def test_chat_sync_convenience_method(self, mock_request, mock_client, sample_chat_request, sample_chat_response_data):
        """Test chat sync convenience method."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_chat_response_data
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        result = chat.sync(client=mock_client, body=sample_chat_request)

        assert isinstance(result, ChatCompletionResponse)


class TestIndexManagementAPI:
    """Test index management API endpoints."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock client for testing."""
        return Client(base_url="http://localhost:5789")

    @pytest.fixture
    def sample_index_request(self):
        """Create a sample index request."""
        document = Document(
            doc_id="test-doc-1",
            text="Sample document text",
            metadata={"author": "test-author"}
        )
        return IndexRequest(
            index_name="test-index",
            documents=[document]
        )

    @pytest.fixture
    def sample_document_response_data(self):
        """Create sample document response data."""
        return [
            {
                "doc_id": "test-doc-1",
                "text": "Sample document text",
                "hash_value": None,
                "metadata": {"author": "test-author"},
                "is_truncated": False
            }
        ]

    @patch('httpx.Client.request')
    def test_create_index_sync(self, mock_request, mock_client, sample_index_request, sample_document_response_data):
        """Test create index endpoint."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = sample_document_response_data
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = create_index.sync_detailed(client=mock_client, body=sample_index_request)

        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]["method"] == "post"
        assert call_args[1]["url"] == "/index"

        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.parsed, list)

    @patch('httpx.Client.request')
    def test_delete_index_sync(self, mock_request, mock_client):
        """Test delete index endpoint."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Index deleted successfully"}
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = delete_index.sync_detailed(client=mock_client, index_name="test-index")

        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]["method"] == "delete"
        assert "/indexes/test-index" in call_args[1]["url"]

        assert response.status_code == HTTPStatus.OK

    @patch('httpx.Client.request')
    def test_list_indexes_sync(self, mock_request, mock_client):
        """Test list indexes endpoint."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = ["index1", "index2", "test-index"]
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = list_indexes.sync_detailed(client=mock_client)

        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]["method"] == "get"
        assert call_args[1]["url"] == "/indexes"

        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.parsed, list)

    @patch('httpx.Client.request')
    def test_load_index_sync(self, mock_request, mock_client):
        """Test load index endpoint."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Index loaded successfully"}
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = load_index.sync_detailed(
            client=mock_client,
            index_name="test-index",
            path="/path/to/index"
        )

        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]["method"] == "post"
        assert "/load/test-index" in call_args[1]["url"]

        assert response.status_code == HTTPStatus.OK

    @patch('httpx.Client.request')
    def test_persist_index_sync(self, mock_request, mock_client):
        """Test persist index endpoint."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"message": "Index persisted successfully"}
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = persist_index.sync_detailed(
            client=mock_client,
            index_name="test-index",
            path="/path/to/persist"
        )

        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]["method"] == "post"
        assert "/persist/test-index" in call_args[1]["url"]

        assert response.status_code == HTTPStatus.OK


class TestDocumentManagementAPI:
    """Test document management API endpoints."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock client for testing."""
        return Client(base_url="http://localhost:5789")

    @pytest.fixture
    def sample_delete_request(self):
        """Create a sample delete document request."""
        return DeleteDocumentRequest(
            doc_ids=["doc1", "doc2"]
        )

    @pytest.fixture
    def sample_update_request(self):
        """Create a sample update document request."""
        document = Document(
            doc_id="doc1",
            text="Updated text",
            metadata={"updated": True}
        )
        return UpdateDocumentRequest(
            documents=[document]
        )

    @patch('httpx.Client.request')
    def test_list_documents_in_index_sync(self, mock_request, mock_client):
        """Test list documents in index endpoint."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "documents": [
                {"doc_id": "doc1", "text": "Sample text 1"},
                {"doc_id": "doc2", "text": "Sample text 2"}
            ],
            "count": 2,
            "total_items": 2
        }
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = list_documents_in_index.sync_detailed(
            client=mock_client,
            index_name="test-index",
            limit=10,
            offset=0
        )

        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]["method"] == "get"
        assert "/indexes/test-index/documents" in call_args[1]["url"]

        assert response.status_code == HTTPStatus.OK

    @patch('httpx.Client.request')
    def test_delete_documents_in_index_sync(self, mock_request, mock_client, sample_delete_request):
        """Test delete documents in index endpoint."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "deleted_doc_ids": ["doc1", "doc2"],
            "not_found_doc_ids": []
        }
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = delete_documents_in_index.sync_detailed(
            client=mock_client,
            index_name="test-index",
            body=sample_delete_request
        )

        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]["method"] == "post"
        assert "/indexes/test-index/documents/delete" in call_args[1]["url"]

        assert response.status_code == HTTPStatus.OK

    @patch('httpx.Client.request')
    def test_update_documents_in_index_sync(self, mock_request, mock_client, sample_update_request):
        """Test update documents in index endpoint."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "updated_documents": [
                {"doc_id": "doc1", "text": "Updated text", "metadata": {"updated": True}}
            ],
            "unchanged_documents": [],
            "not_found_documents": []
        }
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = update_documents_in_index.sync_detailed(
            client=mock_client,
            index_name="test-index",
            body=sample_update_request
        )

        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]["method"] == "post"
        assert "/indexes/test-index/documents" in call_args[1]["url"]

        assert response.status_code == HTTPStatus.OK


class TestMonitoringAPI:
    """Test monitoring API endpoints."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock client for testing."""
        return Client(base_url="http://localhost:5789")

    @patch('httpx.Client.request')
    def test_get_health_sync(self, mock_request, mock_client):
        """Test health check endpoint."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "healthy",
            "timestamp": "2025-10-28T12:00:00Z",
            "version": "1.0.0"
        }
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = get_health.sync_detailed(client=mock_client)

        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]["method"] == "get"
        assert call_args[1]["url"] == "/health"

        assert response.status_code == HTTPStatus.OK
        assert isinstance(response.parsed, HealthStatus)

    @patch('httpx.Client.request')
    def test_get_health_sync_convenience_method(self, mock_request, mock_client):
        """Test health check sync convenience method."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "status": "healthy",
            "timestamp": "2025-10-28T12:00:00Z"
        }
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        result = get_health.sync(client=mock_client)

        assert isinstance(result, HealthStatus)

    @patch('httpx.Client.request')
    def test_get_metrics_sync(self, mock_request, mock_client):
        """Test metrics endpoint."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.content = b"# HELP requests_total Total number of requests\n# TYPE requests_total counter\nrequests_total 42\n"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = get_metrics.sync_detailed(client=mock_client)

        mock_request.assert_called_once()
        call_args = mock_request.call_args
        assert call_args[1]["method"] == "get"
        assert call_args[1]["url"] == "/metrics"

        assert response.status_code == HTTPStatus.OK


class TestErrorHandling:
    """Test error handling scenarios across all endpoints."""

    @pytest.fixture
    def mock_client(self):
        """Create a mock client with raise_on_unexpected_status=True."""
        return Client(base_url="http://localhost:5789", raise_on_unexpected_status=True)

    @patch('httpx.Client.request')
    def test_unexpected_status_raises_error(self, mock_request, mock_client):
        """Test that unexpected status codes raise errors when configured."""
        from kaito_rag_engine_client.errors import UnexpectedStatus
        
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.content = b"Internal Server Error"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        chat_request = ChatRequest()
        
        with pytest.raises(UnexpectedStatus):
            chat.sync_detailed(client=mock_client, body=chat_request)

    @patch('httpx.Client.request')
    def test_timeout_handling(self, mock_request):
        """Test timeout exception handling."""
        client = Client(base_url="http://localhost:5789", timeout=httpx.Timeout(1.0))
        mock_request.side_effect = httpx.TimeoutException("Request timed out")

        chat_request = ChatRequest()
        
        with pytest.raises(httpx.TimeoutException):
            chat.sync_detailed(client=client, body=chat_request)

    @patch('httpx.Client.request')
    def test_connection_error_handling(self, mock_request):
        """Test connection error handling."""
        client = Client(base_url="http://localhost:5789")
        mock_request.side_effect = httpx.ConnectError("Connection failed")

        chat_request = ChatRequest()
        
        with pytest.raises(httpx.ConnectError):
            chat.sync_detailed(client=client, body=chat_request)


class TestAuthenticatedEndpoints:
    """Test endpoints that require authentication."""

    @pytest.fixture
    def auth_client(self):
        """Create an authenticated client."""
        return AuthenticatedClient(
            base_url="http://localhost:5789",
            token="test-auth-token"
        )

    @patch('httpx.Client.request')
    def test_authenticated_request_includes_auth_header(self, mock_request, auth_client):
        """Test that authenticated requests include proper authorization headers."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = ["index1", "index2"]
        mock_response.content = b"response content"
        mock_response.headers = {}
        mock_request.return_value = mock_response

        response = list_indexes.sync_detailed(client=auth_client)

        # Verify the client was configured with auth headers
        httpx_client = auth_client.get_httpx_client()
        assert "Authorization" in httpx_client.headers
        assert httpx_client.headers["Authorization"] == "Bearer test-auth-token"

        assert response.status_code == HTTPStatus.OK


if __name__ == "__main__":
    pytest.main([__file__])
