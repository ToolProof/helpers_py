'''
Docstring
'''
import subprocess
import os
import shutil
from typing import Dict, Optional

def clear_tmp():
    '''
    Clears the temporary directory.
    '''
    tmp_dir = '/tmp'
    for filename in os.listdir(tmp_dir):
        file_path = os.path.join(tmp_dir, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}: {e}')


def run_command(command: str, check: bool = True, env: Optional[Dict[str, str]] = None) -> subprocess.CompletedProcess[str]:
    '''
    Runs a shell command and optionally checks for errors.
    '''
    try:
        result = subprocess.run(command, shell=True, check=check, text=True, capture_output=True, env=env)
        print(result.stdout)
        return result
    except subprocess.CalledProcessError as e:
        print(f'Error while running command: {command}')
        print(f'Stderr: {e.stderr}')  # More detailed error output
        raise