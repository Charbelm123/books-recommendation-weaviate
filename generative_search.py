import weaviate

client = weaviate.connect_to_local(additional_config=weaviate.classes.init.AdditionalConfig(
    timeout=weaviate.classes.init.Timeout(init=2, query=200, insert=120) 
))
print(client.is_connected())
print(client.get_meta())

book_collection = client.collections.get(name="bookRecommendation")

user_input = input("what book are you interested in? ")
response = book_collection.generate.near_text(
    query=user_input,
    single_prompt="Explain why this book might be interesting to read. The book's title is {title}, with a description: {description}, and is in the genre: {categories}.",
    limit=2,
)

print(f"Here are the recommended books for you based on your interest in {user_input}:")
for book in response.objects:
    print(f"Book Title: {book.properties['title']}")
    # print(f"Book Description: {book.properties['description']}")
    print(f"Generated output: {book.generated}")  # Note that the generated output is per object


    print('---\n\n\n')


client.close()

####  implement a generative feedback loop to improve the search results
###cache similar search querries
