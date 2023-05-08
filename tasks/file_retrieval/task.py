import os

def execute(file_path):
    try:
        with open(file_path, 'r') as file:
            file_content = file.read()
        return {'output_data': file_content}
    except Exception as e:
        file_content = f"Error retrieving file '{file_path}': {e}"
        return {'output_data': file_content}
