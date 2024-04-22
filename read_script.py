import chromadb
from langchain_community.embeddings import HuggingFaceEmbeddings

def filter_lines(input_text, query):
    filtered_lines = []
    for line in input_text:
        if query in line:
            filtered_lines.append(line.strip())
    return filtered_lines

# Initialize Chroma DB client
client = chromadb.PersistentClient(path="./db")
collection = client.get_collection(name="my_collection7")
from langchain_community.embeddings import HuggingFaceEmbeddings

# Initialize GPT4All embeddings
embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-large-en-v1.5")

# Get user input
query = input("Enter your query: ")

# Convert query to vector representation
query_vector = embeddings.embed_query(query)

# Query Chroma DB with the vector representation
results = collection.query(query_embeddings=query_vector, n_results=2 , include=["documents"])
# print(results)
# Print results
for result in results["documents"]:
    for i in result:
        split_strings = i.split('\n')
        # print(split_strings)
        filtered_lines = filter_lines(split_strings, query)
        if filtered_lines:  # Check if filtered lines list is not empty
                for line in filtered_lines:
                    print(line)
    

