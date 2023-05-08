import os

def execute(input_directory: str):
    try:
        file_list = os.listdir(input_directory)
        return {'status': 'success', 'output_data': file_list}
    except Exception as e:
        return {'status': 'failure', 'message': str(e)}

