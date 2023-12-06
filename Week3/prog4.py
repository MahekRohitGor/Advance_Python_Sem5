import os
import shutil
import stat
import time

def main():
    file_name = "complex.txt"

    write_to_file(file_name)
    print("____")

    read_from_file(file_name)
    print("____")

    read_single_line(file_name)
    print("____")
    
    read_all_lines(file_name)
    print("____")

    write_list_to_file(file_name)
    print("____")

    move_file_pointer(file_name)
    print("____")

    flush_file_buffer(file_name)
    print("____")

    close_file_explicitly(file_name)
    print("____")

    new_file_name = "renamed_file.txt"
    rename_file("to_rename.txt", new_file_name)
    print("____")

    get_change_file_permission(file_name)
    print("____")
    get_file_metadata(file_name)
    print("____")

def write_to_file(file_name):
    with open(file_name, "w") as file:
        data_to_write = "This is sample file"
        file.write(data_to_write)

def read_from_file(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        print("Reading entire file: ")
        print(content)

def read_single_line(file_name):
    with open(file_name, "r") as file:
        line = file.readline()
        print("Reading a single line: ")
        print(line)

def read_all_lines(file_name):
    with open(file_name, "r") as file:
        lines = file.readlines() #Read line returns list of lines
        print("Reading all lines: ")
        print(lines)

def write_list_to_file(file_name):
    lines_to_write = ["This is another \n", "And one more line\n"]
    with open(file_name, "a") as file:
        file.writelines(lines_to_write)

def move_file_pointer(file_name):
    with open(file_name, "r") as file:
        print("Current position to the file pointer", file.tell())
        file.seek(15)
        print("Moved the file pointer to position 15.")
        print("Current position to the file pointer", file.tell())
        current = file.read()
        print("Reading file after seek(): ")
        print(current)

def flush_file_buffer(file_name):
    with open(file_name, "r") as file:
        print("\n Reading data before flush()")
        print(file.read())
        file.flush()
        print("Reading data after flush()")
        print(file.read()) 
        print("File buffer flushed")

def close_file_explicitly(file_name):
    file = open(file_name, "r")
    print("File is open")
    file.close()
    print("File is closed explicitly")
    
def rename_file(old_file, new_file_name):
    try:
        os.rename(old_file, new_file_name)
        print("File: ", old_file, " renamed to ", new_file_name)
    except FileNotFoundError:
        print("The file ", old_file, " does not exist")
    except FileExistsError:
        print("A file with name", new_file_name, "already exists")

def get_change_file_permission(file_name):
    file_permission = os.stat(file_name).st_mode
    print("File Permission (in octal): ", oct(file_permission))
    file_permission = file_permission | stat.S_IRWXU
    os.chmod(file_name, stat.S_IRWXG)
    print("Changed file permission (in octal)", oct(os.stat(file_name).st_mode))

def get_file_metadata(file_name):
    file_stat = os.stat(file_name)
    print("File Size: ", file_stat.st_size, "bytes")
    print("File Name: ", os.path.basename(file_name))
    print("File Type: ", "Directory" if os.path.isdir(file_name) else "File")
    print("Creation time: ", time.ctime(file_stat.st_ctime))
    print("Last Access Time: ", time.ctime(file_stat.st_atime))
    print("Last Modification time: ", time.ctime(file_stat.st_mtime))
    print("Disk Usage in bytes for D drive: ", shutil.disk_usage("D:/"))


if __name__ == "__main__":
    main()
