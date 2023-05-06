import pylint.lint

def execute(python_code: str):
    with open("temp_code.py", "w") as f:
        f.write(python_code)
    
    pylint_output = pylint.lint.Run(["temp_code.py"], do_exit=False)
    return {'status': 'success', 'syntax_check_result': pylint_output.linter.stats['message']}
