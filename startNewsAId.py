import os
import subprocess

def run_commands_in_terminals(commands):
    # Base directory relative to the script's location
    base_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))
    # AppleScript to open a new Terminal window and navigate to the project directory
    apple_script = 'tell application "Terminal" to do script "cd \\"{dir}\\" && {command}"'
    # Loop over each command
    for command in commands:
        full_command = apple_script.format(dir=base_dir, command=command)
        subprocess.run(['osascript', '-e', full_command])

if __name__ == "__main__":
    # List of commands to run in separate terminals
    commands = [
        'source ~/.venv/bin/activate && python3 Backend/newspagegeneration.py',  # Example command 1
        'source ~/.venv/bin/activate && ./run',                                  # Example command 2
        'source ~/.venv/bin/activate && cd Frontend && npm run dev'              # Example command 3
    ]
    
    run_commands_in_terminals(commands)
    print("Everything is running!\n")
    print("Navigate to: http://localhost:3000 to start!")
