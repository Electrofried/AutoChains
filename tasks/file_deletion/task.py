import os

def execute(input_path):
    try:
        os.remove(input_path)
        message = f"File '{input_path}' has been deleted successfully."
        return {'message': message}
    except Exception as e:
        message =  f"Error deleting file '{input_path}': {e}"
        return {'message': message}
