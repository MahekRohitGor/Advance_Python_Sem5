# Custom exception for file read error
class FileReadError(Exception):
    pass

# Custom exception for file write errors
class FileWriteError(Exception):
    pass

def read_bfile(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            return data
    except FileNotFoundError:
        raise FileReadError(f"File '{file_path}' not found.")
    except Exception as e:
        raise FileReadError(f"An error occurred while reading '{file_path}': {str(e)}")

def write_bfile(file_path, data):
    try:
        with open(file_path, 'wb') as file:
            file.write(data)
    except Exception as e:
        raise FileWriteError(f"An error occurred while writing '{file_path}': {str(e)}")
try:
    content = read_bfile('Week4/data.bin')
    new_data = b"New binary data"
    write_bfile('Week4/new_data.bin', new_data)
except FileReadError as read_err:
    print(f"File read error: {read_err}")
except FileWriteError as write_err:
    print(f"File write error: {write_err}")
