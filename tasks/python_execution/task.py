import subprocess

def execute(input_path: str):
    try:
        result = subprocess.check_output(["python", input_path])
        return {'status': 'success', 'output_data': result.decode("utf-8")}
    except subprocess.CalledProcessError as e:
        return {'status': 'error', 'output_data': str(e.output)}
