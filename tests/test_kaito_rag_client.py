# Copyright (c) KAITO authors.
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import json
import pytest
from unittest.mock import Mock, patch
import requests

from kaito_rag_client.src.kaito_rag_client import KAITORAGClient


class TestKAITORAGClient:
    """Test suite for KAITORAGClient"""

    @pytest.fixture
    def client(self):
        """Create a test client instance"""
        return KAITORAGClient(
            base_url="http://test-api.example.com",
            model_name="test-model"
        )

    @pytest.fixture
    def mock_response(self):
        """Create a mock response object"""
        mock_resp = Mock()
        mock_resp.json.return_value = {"status": "success", "data": "test_data"}
        mock_resp.raise_for_status.return_value = None
        return mock_resp

    def test_client_initialization(self):
        """Test client initialization with correct attributes"""
        client = KAITORAGClient("http://example.com", "gpt-4")
        
        assert client.base_url == "http://example.com"
        assert client.model_name == "gpt-4"
        assert client.headers == {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

    @patch('requests.post')
    def test_index_documents_success(self, mock_post, client, mock_response):
        """Test successful document indexing"""
        mock_post.return_value = mock_response
        
        documents = [
            {"text": "Document 1", "metadata": {"type": "text"}},
            {"text": "Document 2", "metadata": {"type": "text"}}
        ]
        
        result = client.index_documents("test_index", documents)
        
        mock_post.assert_called_once_with(
            "http://test-api.example.com/index",
            json={"index_name": "test_index", "documents": documents},
            headers=client.headers
        )
        assert result == {"status": "success", "data": "test_data"}

    @patch('requests.post')
    def test_index_documents_http_error(self, mock_post, client):
        """Test document indexing with HTTP error"""
        mock_resp = Mock()
        mock_resp.raise_for_status.side_effect = requests.HTTPError("404 Not Found")
        mock_post.return_value = mock_resp
        
        documents = [{"text": "Document 1"}]
        
        with pytest.raises(requests.HTTPError):
            client.index_documents("test_index", documents)

    @patch('requests.post')
    def test_query_success(self, mock_post, client, mock_response):
        """Test successful query"""
        mock_response.json.return_value = {
            "results": [{"text": "Result 1", "score": 0.9}],
            "query": "test query"
        }
        mock_post.return_value = mock_response
        
        result = client.query(
            index_name="test_index",
            query="test query",
            llm_temperature=0.7,
            llm_max_tokens=100,
            top_k=3
        )
        
        expected_payload = {
            "index_name": "test_index",
            "query": "test query",
            "top_k": 3,
            "llm_params": {
                "temperature": 0.7,
                "max_tokens": 100,
            },
        }
        
        mock_post.assert_called_once_with(
            "http://test-api.example.com/query",
            json=expected_payload,
            headers=client.headers
        )
        assert result["query"] == "test query"

    @patch('requests.post')
    def test_chat_without_index(self, mock_post, client, mock_response):
        """Test chat without index (base LLM)"""
        mock_response.json.return_value = {
            "choices": [{"message": {"content": "Test response"}}]
        }
        mock_post.return_value = mock_response
        
        client.chat(
            query="Hello",
            llm_temperature=0.5,
            llm_max_tokens=150
        )
        
        expected_payload = {
            "model": "test-model",
            "messages": [{"role": "user", "content": "Hello"}],
            "temperature": 0.5,
            "max_tokens": 150
        }
        
        mock_post.assert_called_once_with(
            "http://test-api.example.com/v1/chat/completions",
            json=expected_payload,
            headers=client.headers
        )

    @patch('requests.post')
    def test_chat_with_index(self, mock_post, client, mock_response):
        """Test chat with RAG index"""
        mock_post.return_value = mock_response
        
        chat_history = [
            {"role": "user", "content": "Previous question"},
            {"role": "assistant", "content": "Previous answer"}
        ]
        
        client.chat(
            query="Follow-up question",
            chat_history=chat_history,
            index_name="test_index",
            llm_temperature=0.8,
            llm_max_tokens=200
        )
        
        expected_messages = chat_history + [{"role": "user", "content": "Follow-up question"}]
        expected_payload = {
            "model": "test-model",
            "messages": expected_messages,
            "temperature": 0.8,
            "max_tokens": 200,
            "index_name": "test_index"
        }
        
        mock_post.assert_called_once_with(
            "http://test-api.example.com/v1/chat/completions",
            json=expected_payload,
            headers=client.headers
        )

    @patch('requests.post')
    def test_chat_with_top_p(self, mock_post, client, mock_response):
        """Test chat with top_p parameter (should remove temperature)"""
        mock_post.return_value = mock_response
        
        client.chat(
            query="Test query",
            top_p=0.9,
            llm_temperature=0.7  # This should be ignored when top_p is set
        )
        
        expected_payload = {
            "model": "test-model",
            "messages": [{"role": "user", "content": "Test query"}],
            "top_p": 0.9
            # Note: temperature should NOT be in the payload
        }
        
        mock_post.assert_called_once_with(
            "http://test-api.example.com/v1/chat/completions",
            json=expected_payload,
            headers=client.headers
        )

    @patch('requests.post')
    def test_update_documents(self, mock_post, client, mock_response):
        """Test updating documents"""
        mock_post.return_value = mock_response
        
        documents = [
            {"id": "doc1", "text": "Updated text 1", "metadata": {"updated": True}},
            {"id": "doc2", "text": "Updated text 2"}
        ]
        
        client.update_documents("test_index", documents)
        
        mock_post.assert_called_once_with(
            "http://test-api.example.com/indexes/test_index/documents",
            json={"documents": documents},
            headers=client.headers
        )

    @patch('requests.post')
    def test_delete_documents(self, mock_post, client, mock_response):
        """Test deleting documents"""
        mock_post.return_value = mock_response
        
        document_ids = ["doc1", "doc2", "doc3"]
        
        client.delete_documents("test_index", document_ids)
        
        mock_post.assert_called_once_with(
            "http://test-api.example.com/indexes/test_index/documents/delete",
            json={"doc_ids": document_ids},
            headers=client.headers
        )

    @patch('requests.get')
    def test_list_documents(self, mock_get, client, mock_response):
        """Test listing documents"""
        mock_response.json.return_value = {
            "documents": [{"id": "doc1", "text": "Document 1"}],
            "total": 1
        }
        mock_get.return_value = mock_response
        
        metadata_filter = {"type": "text"}
        
        result = client.list_documents(
            index_name="test_index",
            metadata_filter=metadata_filter,
            limit=20,
            offset=10
        )
        
        expected_params = {
            "limit": 20,
            "offset": 10,
            "metadata_filter": json.dumps(metadata_filter)
        }
        
        mock_get.assert_called_once_with(
            "http://test-api.example.com/indexes/test_index/documents",
            headers=client.headers,
            params=expected_params
        )
        assert result["total"] == 1

    @patch('requests.get')
    def test_list_documents_no_filter(self, mock_get, client, mock_response):
        """Test listing documents without metadata filter"""
        mock_get.return_value = mock_response
        
        client.list_documents(
            index_name="test_index",
            metadata_filter=None,
            limit=10,
            offset=0
        )
        
        expected_params = {
            "limit": 10,
            "offset": 0
        }
        
        mock_get.assert_called_once_with(
            "http://test-api.example.com/indexes/test_index/documents",
            headers=client.headers,
            params=expected_params
        )

    @patch('requests.get')
    def test_list_indexes(self, mock_get, client, mock_response):
        """Test listing all indexes"""
        mock_response.json.return_value = {
            "indexes": ["index1", "index2", "index3"]
        }
        mock_get.return_value = mock_response
        
        result = client.list_indexes()
        
        mock_get.assert_called_once_with(
            "http://test-api.example.com/indexes",
            headers=client.headers
        )
        assert "indexes" in result

    @patch('requests.post')
    def test_persist_index(self, mock_post, client, mock_response):
        """Test persisting an index"""
        mock_post.return_value = mock_response
        
        client.persist_index("test_index", "/custom/path")
        
        mock_post.assert_called_once_with(
            "http://test-api.example.com/persist/test_index",
            params={"path": "/custom/path"},
            headers=client.headers
        )

    @patch('requests.post')
    def test_persist_index_default_path(self, mock_post, client, mock_response):
        """Test persisting an index with default path"""
        mock_post.return_value = mock_response
        
        client.persist_index("test_index")
        
        mock_post.assert_called_once_with(
            "http://test-api.example.com/persist/test_index",
            params={"path": "/tmp"},
            headers=client.headers
        )

    @patch('requests.post')
    def test_load_index(self, mock_post, client, mock_response):
        """Test loading an index"""
        mock_post.return_value = mock_response
        
        client.load_index("test_index", "/custom/path", overwrite=False)
        
        mock_post.assert_called_once_with(
            "http://test-api.example.com/load/test_index",
            params={"path": "/custom/path", "overwrite": False},
            headers=client.headers
        )

    @patch('requests.post')
    def test_load_index_defaults(self, mock_post, client, mock_response):
        """Test loading an index with default parameters"""
        mock_post.return_value = mock_response
        
        client.load_index("test_index")
        
        mock_post.assert_called_once_with(
            "http://test-api.example.com/load/test_index",
            params={"path": "/tmp", "overwrite": True},
            headers=client.headers
        )

    @patch('requests.delete')
    def test_delete_index(self, mock_delete, client, mock_response):
        """Test deleting an index"""
        mock_delete.return_value = mock_response
        
        client.delete_index("test_index")
        
        mock_delete.assert_called_once_with(
            "http://test-api.example.com/indexes/test_index",
            headers=client.headers
        )

    @patch('requests.post')
    def test_http_error_handling(self, mock_post, client):
        """Test that HTTP errors are properly raised"""
        mock_resp = Mock()
        mock_resp.raise_for_status.side_effect = requests.HTTPError("500 Internal Server Error")
        mock_post.return_value = mock_resp
        
        with pytest.raises(requests.HTTPError):
            client.index_documents("test_index", [{"text": "test"}])

    def test_chat_parameter_validation(self, client):
        """Test chat method parameter handling edge cases"""
        with patch('requests.post') as mock_post:
            mock_resp = Mock()
            mock_resp.json.return_value = {"choices": []}
            mock_resp.raise_for_status.return_value = None
            mock_post.return_value = mock_resp
            
            # Test with llm_max_tokens = 0 (should not include max_tokens)
            client.chat("test", llm_max_tokens=0)
            
            call_args = mock_post.call_args
            payload = call_args[1]['json']
            assert 'max_tokens' not in payload
            
            # Test with llm_max_tokens = -1 (should not include max_tokens)
            client.chat("test", llm_max_tokens=-1)
            
            call_args = mock_post.call_args
            payload = call_args[1]['json']
            assert 'max_tokens' not in payload