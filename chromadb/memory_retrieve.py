from chroma_handler import ChromaDBHandler

def filter_memories_by_distance(retrieved_memories, distance_value, higher_than=True):

    filtered_memories = []
    for i in range(len(retrieved_memories['documents'][0])):
        memory = retrieved_memories['documents'][0][i]
        distance = retrieved_memories['distances'][0][i]

        if higher_than:
            if distance > distance_value:
                filtered_memories.append(memory)
        else:
            if distance < distance_value:
                filtered_memories.append(memory)

    return filtered_memories


def get_filtered_memories(prompt, name, chunktype, distance_value=0.1):
    handler = ChromaDBHandler()
    retrieved_memories = handler.retrieve(query_text=prompt, name=name, chunk_type=chunktype)

    if not retrieved_memories:
        return []

    filtered_memories = filter_memories_by_distance(retrieved_memories, distance_value)
    return filtered_memories
