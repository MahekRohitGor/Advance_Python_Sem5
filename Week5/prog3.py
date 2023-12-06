import subprocess
# Python program (Parent process) will create subprocess with run() or Popen()
def run_command(command): # takes a parameter command, which represents the command to be executed.
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True)
        
        if result.returncode == 0: 
            print("Command executed successfully:")
            print(result.stdout)   
        else:
            print("Command failed:")
            print(result.stderr)  # Access and print the error output from PIPE programmatically 
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    command = input("Enter a command to run: ")  # e.g. For Windows 'dir' for Unix 'ls'
    run_command(command)