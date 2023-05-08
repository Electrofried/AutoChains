import os

def execute(input_path, input_content):
    try:
        with open(input_path, 'a') as file:
            file.write(input_content)
        message = f"Content appended to file '{input_path}' successfully."
        return {'message': message}
    except Exception as e:
        message = f"Error appending content to file '{input_path}': {e}"
        return {'message': message}
