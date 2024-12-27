# Some files were created in encodings other then utf8, the problem is that python tries to read them all with utf8
# wich causes some weird symbols to appear.

# The purpose of this script is to load the csv files and detect wich is the right encoding, load with the right encoding and then save as utf8
import chardet
import os
import pandas as pd

# Getting all the files
files = os.listdir("./Raw")

for f in files:
    encoding = None
    with open("./Raw/" + f, "rb") as arq:
        print(f)
        encoding = chardet.detect(arq.read(1000))["encoding"] # Detecting the encoding

    df = pd.read_csv("./Raw/" + f, encoding=encoding, low_memory=False) # Opening with the right encoding
    df.to_csv("./Raw/" + f, index=False, encoding="utf-8") # Saving as UTF8