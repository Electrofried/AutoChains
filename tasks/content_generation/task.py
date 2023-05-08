import os

from provider import generate_text

def execute(input_type: str, input_goal: str, input_sub_goal: str, input_instruction: str = None):
    prompt_template = load_prompt_text('tasks/content_generation/prompt.txt')

    instruction_section = f"Please follow this instruction: '{input_instruction}'." if input_instruction else ""
    prompt = prompt_template.format(content_type=input_type, main_goal=input_goal, sub_goal=input_sub_goal, instruction_section=instruction_section)

    generated_content = generate_text(prompt)
    
    return {'output_data': generated_content}

def load_prompt_text(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()