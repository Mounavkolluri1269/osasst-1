import subprocess
import os
import platform

def display_instructions():
    print("Available commands:")
    print("- ls/dir: List directory contents")
    print("- mkdir/md: Create a new directory")
    print("- cat/type: Display file contents")
    print("- help: Show this help message")
    print("- exit: Exit the CLI")

def run_cli():
    print("Welcome to the Simple CLI! Type 'help' for available commands.")
    os_type = platform.system().lower()

    while True:
        user_input = input("> ").strip()

        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        elif user_input.lower() == "help":
            display_instructions()
        elif user_input.startswith("mkdir") or user_input.startswith("md"):
            dir_name = user_input.split(" ", 1)[-1]
            try:
                os.makedirs(dir_name, exist_ok=True)
                print(f"Folder '{dir_name}' created.")
            except Exception as err:
                print(f"Error creating folder: {err}")
        elif user_input.startswith("ls") or user_input.startswith("dir"):
            try:
                if os_type == "windows":
                    subprocess.run("dir", shell=True)
                else:
                    subprocess.run("ls", shell=True)
            except Exception:
                print("Error listing directory contents.")
        elif user_input.startswith("cat") or user_input.startswith("type"):
            parts = user_input.split(" ", 1)
            if len(parts) == 2:
                file_name = parts[1]
                try:
                    if os_type == "windows":
                        subprocess.run(f"type {file_name}", shell=True)
                    else:
                        subprocess.run(f"cat {file_name}", shell=True)
                except Exception:
                    print("Error displaying file contents.")
            else:
                print("Error: No filename provided.")
        elif user_input == "":
            print("Error: Empty command.")
        else:
            print("Error: Command not recognized.")

if __name__ == "__main__":
    run_cli()
