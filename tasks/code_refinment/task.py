from provider import generate_text


def execute(input_code: str, input_goal: str, input_sub_goal: str, input_error: str = None):
    prompt_template = load_prompt_text('tasks/code_refinement/prompt.txt')

    error_section = f"Consider the following error message: '{input_error}'." if input_error else ""
    prompt = prompt_template.format(main_goal=input_goal, sub_goal=input_sub_goal, error_section=error_section, code=input_code)
    
    refined_code = generate_text(prompt)
    return {'status': 'success', 'refined_code': refined_code}


def load_prompt_text(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()
