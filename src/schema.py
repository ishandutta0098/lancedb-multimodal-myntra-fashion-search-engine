from typing import Any

from lancedb.pydantic import LanceModel, Vector
from PIL import Image

from embedding_model import register_model

# Register the OpenAI CLIP model
clip = register_model("open-clip")


class Myntra(LanceModel):
    """
    Represents a Myntra Schema.

    Attributes:
        vector (Vector): The vector representation of the item.
        image_uri (str): The URI of the item's image.
    """

    vector: Vector(clip.ndims()) = clip.VectorField()
    image_uri: str = clip.SourceField()

    @property
    def image(self):
        return Image.open(self.image_uri)


# Function to map schema name to schema class
def get_schema_by_name(schema_name: str) -> Any:
    """
    Retrieves the schema object based on the given schema name.

    Args:
        schema_name (str): The name of the schema.

    Returns:
        object: The schema object corresponding to the given schema name, or None if not found.

    Usage:
    >>> schema = get_schema_by_name("Myntra")
    """
    schema_map = {
        "Myntra": Myntra,
    }
    return schema_map.get(schema_name)
