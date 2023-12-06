import zipfile
import zlib
data = "This is the sample data that needs to be compressed"*1000
compressed_data = zlib.compress(data.encode('utf-8'))
decompressed_data = zlib.decompress(compressed_data)
print(f"Data: {len(data)}")
print(f"Compressed Data : {len(compressed_data)}")
print(f"Decompressed Data : {len(decompressed_data)}")