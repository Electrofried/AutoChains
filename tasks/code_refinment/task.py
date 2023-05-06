from provider import generate_text


def execute(code: str, main_goal: str, sub_goal: str, error: str = None):
    prompt_template = load_prompt_text('tasks/code_refinement/prompt.txt')

    error_section = f"Consider the following error message: '{error}'." if error else ""
    prompt = prompt_template.format(main_goal=main_goal, sub_goal=sub_goal, error_section=error_section, code=code)
    
    refined_code = generate_text(prompt)
    return {'status': 'success', 'refined_code': refined_code}


def load_prompt_text(filename: str) -> str:
    with open(filename, 'r') as file:
        return file.read()
