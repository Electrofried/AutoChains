from task_loader import TaskLoader
from provider import generate_text
import re


def execute(input_data: str) -> dict:
    input_types = ['main_goal', 'sub_goal']
    task_loader = TaskLoader()
    valid_starting_tasks = task_loader.get_valid_tasks_by_input_types(input_types)

    prompt = load_prompt_text('tasks/chain_create/prompt.txt')
    prompt = prompt.format(objective_list=input_data, valid_starting_tasks=valid_starting_tasks)
    chosen_starting_task = generate_text(prompt)
    # Extract the chosen task name from the response
    chosen_starting_task_name = extract_task_name(chosen_starting_task, valid_starting_tasks)

    chain_so_far = [chosen_starting_task_name]

    return {'chosen_starting_task_name': chosen_starting_task_name, 'chain_so_far': chain_so_far}

def load_prompt_text(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()
    
def extract_task_name(response: str, valid_tasks: list) -> str:
    for task in valid_tasks:
        if re.search(r'\b' + re.escape(task['name']) + r'\b', response):
            return task['name']
    return None
