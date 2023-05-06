import re
import json
import os

def load_filter():
    if not os.path.exists('filter.json'):
        raise FileNotFoundError('Filter file "filter.json" not found. Please ensure the file is in the correct directory.')

    with open('filter.json', 'r') as f:
        filter_list = json.load(f)
    return filter_list

def filter_text(text, filter_list):
    for filter_item in filter_list:
        text = text.replace(filter_item, '')
    return text

def split_long_sentence(sentence, max_chars):
    words = sentence.split(' ')
    chunks = []
    current_chunk = ""

    for word in words:
        if len(current_chunk) + len(word) + 1 > max_chars:
            chunks.append(current_chunk)
            current_chunk = word
        else:
            if current_chunk:
                current_chunk += " "
            current_chunk += word

    if current_chunk:
        chunks.append(current_chunk)

    return chunks

def chunk_text(text, max_chars=180, min_chars=64):
    filter_list = load_filter()
    text = filter_text(text, filter_list)

    sentences = re.split(r'(?<=[.!?])\s+', text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(sentence) > max_chars:
            long_sentence_chunks = split_long_sentence(sentence, max_chars)
            chunks.extend(long_sentence_chunks)
            continue

        if len(current_chunk) + len(sentence) + 1 > max_chars:
            chunks.append(current_chunk)
            current_chunk = sentence
        else:
            if len(current_chunk) + len(sentence) + 1 <= min_chars:
                if current_chunk:
                    current_chunk += " "
                current_chunk += sentence
            else:
                chunks.append(current_chunk)
                current_chunk = sentence

    if current_chunk:
        chunks.append(current_chunk)

    i = 0
    while i < len(chunks) - 1:
        combined_length = len(chunks[i]) + len(chunks[i + 1]) + 1
        if combined_length <= max_chars:
            chunks[i] += " " + chunks.pop(i + 1)
        else:
            i += 1

    return chunks
