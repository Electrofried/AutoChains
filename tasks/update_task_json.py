import os
import json
import ast
from pathlib import Path

def extract_imports(node):
    imports = []
    if isinstance(node, ast.Import):
        for alias in node.names:
            imports.append(alias.name)
    elif isinstance(node, ast.ImportFrom):
        for alias in node.names:
            imports.append(f"{node.module}.{alias.name}")
    for child in ast.iter_child_nodes(node):
        imports.extend(extract_imports(child))
    return imports


task_folders = [f for f in os.listdir() if os.path.isdir(f) and f != "__pycache__"]
all_imports = set()

for folder in task_folders:
    task_file = os.path.join(folder, "task.py")
    json_file = os.path.join(folder, "task_info.json")

    with open(task_file, "r") as f:
        source_code = f.read()

    module = ast.parse(source_code)

    imports = list(set(extract_imports(module)))
    all_imports.update(imports)

    function_node = None
    for node in module.body:
        if isinstance(node, ast.FunctionDef) and node.name == "execute":
            function_node = node
            break

    if function_node is not None:
        input_tags = [arg.arg for arg in function_node.args.args]
        output_tag = "result" if function_node.returns else None

        with open(json_file, "r") as json_f:
            task_info = json.load(json_f)

        task_info["input_tags"] = input_tags
        task_info["imports"] = imports
        if output_tag:
            task_info["output_tags"] = [output_tag]

        with open(json_file, "w") as json_f:
            json.dump(task_info, json_f, indent=4)

    else:
        print(f"Error: 'execute' method not found in {task_file}")

print("Task JSON files updated successfully.")

with open("requirements.txt", "w") as req_file:
    req_file.write("\n".join(sorted(all_imports)))

print("Generated requirements.txt with all imported packages.")
