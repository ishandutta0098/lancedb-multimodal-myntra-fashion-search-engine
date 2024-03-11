from PIL import Image
from lancedb.pydantic import LanceModel, Vector
from embedding_model import register_model

clip = register_model("open-clip")

class Myntra(LanceModel):
    vector: Vector(clip.ndims()) = clip.VectorField()
    image_uri: str = clip.SourceField()

    @property
    def image(self):
        return Image.open(self.image_uri)

# Function to map schema name to schema class
def get_schema_by_name(schema_name):
    schema_map = {
        "Myntra": Myntra,
    }
    return schema_map.get(schema_name)
