from io import StringIO
from pylint import epylint as lint

def execute(input_code: str):

    pylint_output = StringIO()
    lint.py_run(command_options='', file_input=StringIO(input_code), reporter=lint.PyLintReporter(output=pylint_output))
    pylint_result = pylint_output.getvalue()

    if pylint_result.strip() == "":
        return {'status': True, 'output_data': pylint_result}
    else:
        return {'status': False, 'output_data': pylint_result}


