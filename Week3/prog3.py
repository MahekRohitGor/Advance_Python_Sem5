# Program to copy all the files with '.jpg' extension from a source directory to the 
#'destination' directory. Finally, the program should navigate the file system and display the current 
# working directory and its parent directory.
import os
import shutil
dest_directory = "destination"
os.makedirs(dest_directory)
print("New directory created: ", dest_directory)

source_directory = "source"
for filename in os.listdir(source_directory):
    if filename.endswith(".jpg"):
        source_file = os.path.join(source_directory, filename)
        destination_file = os.path.join(dest_directory, filename)
        shutil.copy(source_file, destination_file)
        print("Copied: ", source_file, "->", destination_file)

current_directory = os.getcwd()
print("Current Directory: ", current_directory)

parent_directory = os.path.dirname(current_directory)
print("Parent Directory: ", parent_directory)

child_directory = [d for d in os.listdir(current_directory) if os.path.isdir(os.path.join(current_directory,d))]
print("Child directory: ", child_directory)