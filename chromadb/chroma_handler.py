# chroma_handler.py

import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions


# Create a ChromaDB client object with the specified settings.
client = chromadb.Client(
    Settings(
        persist_directory="db",
        chroma_db_impl="duckdb+parquet"
    )
)

# Get the named collection, or create a new one if it doesn't exist.
# Pass the encoder object as the embedding_function parameter.
# Initialize an embedding function for encoding text data as numeric vectors.
encoder = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-mpnet-base-v2")

collection_name = "memories"

try:
    collection = client.get_collection(name=collection_name, embedding_function=encoder)
    print(f"Collection {collection_name} found.")
except ValueError:
    print(f"Collection {collection_name} does not exist. Creating it...")
    collection = client.create_collection(name=collection_name, embedding_function=encoder)
    print(f"Collection {collection_name} created successfully.")


class ChromaDBHandler:

    @staticmethod
    def store(textdata, metadata, ids):
        """
        Stores new textdata, username, and ids in the ChromaDB collection.

        Args:
            textdata: list of strings, the text data to store.
            username: list of strings, the usernames associated with the text data.
            ids: list of strings or ints, the unique IDs associated with the text data.

        Returns:
            None.
        """
        # Store the new entry in the collection.
        collection.add(
            documents=textdata,
            metadatas=metadata,
            ids=ids
        )
        client.persist()

    @staticmethod
    def retrieve(query_text, name, chunk_type):

        metadata = {"name": name, "type": chunk_type}

        try:
            results = collection.query(
                query_texts=[query_text],
                n_results=3,
                where=metadata,
                include=["documents", "distances", "metadatas"]
            )
        except (chromadb.errors.NoDatapointsException, chromadb.errors.NotEnoughElementsException) as e:
            # Print the error message
            print(f"Error: {e}")
            # Return an empty list if no results are found or if there are not enough elements
            results = []

        # print(f"Generated results: {results}")
        return results

# END
