import os
from provider import generate_text

def execute(main_goal: str, sub_goal: str, specific_info: str = None):
    prompt_template = load_prompt_text('tasks/code_generation/prompt.txt')

    specific_info_section = f"Keep in mind the following specific information: '{specific_info}'." if specific_info else ""
    prompt = prompt_template.format(main_goal=main_goal, sub_goal=sub_goal, specific_info_section=specific_info_section)
    
    generated_code = generate_text(prompt)
    return {'status': 'success', 'generated_code': generated_code}

def load_prompt_text(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()