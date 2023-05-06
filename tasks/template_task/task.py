import os

from provider import generate_text

def execute(input_data):
    with open(os.path.join(os.path.dirname(__file__), "prompt.txt"), "r") as f:
        prompt_template = f.read()
    
    # Replace {placeholders} in the prompt_template with appropriate values from input_data
    prompt = prompt_template.format(**input_data)
    
    generated_text = generate_text(prompt)
    
    # Process the generated_text and return the output as needed by the task
    # ...
