# Multimodal Myntra Fashion Search Engine with LanceDB Vector Database

Welcome to the GitHub repository for the Myntra Fashion Search Engine, a cutting-edge solution leveraging the power of [LanceDB](https://lancedb.com/) Vector Database to enable efficient and intuitive fashion searches. This project demonstrates the simplicity and effectiveness of using vector embeddings, specifically with OpenAI's CLIP model, to create a multimodal search engine capable of understanding and processing both text and image queries.

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
- PIL (Python Imaging Library)

### Installation

1. Clone the repository:
```
git clone https://github.com/ishandutta0098/lancedb-multimodal-myntra-fashion-search-engine.git
```
  
2. Navigate to the project directory and install the required dependencies:
```
cd lancedb-multimodal-myntra-fashion-search-engine
pip install -r requirements.txt
```

3. Download the dataset from Kaggle and store it in the input folder.
- [Myntra Fashion Product Dataset](https://www.kaggle.com/datasets/hiteshsuthar101/myntra-fashion-product-dataset)
This is how the `input` directory should look like:    
```
input
    |-images
    |   |-0.jpg
    |   |-2.jpg
    |   ..
    |   ..
    |- Fashion Dataset.csv
```

4. Run the Streamlit app:
```
streamlit run app.py
```


### Usage

Follow the on-screen instructions on the Streamlit app to perform searches. You can search using text queries or by uploading an image to find similar fashion items.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
