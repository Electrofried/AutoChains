import subprocess

def execute(file_path: str):
    try:
        result = subprocess.check_output(["python", file_path])
        return {'status': 'success', 'execution_result': result.decode("utf-8")}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'message': str(e.output)}
