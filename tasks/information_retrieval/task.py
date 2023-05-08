import os

from provider import generate_text

def execute(input_goal: str, input_sub_goal: str, input_info: str = None):
    prompt_template = load_prompt_text('tasks/information_retrieval/prompt.txt')

    specific_info_section = f"Keep in mind the following specific information: '{input_info}'." if input_info else ""
    prompt = prompt_template.format(main_goal=input_goal, sub_goal=input_sub_goal, specific_info_section=specific_info_section)

    retrieved_information = generate_text(prompt)
    return {'status': 'success', 'retrieved_information': retrieved_information}


def load_prompt_text(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()