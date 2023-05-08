import os

def execute(input_directory: str):
    try:
        file_list = os.listdir(input_directory)
        return {'status': 'success', 'file_list': file_list}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

