import os 
import shutil

def create_directory(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"Directory: '{dir_name}' created successfully!")
    except FileExistsError:
        print(f"Directory '{dir_name}' already exists")

# Function to delete a directory
def delete_directory(dir_name):
    try:
        shutil.rmtree(dir_name)
        print(f"Directory '{dir_name}' deleted successfully!")
    except FileNotFoundError:
        print(f"Directory '{dir_name}' not found")
    except OSError as e:
        print(f"Error Occured while deleting '{dir_name}': {e} ")

def move_file_or_directory(src, dest):
    try:
        shutil.move(src,dest)
        print(f"Moved '{src}' to '{dest}' successfully! ")
    except FileNotFoundError:
        print(f"File or directory '{src}' not found")
    except shutil.Error as e:
        print(f"Error occured while  moving '{src}' to '{dest}' : {e}")

def copy_file_or_directory(src, dest):
    if os.path.exists(src):
        try:
            shutil.copy(src, dest)
            print(f"Copied '{src}' to '{dest}' successfully!")
        except FileNotFoundError:
            print(f"File or directory '{src}' not found")
        except shutil.Error as e:
            print(f"Error occured while copying '{src}'  to '{dest}': {e}")

    else:
        print(f"Source file or directory '{src}' not found")

def list_files_in_directory(dir_name):
    try:
        print(f"Files in directory '{dir_name}' : ")
        for root, dirs, files in os.walk(dir_name):
            for file in files:
                print(os.path.join(root, file))
    except FileNotFoundError:
        print(f"Directory '{dir_name}' not found")

directory_name = "Example_Directory"
create_directory(directory_name)

file_to_move = "example.txt"
file_to_copy = "example_copy.txt"

move_file_or_directory(file_to_move, directory_name)
move_file_or_directory(file_to_copy, directory_name)
list_files_in_directory(os.path.dirname(os.getcwd()))
