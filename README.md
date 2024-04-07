# Multimodal Myntra Fashion Search Engine with LanceDB Vector Database

<a target="_blank" href="https://lightning.ai/ishandutta0098/studios/multimodal-myntra-fashion-search-engine-with-lancedb">
  <img src="https://pl-bolts-doc-images.s3.us-east-2.amazonaws.com/app-2/studio-badge.svg" alt="Open In Studio"/>
</a>

Welcome to the GitHub repository for the Myntra Fashion Search Engine, a cutting-edge solution leveraging the power of [LanceDB](https://lancedb.com/) Vector Database to enable efficient and intuitive fashion searches. This project demonstrates the simplicity and effectiveness of using vector embeddings, specifically with OpenAI's CLIP model, to create a multimodal search engine capable of understanding and processing both text and image queries.

## Project Demo Video

https://github.com/ishandutta0098/lancedb-multimodal-myntra-fashion-search-engine/assets/47643789/193ddfa7-1a50-461f-90a4-438c1724a05b


## Resources
- [Blog](https://blog.lancedb.com/multimodal-myntra-fashion-search-engine-using-lancedb/)
- [Lightning Studio](https://lightning.ai/ishandutta0098/studios/multimodal-myntra-fashion-search-engine-with-lancedb)
- [Colab Notebook](https://colab.research.google.com/drive/1qnaNasUy6aJOcaUYw9lMX_s4SWWGq3jY?usp=sharing)
  
## Overview

The Myntra Fashion Search Engine is designed to simplify the process of finding fashion items by using LanceDB vector database. By converting images into searchable embeddings and integrating a user-friendly interface with Streamlit, this project showcases a seamless approach to building sophisticated search functionalities for fashion e-commerce platforms.

## Features

- **Vector Embeddings**: Utilizes OpenAI's CLIP model for converting images into searchable embeddings.
- **Multimodal Search**: Supports both text and image queries, allowing users to search for fashion items using either mode.
- **Simplified Schema Definition**: Streamlines the process of defining data schemas for LanceDB, making it easy to set up and manage the database.
- **Streamlit Integration**: Offers an intuitive and interactive user interface for search queries, built with Streamlit.
- **Flexible Search**: Capable of handling large volumes of data, providing fast and accurate search results.

## How It Works

The project is structured around a few key steps:

1. **Registering CLIP Embeddings**: Sets up the CLIP model within LanceDB for image to vector conversion.
2. **Creating Data Schema**: Defines the structure of the database table with vector and source fields.
3. **Creating and Managing Tables**: Demonstrates how to create and populate tables within LanceDB.
4. **Executing Searches**: Implements text and image search functionalities.
5. **Building a Streamlit App**: Provides a step-by-step guide to creating a Streamlit application for user interaction.

## Getting Started

To get started with the Myntra Fashion Search Engine, clone this repository and follow the instructions below.

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- LanceDB
- Streamlit
- open-clip-torch

### Installation

1. Clone the repository:
```
git clone https://github.com/ishandutta0098/lancedb-multimodal-myntra-fashion-search-engine.git
```
  
2. Navigate to the project directory and install the required dependencies using the `environment.yml` file:
```
cd lancedb-multimodal-myntra-fashion-search-engine

# Create the conda environment
conda env create -f environment.yml

# Activate the environment
conda activate lance-env
```

3. Download the dataset from Kaggle and store it in the input folder.
- [Myntra Fashion Product Dataset](https://www.kaggle.com/datasets/hiteshsuthar101/myntra-fashion-product-dataset)  
This is how the `input` directory should look like:      
```
input
    |-Images
    |   |-0.jpg
    |   |-2.jpg
    |   ..
    |   ..
    |- Fashion Dataset.csv
```

4. Create the Table:  
Pass the name of the database, name of the table and directory of the images in your dataset to create a table. 

```
python src/make_table.py --database "~/.lancedb" --table_name "myntra" --data_path "input/Images" 
```


5. Run the Streamlit app:
There are a number of arguments you can pass to the app. Here is the most basic run command. 
  
```
streamlit run src/app.py -- --table_name myntra
```
  
**Other options** - 
- `--search_query`: Text prompt or Image to search for
- `--limit_min`: Minimum limit for number of results
- `--limit_max`: Maximum limit for number of results
- `--limit_default`: Default limit for number of results

**Note:**  
To ensure the arguments get accepted by streamlit as script arguments, you need to add an additional `--` as a separator as shown above.
  
### Usage

Follow the on-screen instructions on the Streamlit app to perform searches. You can search using text queries or by uploading an image to find similar fashion items.

### Terminal Based Search
You can also run the vector search by calling the script `src/vector_search.py` instead of running the streamlit app. Here are the commands for text and image search. 


#### Syntax
```
python src/vector_search.py --database <database_name> --table_name <table> --schema <schema_name> --search_query <query> --output_folder <output folder>  
```
  
1. Text Search Example:  
```
python src/vector_search.py --database ~/.lancedb --table_name myntra --schema "Myntra" --search_query "White Kurta" --output_folder "output"            
```

2. Image Search Example:  
In this case pass the image path in the search query.
```
python src/vector_search.py --database ~/.lancedb --table_name myntra --schema "Myntra" --search_query "input/Images/34.jpg" --output_folder "output"
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.
