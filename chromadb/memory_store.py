# # memory_store.py

import uuid
from chroma_handler import ChromaDBHandler
from chunking import chunk_text

LOG_LEVEL = 2  # Set the log level: 0 - No logs, 1 - Info, 2 - Debug


def logger(message, level=1):
   
    if LOG_LEVEL >= level:
        print(message)


def store_filtered_chunks(chroma_handler, prompt, result, name):
    
    prompt_id = str(uuid.uuid4())
    store_chunk(chroma_handler, prompt, name, 'prompt', prompt_id)
    store_chunk(chroma_handler, result, name, 'response', prompt_id)


def store_chunk(chroma_handler, chunk, name, chunk_type, prompt_id):
    
    texts = chunk_text(chunk, max_chars=180, min_chars=64)
    logger(f"Chunked text: {texts}", 1)

    memories = []
    metadatas = []
    ids = []

    for text_chunk in texts:
        if len(text_chunk) >= 32:
            retrieved_chunk = chroma_handler.retrieve(text_chunk, name, chunk_type)

            if not retrieved_chunk:
                memory_id = str(uuid.uuid4())
                logger(f"Generated memory_id: {memory_id}", 2)

                memories.append(text_chunk)
                metadatas.append({"name": name, "prompt_id": prompt_id, "type": chunk_type})
                ids.append(memory_id)
            else:
                should_store = True
                for distance_list in retrieved_chunk['distances']:
                    if any(distance <= 0.2 for distance in distance_list):
                        should_store = False
                        break

                if should_store:
                    memory_id = str(uuid.uuid4())
                    logger(f"Generated memory_id: {memory_id}", 2)

                    memories.append(text_chunk)
                    metadatas.append({"name": name, "prompt_id": prompt_id, "type": chunk_type})
                    ids.append(memory_id)

    if memories:
        logger(f"Saving memories: {memories}", 2)
        chroma_handler.store(textdata=memories, metadata=metadatas, ids=ids)


