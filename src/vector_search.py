import lancedb
import argparse

from schema import Myntra, get_schema_by_name
import os

def run_vector_search(database, table_name, schema, search_query, limit=6, output_folder="output"):
    if os.path.exists(output_folder):
        for file in os.listdir(output_folder):
            os.remove(os.path.join(output_folder, file))
    else:
        os.makedirs(output_folder)

    db = lancedb.connect(database)
    table = db.open_table(table_name)
    rs = table.search(search_query).limit(limit).to_pydantic(schema)
    
    for i in range(limit):
        image_path = os.path.join(output_folder, f"image_{i}.jpg")
        rs[i].image.save(image_path, "JPEG")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Vector Search')
    parser.add_argument('--database', type=str, help='Path to the database')
    parser.add_argument('--table_name', type=str, help='Name of the table')
    parser.add_argument('--schema', type=str, help='Schema of the table', default="Myntra")
    parser.add_argument('--search_query', type=str, help='Search query')
    parser.add_argument('--limit', type=int, default=6, help='Limit the number of results (default: 6)')
    parser.add_argument('--output_folder', type=str, default="output", help='Output folder path')

    args = parser.parse_args()

    schema = get_schema_by_name(args.schema)
    if schema is None:
        raise ValueError(f"Unknown schema: {args.schema}")

    run_vector_search(args.database, args.table_name, args.schema, args.search_query, args.limit, args.output_folder)
