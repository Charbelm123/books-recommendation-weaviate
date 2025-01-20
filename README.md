## Book Recommendation System
A vector database-powered book recommendation system built with Weaviate and Python.

# Description
This project implements a book recommendation system using Weaviate as the vector database. It processes book data with attributes like title, author, description, ratings etc. and enables semantic search and recommendations based on book content and metadata.

# Features
-Vector-based semantic search across book descriptions and metadata
-Book recommendation based on content similarity
-Support for filtering by:
  Categories
  Authors
  Ratings
  Publication year
  Number of pages
## Technology Stack
  -Weaviate vector database
  -Pandas for data processing
  -Docker for Weaviate deployment
  -Ollama for text embeddings
## Setup
1-Clone the repository
2-Install dependencies:
  pip install weaviate-client pandas
3-Start Weaviate:
  docker-compose up -d
4-Run the data import script:
  python populate.py
5-Run the search/recommendation system:
  python generative_search.py

## Data Structure
The system uses a book dataset with the following fields:

isbn13: ISBN-13 identifier
isbn10: ISBN-10 identifier
title: Book title
subtitle: Book subtitle
authors: Book authors
categories: Book categories/genres
thumbnail: Cover image URL
description: Book description
published_year: Year published
average_rating: Average user rating
num_pages: Number of pages
ratings_count: Number of ratings
