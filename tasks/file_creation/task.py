import os

def execute(file_path, file_content):
    try:
        with open(file_path, 'w') as file:
            file.write(file_content)
        return f"File '{file_path}' has been created successfully."
    except Exception as e:
        return f"Error creating file '{file_path}': {e}"
