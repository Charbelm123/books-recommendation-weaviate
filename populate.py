import weaviate
import pandas as pd
from weaviate.util import get_valid_uuid
from uuid import uuid4
client = weaviate.connect_to_local()
print(client.is_connected())


# book_collection = client.collections.get(name="bookRecommendation")
books = pd.read_csv('books.csv')
for index , row in books.iterrows():
    if row.isnull().sum() > 0:
        books.drop(index, inplace=True)
print(books.shape)
i=0
try:
    for index, book in books.iterrows():
        i+=1
        properties ={
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
        row = book_collection.data.insert(uuid = id, properties = properties)
        print(index)
        if i==10:
            break
    

except Exception as e:
    print(e)
book_collection = client.collections.get(name="bookRecommendation")
for item in book_collection.iterator():
    print(item)
client.close()