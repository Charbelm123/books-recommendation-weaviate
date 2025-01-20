import weaviate
from weaviate.util import get_valid_uuid
from uuid import uuid4  
import pandas as pd
import json
client = weaviate.connect_to_local()
client.collections.delete(name='bookRecommendation2')
print(client.is_connected())


question = client.collections.create(
    name='bookRecommendation2',
    description='A collection of book recommendations',
    vectorizer_config=weaviate.classes.config.Configure.Vectorizer.text2vec_ollama(api_endpoint="http://host.docker.internal:11434",model="llama3.2:latest"),#
    # generative_config=weaviate.classes.config.Configure.Generative.ollama(api_endpoint="http://localhost:11434", model = "llama3.2:latest"),
    properties=[
        weaviate.classes.config.Property(name = 'isbn13', data_type = weaviate.classes.config.DataType.TEXT, skip_vectorization=True, tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
        weaviate.classes.config.Property(name = 'isbn10', data_type = weaviate.classes.config.DataType.TEXT, skip_vectorization=True,tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
        weaviate.classes.config.Property(name = 'title', data_type = weaviate.classes.config.DataType.TEXT,tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
        weaviate.classes.config.Property(name = 'subtitle', data_type = weaviate.classes.config.DataType.TEXT, skip_vectorization=True,tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
        weaviate.classes.config.Property(name = 'authors', data_type = weaviate.classes.config.DataType.TEXT,tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
        weaviate.classes.config.Property(name = 'categories', data_type = weaviate.classes.config.DataType.TEXT,tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
        weaviate.classes.config.Property(name = 'thumbnail', data_type = weaviate.classes.config.DataType.TEXT, skip_vectorization=True,tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
        weaviate.classes.config.Property(name = 'description', data_type = weaviate.classes.config.DataType.TEXT,tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
        weaviate.classes.config.Property(name = 'published_year', data_type = weaviate.classes.config.DataType.TEXT,tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
        weaviate.classes.config.Property(name = 'average_rating', data_type = weaviate.classes.config.DataType.TEXT,tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
        weaviate.classes.config.Property(name = 'num_pages', data_type = weaviate.classes.config.DataType.TEXT,tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
        weaviate.classes.config.Property(name = 'ratings_count', data_type = weaviate.classes.config.DataType.TEXT,tokenization=weaviate.classes.config.Tokenization.LOWERCASE),
    ]
)
print(client.collections.list_all().keys())


collection = client.collections.get(name='bookRecommendation')
books = pd.read_csv('books.csv')
for index , row in books.iterrows():
    if row.isnull().sum() > 0:
        books.drop(index, inplace=True)

print(books.shape)
print(books.info())
i=0
with collection.batch.fixed_size(1) as batch:
    for index, book in books.iterrows():
        i+=1
        print(index)
        weaviate_obj = {
            "isbn13": str(book.iloc[0]),
            "isbn10": book.iloc[1],
            "title": book.iloc[2],
            "subtitle": book.iloc[3],
            "authors": book.iloc[4],
            "categories": book.iloc[5],
            "thumbnail": book.iloc[6],
            "description": book.iloc[7],
            "published_year": str(book.iloc[8]),
            "average_rating":str(book.iloc[9]),
            "num_pages": str(book.iloc[10]),
            "ratings_count": str(book.iloc[11]),
        }
        id = get_valid_uuid(uuid4())
        batch.add_object(
            properties=weaviate_obj,
            uuid=id
            )
        break
        
      

if collection.batch.failed_objects:
    print("Failed objects:")
    for failed_obj in collection.batch.failed_objects:
        print(failed_obj)

for item in collection.iterator():
    print(item)

client.close()
