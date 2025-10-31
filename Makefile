OPEN_API_SPEC := ./openapi.json

.PHONY: install-openapi-generator
install-openapi-generator:
	pip install openapi-python-client

.PHONY: generate-client
generate-client: install-openapi-generator
	openapi-python-client generate --path $(OPEN_API_SPEC) --meta=setup --overwrite
	rm -rf ./src/kaito_rag_engine_client/*
	mv ./kaito-rag-engine-client/kaito_rag_engine_client/* ./src/kaito_rag_engine_client/
	rm -rf ./kaito-rag-engine-client
