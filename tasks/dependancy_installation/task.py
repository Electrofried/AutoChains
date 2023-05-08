import subprocess
import re

def execute(input_code: str):
    dependencies = extract_dependencies(input_code)
    try:
        for dependency in dependencies:
            subprocess.check_call(["pip", "install", dependency])
        return {'status': 'success'}
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def extract_dependencies(python_code: str):
    dependencies = set()
    lines = python_code.split("\n")
    for line in lines:
        if line.startswith("import") or line.startswith("from"):
            match = re.search(r"^\s*(?:import|from)\s+([\w_]+)", line)
            if match:
                dependencies.add(match.group(1))
    return list(dependencies)


