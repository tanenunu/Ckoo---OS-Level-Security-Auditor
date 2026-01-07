import subprocess
import shlex

#Convert command-line args to tokens:
command_line = "lsof -i | grep LISTEN"
o_p_args = shlex.split(command_line)

#Perform checks:
users_result = subprocess.run(["dscl", ".", "list", "/Users"], capture_output=True, text=True)
runningprocesses_result = subprocess.run(["ps", "aux"], capture_output=True, text=True)
openports_result = subprocess.run(o_p_args, capture_output=True, text=True)
agents_result = subprocess.run(["ls", "/Library/LaunchAgents"], capture_output=True, text=True)
daemons_result = subprocess.run(["ls", "/Library/LaunchDaemons"], capture_output=True, text=True)

#Create reports:
with open("users-result.txt", "w") as file:
    file.write(f"Stdout: {users_result.stdout}\n")
    file.write(f"Stderr: {users_result.stderr}\n")
    file.write(f"Exit code: {users_result.returncode}\n")

with open("runningprocesses-result.txt", "w") as file:
    file.write(f"Stdout: {runningprocesses_result.stdout}\n")
    file.write(f"Stderr: {runningprocesses_result.stderr}\n")
    file.write(f"Exit code: {runningprocesses_result.returncode}\n")

with open("openports-result.txt", "w") as file:
    file.write(f"Stdout: {openports_result.stdout}\n")
    file.write(f"Stderr: {openports_result.stderr}\n")
    file.write(f"Exit code: {openports_result.returncode}\n")

with open("launch-result.txt", "w") as file:
    file.write(f"Stdout: {agents_result.stdout}\n")
    file.write(f"Stderr: {agents_result.stderr}\n")
    file.write(f"Exit code: {agents_result.returncode}\n")
    file.write(f"Stdout: {daemons_result.stdout}\n")
    file.write(f"Stderr: {daemons_result.stderr}\n")
    file.write(f"Exit code: {daemons_result.returncode}\n")


