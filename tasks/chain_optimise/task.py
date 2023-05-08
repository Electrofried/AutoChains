from provider import generate_text
from task_loader import TaskLoader
import re



def execute(input_data: list, chain_so_far: list) -> dict:
    formatted_current_chain = "\n".join([f"{i + 1}. {task}" for i, task in enumerate(chain_so_far)])
    prompt = load_prompt_text('tasks/chain_optimise/prompt.txt')
    prompt = prompt.format(objective_list=input_data, current_chain=formatted_current_chain)

    optimized_chain_text = generate_text(prompt)

    # Extract the tasks from the optimized chain text
    optimized_chain = extract_tasks(optimized_chain_text, chain_so_far)

    return {'optimized_chain': optimized_chain}

def extract_tasks(response: str, valid_tasks: list) -> list:
    tasks = []
    for task in valid_tasks:
        if re.search(r'\b' + re.escape(task) + r'\b', response):
            tasks.append(task)
    return tasks


def load_prompt_text(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()
