# Take prompt.txt and append the user input for processing


def format_input(prompt, memories):
    with open("prompt.txt", "r") as file:
        template = file.read()

    formatted_memories = '\n'.join(memories)
    formatted_prompt = template.replace("{prompt}", prompt).replace("{memories}", formatted_memories)
    return formatted_prompt
