import os
from provider import generate_text

def execute(input_data, num_sub_tasks):
    with open(os.path.join(os.path.dirname(__file__), "prompt.txt"), "r") as f:
        prompt_template = f.read()
    
    prompt = input_data["prompt"]
    prompt_txt = prompt_template.format(objective=prompt, num_sub_tasks=num_sub_tasks)
    
    generated_text = generate_text(prompt_txt)
    sub_tasks = parse_sub_tasks(generated_text, num_sub_tasks)
    
    return sub_tasks


def parse_sub_tasks(generated_text, num_sub_tasks):
    lines = generated_text.split('\n')
    sub_tasks = [line.strip() for line in lines if line.strip() and line[:20].strip().isdigit()]
    return sub_tasks[:num_sub_tasks]

