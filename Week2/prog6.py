# Read and write JSON data to/from a file. The code defines two functions, read_json(filename) and write_json(filename, data), that handle reading and writing JSON data from/to a file, respectively. It provides an example usage where it creates a sample JSON object, writes it to a file, reads it back from the file, modifies the JSON data, and then writes the updated data back to the file.
# Date: 31st July
import json
def read_json(filename):  
    with open(filename, 'r') as file: # open file in read mode
        #the json module provides two main methods for working with JSON data: json.load() and json.dump().
        # json.load: This method is used to read JSON data from a file-like object and parse it into a Python data structure
        json_data = json.load(file)
    return json_data

def write_json(filename, data):
    with open(filename, 'w') as file: # Open file in write mode
        # json.dump: This method is used to write JSON data from a Python data structure into a file-like object 
        json.dump(data, file, indent=4)
        print("Data written successfully in sample.json file!")

if __name__ == "__main__":
    data = {
        "Name": "Mahek Gor",
        "Age": 20,
        "Course": "CSE",
        "email": "mg@xyz.com"
    }

    write_json("Syllabus/Week2/sample.json", data)

    print("Original Data before modifications")
    read_file_data = read_json("Syllabus/Week2/sample.json")
    if read_file_data:
        print(read_file_data)

# Let us Modify the data in json file
read_file_data["Course"] = "Computer Science and Engineering"

# Write it back to sample.json
write_json("Syllabus/Week2/sample.json", read_file_data)

print("Updated data after modifications")
read_file_data = read_json("Syllabus/Week2/sample.json")
if read_file_data:
    print(read_file_data)

