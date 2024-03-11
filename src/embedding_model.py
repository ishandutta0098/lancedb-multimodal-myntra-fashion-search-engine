from lancedb.embeddings import EmbeddingFunctionRegistry

def register_model(model_name):
    registry = EmbeddingFunctionRegistry.get_instance()
    model = registry.get(model_name).create()
    return model
