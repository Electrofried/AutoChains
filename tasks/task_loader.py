import os
import json
import importlib
from importlib.util import spec_from_file_location, module_from_spec

class TaskLoader:
    def __init__(self, tasks_directory: str = "tasks"):
        self.tasks_directory = tasks_directory
        self.tasks = self.load_tasks()

    def load_tasks(self):
        tasks = {}
        for task_dir in os.listdir(self.tasks_directory):
            task_path = os.path.join(self.tasks_directory, task_dir)
            if os.path.isdir(task_path):
                task_info_file = os.path.join(task_path, "task_info.json")
                task_module_file = os.path.join(task_path, "task.py")

                if os.path.exists(task_info_file) and os.path.exists(task_module_file):
                    with open(task_info_file, "r") as f:
                        task_info = json.load(f)

                    spec = spec_from_file_location(f"{task_dir}.task", task_module_file)
                    task_module = module_from_spec(spec)
                    spec.loader.exec_module(task_module)

                    tasks[task_dir] = {
                        "info": task_info,
                        "module": task_module,
                    }
        return tasks

    def execute_task(self, task_name: str, **kwargs):
        if task_name not in self.tasks:
            raise ValueError(f"Task '{task_name}' not found.")
        task = self.tasks[task_name]
        return task["module"].execute(**kwargs)
