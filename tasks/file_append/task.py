import os

def execute(file_path, content_to_append):
    try:
        with open(file_path, 'a') as file:
            file.write(content_to_append)
        return f"Content appended to file '{file_path}' successfully."
    except Exception as e:
        return f"Error appending content to file '{file_path}': {e}"

