import json
import os

task_directory = '.'

combined_tags = {
    "task_types": [],
    "input_tags": {},
    "output_tags": {},
    "attributes": {}
}

for root, _, files in os.walk(task_directory):
    if 'task_info.json' in files:
        with open(os.path.join(root, 'task_info.json'), 'r') as f:
            task_info = json.load(f)

        task_type = task_info["name"]
        combined_tags["task_types"].append(task_type)

        for input_tag in task_info["input_tags"]:
            if input_tag not in combined_tags["input_tags"]:
                combined_tags["input_tags"][input_tag] = []
            combined_tags["input_tags"][input_tag].append(task_type)

        for output_tag in task_info["output_tags"]:
            if output_tag not in combined_tags["output_tags"]:
                combined_tags["output_tags"][output_tag] = []
            combined_tags["output_tags"][output_tag].append(task_type)

        for attribute in task_info["attributes"]:
            if attribute not in combined_tags["attributes"]:
                combined_tags["attributes"][attribute] = []
            combined_tags["attributes"][attribute].append(task_type)

with open('combined_tags.json', 'w') as f:
    json.dump(combined_tags, f, indent=2)
