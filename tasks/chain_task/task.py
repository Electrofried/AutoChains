from task_loader import TaskLoader
from provider import generate_text
import re


def execute(goal: str, chain_so_far: list, hard_limit: int = None) -> str:
    input_types = set(chain_so_far[-1]['output_tags'])
    task_loader = TaskLoader()
    valid_next_tasks = task_loader.get_valid_tasks_by_input_types(input_types)

    prompt = load_prompt_text('tasks/chain_task/prompt.txt')
    prompt = prompt.format(goal=goal, valid_next_tasks=valid_next_tasks, chain_so_far=chain_so_far)
    chosen_next_task = generate_text(prompt)
    chosen_next_task_name = extract_task_name(chosen_next_task, valid_next_tasks)

    if hard_limit and len(chain_so_far) >= hard_limit:
        chosen_next_task_name = 'chain complete'

    return chosen_next_task_name, chain_so_far

def load_prompt_text(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()

def extract_task_name(response: str, valid_tasks: list) -> str:
    for task in valid_tasks:
        if re.search(r'\b' + re.escape(task['name']) + r'\b', response):
            return task['name']
    return None
