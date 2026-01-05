import subprocess
import shlex

def run_command(command_str):
    args = shlex.split(command_str)
    result = subprocess.run(
        args,
        capture_output=True,
        text=True,
        shell=False
    )
    return result.stdout