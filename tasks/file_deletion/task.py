import os

def execute(file_path):
    try:
        os.remove(file_path)
        return f"File '{file_path}' has been deleted successfully."
    except Exception as e:
        return f"Error deleting file '{file_path}': {e}"
