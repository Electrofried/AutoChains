import os

def execute(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        return file_content
    except Exception as e:
        return f"Error retrieving file '{file_path}': {e}"