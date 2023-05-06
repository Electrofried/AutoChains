import os

from provider import generate_text

def execute(content_type: str, main_goal: str, sub_goal: str, instruction: str = None):
    prompt_template = load_prompt_text('tasks/content_generation/prompt.txt')

    instruction_section = f"Please follow this instruction: '{instruction}'." if instruction else ""
    prompt = prompt_template.format(content_type=content_type, main_goal=main_goal, sub_goal=sub_goal, instruction_section=instruction_section)

    generated_content = generate_text(prompt)
    return {'status': 'success', 'generated_content': generated_content}

def load_prompt_text(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()