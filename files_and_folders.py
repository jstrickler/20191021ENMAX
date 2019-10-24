#!/usr/bin/env python
import os
from datetime import datetime

folder_name = "DATA"
file_name = "alice.txt"

file_path = os.path.join(folder_name, file_name)

print("file path:", file_path)
file_size = os.path.getsize(file_path)
print("file size:", file_size)

print("dir name:", os.path.dirname(file_path))
print("base name:", os.path.basename(file_path))
print("absolute path:", os.path.abspath(file_path))

raw_timestamp  = os.path.getmtime(file_path)
print("raw timestamp:", raw_timestamp)

timestamp = datetime.fromtimestamp(raw_timestamp)
print("timestamp:", timestamp)
print(timestamp.year, timestamp.month)
