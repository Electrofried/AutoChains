import os

def execute(input_path, input_content):
    try:
        with open(input_path, 'w') as file:
            file.write(input_content)
        message = f"File '{input_path}' has been created successfully."
        return {'message': message}
    except Exception as e:
        message = f"Error creating file '{input_path}': {e}"
        return {'message': message}
