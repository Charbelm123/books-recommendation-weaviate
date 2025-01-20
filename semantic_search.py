import weaviate 


client = weaviate.connect_to_local(additional_config=weaviate.classes.init.AdditionalConfig(
    timeout=weaviate.classes.init.Timeout(init=2, query=200, insert=120) 
))
print(client.is_connected())

book_collection = client.collections.get(name="bookRecommendation")

client.collections.get(name="bookRecommendation", ).query
user_input = input("")

# response = book_collection.query.near_text(query = user_input, limit = 5) 
response = book_collection.query.hybrid(query = user_input, limit = 5) 
#  

response = (
    client.query
    .get("bookRecommendation", ["title", "_additionsl {spellCheck { change {corrected original} didYouMean location originalText}}"])
    .with_near_text(query=user_input)
    .do()
)


for book in response.objects:
    print(f"Book Title: {book.properties['title']}")
    print(f"Book Description: {book.properties['description']}")
    print('---\n\n\n')

client.close() 