import re
import sys


DIRECTORY_REGEX = r'^[A-Za-z0-9_-]*$'

directory_name = '{{ cookiecutter.project_slug }}'

if not re.match(DIRECTORY_REGEX, directory_name):
    print(f'ERROR: {directory_name} is not an acceptable directory!')

    # exits with status 1 to indicate failure
    sys.exit(1)