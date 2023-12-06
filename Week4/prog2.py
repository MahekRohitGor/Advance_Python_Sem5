text = "Hello, 你好, مرحبًا"
encoded_text = text.encode('utf-8')  
print(f"Encoded Text: {encoded_text}") 
decoded_text = encoded_text.decode('utf-8')
print(f"Decoded Text: {decoded_text}")
print ("Task1 is done")
with open("encoded_file.txt", "w", encoding="utf-8") as file:
    file.write("Hello, 你好, مرحبًا")
with open("encoded_file.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(f"File Content: {content}")
print("Task2: Reading from a file is done")
binary_data = b'\x48\x65\x6c\x6c\x6f\x20\x57\x6f\x72\x6c\x64'
with open('binary_file.bin', 'wb') as file:
    file.write(binary_data)
with open('binary_file.bin', 'rb') as file:
    content = file.read()
    print(f"File Content: {content}")
print("Task3: writing binary file is done")
buffer_size = 10 
with open('buffered_example.txt', 'w', buffering=buffer_size) as file:
    for i in range(1, 6):
        file.write(f"This is line {i}\n")
print("Task4: Buffering is done")
