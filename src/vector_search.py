import argparse
import os
from typing import Any
from PIL import Image

import lancedb

from schema import Myntra, get_schema_by_name


def run_vector_search(
    database: str,
    table_name: str,
    schema: Any,
    search_query: Any,
    limit: int = 6,
    output_folder: str = "output",
) -> None:
    """
    This function performs a vector search on the specified database and table using the provided search query.
    The search can be performed on either text or image data. The function retrieves the top 'limit' number of results
    and saves the corresponding images in the 'output_folder' directory. The function assumes if the search query ends 
    with '.jpg' or '.png', it is an image search, otherwise it is a text search.
    Args:
        database (str): The path to the database.
        table_name (str): The name of the table.
        schema (Schema): The schema to use for converting search results to Pydantic models.
        search_query (Any): The search query, can be text or image.
        limit (int, optional): The maximum number of results to return. Defaults to 6.
        output_folder (str, optional): The folder to save the output images. Defaults to "output".

    Returns:
        None

    Usage:
    >>> run_vector_search(database="~/.lancedb", table_name="myntra", schema=Myntra, search_query="Black Kurta")

    """

    # Create the output folder if it does not exist
    if os.path.exists(output_folder):
        for file in os.listdir(output_folder):
            os.remove(os.path.join(output_folder, file))
    else:
        os.makedirs(output_folder)

    # Connect to the lancedb database
    db = lancedb.connect(database)

    # Open the table
    table = db.open_table(table_name)

    # Check if the search query is an image or text
    try:
        if search_query.endswith(".jpg") or search_query.endswith(".png"):
            search_query = Image.open(search_query)
        else:
            search_query = search_query
    except AttributeError as e:
        if str(e) == "'JpegImageFile' object has no attribute 'endswith'":
            print("Running via Streamlit, search query is already an array so skipping opening image using Pillow")
        else:
            raise

    # Perform the vector search and retrieve the results
    rs = table.search(search_query).limit(limit).to_pydantic(schema)

    # Save the images to the output folder
    for i in range(limit):
        image_path = os.path.join(output_folder, f"image_{i}.jpg")
        rs[i].image.save(image_path, "JPEG")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Vector Search")
    parser.add_argument("--database", type=str, help="Path to the database")
    parser.add_argument("--table_name", type=str, help="Name of the table")
    parser.add_argument(
        "--schema", type=str, help="Schema of the table", default="Myntra"
    )
    parser.add_argument("--search_query", type=str, help="Search query")
    parser.add_argument(
        "--limit", type=int, default=6, help="Limit the number of results (default: 6)"
    )
    parser.add_argument(
        "--output_folder", type=str, default="output", help="Output folder path"
    )

    args = parser.parse_args()

    schema = get_schema_by_name(args.schema)
    if schema is None:
        raise ValueError(f"Unknown schema: {args.schema}")

    run_vector_search(
        args.database,
        args.table_name,
        schema,
        args.search_query,
        args.limit,
        args.output_folder,
    )
