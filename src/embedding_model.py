from typing import Any

from lancedb.embeddings import EmbeddingFunctionRegistry


def register_model(model_name: str) -> Any:
    """
    Register a model with the given name using LanceDB's EmbeddingFunctionRegistry.

    Args:
        model_name (str): The name of the model to register.

    Returns:
        model: The registered model instance.

    Usage:
    >>> model = register_model("open-clip")
    """
    registry = EmbeddingFunctionRegistry.get_instance()
    model = registry.get(model_name).create()
    return model
