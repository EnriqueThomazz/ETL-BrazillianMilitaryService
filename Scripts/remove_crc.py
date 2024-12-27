# When using Spark and saving parquet files, a checksum file will always be created, as well as a SUCCESS file.
# PowerBI doesnt handle those files when loading the data, so I'm deleting them manually
import os

# Root directory
dir = "./Gold/"

# Walking to every file in the directory and subdirectories
for path, subd, files in os.walk(dir):
    for name in files:
        f_path = os.path.join(path, name)
        
        # If the file fits the deleting parameters
        if name == '_SUCCESS' or name.endswith(".crc"):
            os.remove(f_path)