import os
from provider import generate_text

def execute(input_data: str, input_goal: str, input_info: str = None):
    prompt_template = load_prompt_text('tasks/code_generation/prompt.txt')

    specific_info_section = f"Keep in mind the following specific information: '{input_info}'." if input_info else ""
    prompt = prompt_template.format(main_goal=input_data, sub_goal=input_goal, specific_info_section=specific_info_section)
    
    generated_code = generate_text(prompt)

    # Impliment code extraction from prompt. Return true/false based on detected code.
    success=True

    

    return {'status': success, 'output_code': generated_code}

def load_prompt_text(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()