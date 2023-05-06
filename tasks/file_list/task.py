import os

def execute(directory_path: str):
    try:
        file_list = os.listdir(directory_path)
        return {'status': 'success', 'file_list': file_list}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

