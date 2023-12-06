# network of remote environmental monitoring stations is set up in various locations, such as forests, oceans, and remote rural areas. These stations are equipped with sensors that continuously collect various environmental data, including temperature, humidity, air quality, water levels, and more. The collected data is crucial for scientific research, early warning systems, and policy-making related to environmental conservation and disaster management.

#  Consider any real-world problem for best-practices like encoding, decoding, buffering, compress/decompress data and file.
import pickle
import zlib
import csv
import datetime
import zipfile
BUFFER_SIZE = 2
# 1. Collect data from user
def collect_data():
    data = {
        'temperature ': float(input("Enter temperature(degree celcius): ")),
        'humidity ': float(input("Enter humidity(In g/m3): ")),
        'airquality ': float(input("Enter air quality index: ")),
        'waterlevels ': float(input("Enter Water levels: (in meters): ")),
        'windspeed ': float(input("Enter Wind speed(in m/s): ")),
        'solarradiation ': float(input("Enter Solar Radiation (in W/m2): ")),
        'soilmoisture ': float(input("Enter Soil Moisture(in %): "))
    }

    return data

# 2. Encode Data that was collected by user
def encode_data(data):
    binary_encoded_data = pickle.dumps(data)
    return binary_encoded_data

# 3. Decode data that was previously encoded
def decode_data(encoded_data):
    decoded_data = pickle.loads(encoded_data)
    return decoded_data

# 4. Store data zip
def store_data_zip(filepath, data):
    with zipfile.ZipFile(filepath, "a", compression=zipfile.ZIP_DEFLATED) as zipf:
        # Convert the data dictionary to a string
        data_str = ",".join([f"{key}:{value}" for key, value in data.items()])
        # Write the data to the zip file
        zipf.writestr(f"{data['timestamp']}.txt", data_str)

# 5. Store the collected data in a file name 'data.csv' and also write timestamps to it
def store_data_csv(filepath, data):
    current_time = datetime.datetime.now()
    data["timestamp"] = current_time.strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, "a") as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        if csvfile.tell() == 0:
            csv_writer.writeheader()
        csv_writer.writerow(data)

# 6. When buffer is full store it in a file data_env.csv
def collect_and_store_in_buffer(buffer, data):
    buffer.append(data)
    if len(buffer) >= BUFFER_SIZE:
        store_buffer_data(buffer)
        buffer.clear()

# 7. Store data in a buffer
def store_buffer_data(buffer):
    with open("Week4/data_env.csv", "a", newline="") as buffer_file:
        csv_writer = csv.DictWriter(buffer_file, fieldnames=buffer[0].keys())
        for data in buffer:
            csv_writer.writerow(data)

def main():
    data_buffer = []
    BUFFER_SIZE = 5
    
    while True:
        data = collect_data()
        encoded = encode_data(data)
        decoded = decode_data(encoded)
        filepath = "Week4/data.csv"
        filepath1 = "Week4/compressed.zip"
        store_data_csv(filepath, data)
        collect_and_store_in_buffer(data_buffer, data)
        store_data_zip(filepath1, data)
        # Create a file and write the encoded text
        with open("Week4/encoded_data.txt", "a") as file1:
            file_writer = file1.writelines(str(encoded))
        
        # Ask the user if they want to continue or stop
        user_input = input("Do you want to continue? (y/n): ")
        if user_input.lower() != 'y':
            break  # Break the loop if the user doesn't want to continue

    while True:
        user_input = str(input("Do you want to decode data ? (y/n): "))
        if user_input.lower() != 'y':
            break
        else:
            pin = str(input("Enter a pin: "))
            if pin != "1234":
                print("Incorrect Pin !!")
            else:
                print(f"Decoded data is {decoded}")


if __name__ == "__main__":
    main()

