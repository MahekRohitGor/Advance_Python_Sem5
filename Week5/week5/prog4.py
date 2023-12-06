import subprocess

def pipline():
    try:
        data = "Hello World! \n Hello World"
        echo_process = subprocess.Popen(['echo', data], stdout=subprocess.PIPE)
        grep_process = subprocess.Popen(['grep', 'Hello'], stdout=subprocess.PIPE)
        echo_process.stdout.close()
        output = grep_process.communicate()[0].decode('utf-8')
        print("Output after filtering")
        print(output)
    except Exception as e:
        print("Error: ", e)


if __name__ == "__main__":
    pipline()