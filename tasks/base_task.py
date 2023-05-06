from tasks.base_task import BaseTask

tasks = BaseTask.load_tasks()

# You can now iterate over tasks and call the execute method as needed
for task in tasks:
    # Check if the input_data is compatible with the task's expected input_type
    if isinstance(input_data, task.info['input_type']):
        result = task.execute(input_data)
        
        # Handle the output data based on the task's output_type
        if task.info['output_type'] == 'str':
            # Handle string output
            pass
        elif task.info['output_type'] == 'dict':
            # Handle dictionary output
            pass
        # Add other output types as needed
