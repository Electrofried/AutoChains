import json
import os
import requests

CONFIG_FILE = 'config.json'

# Load the configuration from the config.json file
def get_config():
    if not os.path.exists(CONFIG_FILE):
        raise FileNotFoundError(f'{CONFIG_FILE} file not found')

    with open(CONFIG_FILE) as f:
        return json.load(f)

# Run the request to the remote server
def run(prompt, **kwargs):
    # Get the configuration data
    config = get_config()
    
    # Extract the default_params and HOST from the configuration
    default_params = config['default_params']
    HOST = config['HOST']

    # Update the default_params with any provided kwargs
    default_params.update({k: v for k, v in kwargs.items() if v is not None})

    URI = f'http://{HOST}/api/v1/generate'

    # Send a POST request to the remote server
    response = requests.post(URI, json={
        'prompt': prompt,
        **default_params
    })

    # Check the response status code
    if response.status_code == 200:
        # Extract the JSON data from the response
        result = response.json()['results'][0]['text']
        
        # Return the result
        return result
    else:
        raise Exception("Error generating text, check the text generator is running and try again")
