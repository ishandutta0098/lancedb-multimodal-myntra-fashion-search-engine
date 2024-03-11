import lancedb
import pandas as pd
from pathlib import Path
from random import sample
import argparse

from schema import Myntra

def create_table(database, table_name, data_path, schema=Myntra, mode="overwrite"):

    # Connect to the lancedb database
    db = lancedb.connect(database)

    # Check if the table already exists in the database
    if table_name in db:
        print(f"Table {table_name} already exists in the database")
        table = db[table_name]

    # if it does not exist then create a new table
    else:   

        print(f"Creating table {table_name} in the database")

        # Create the table with the given schema
        table = db.create_table(table_name, schema=schema, mode=mode)

        # Define the Path of the images and obtain the Image uri
        p = Path(data_path).expanduser()
        uris = [str(f) for f in p.glob("*.jpg")]
        print(f"Found {len(uris)} images in {p}")
        
        # Sample 1000 images from the data 
        uris = sample(uris, 1000)

        # Add the data to the table
        print(f"Adding {len(uris)} images to the table")
        table.add(pd.DataFrame({"image_uri": uris}))
        print(f"Added {len(uris)} images to the table")
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a table in lancedb with Myntra data')
    parser.add_argument('database', help='Path to the lancedb database', default='path/to/database')
    parser.add_argument('table_name', help='Name of the table to be created', default='my_table')
    parser.add_argument('data_path', help='Path to the Myntra data images', default='path/to/data')
    args = parser.parse_args()

    create_table(args.database, args.table_name, args.data_path)
