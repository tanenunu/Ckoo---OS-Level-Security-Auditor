import subprocess
import shlex
import platform

def run_command(check):
    
    os_name = platform.system()
    commands = check.get("commands")
    if not commands:
        return None
    
    command_str = commands.get(os_name)
    print(f"Running command '{command_str}'...")
    if not command_str:
        return None #OS not supported for this check
    
    # Windows needs shell=True for built-ins
    if os_name == "Windows":
        result = subprocess.run(
            command_str,
            capture_output=True,
            text=True,
            timeout=60,
            shell=True
        )
    else:
        args = shlex.split(command_str)
        result = subprocess.run(
            args,
            capture_output=True,
            text=True,
            timeout=60,
            shell=False
        )
    print("DONE✅")

    return result.stdout