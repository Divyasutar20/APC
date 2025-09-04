
with open("file_example.txt", "w") as f:
    f.write("Line 1: Hello, file!\n")
    f.write("Line 2: Writing to file.\n")

with open("file_example.txt", "a") as f:
    f.write("Line 3: Appended line.\n")

with open("file_example.txt", "r") as f:
    content = f.read()
    print("Read entire content:\n", content)

with open("file_example.txt", "r") as f:
    print("Read line by line:")
    for line in f:
        print(line.strip())

with open("file_example.txt", "r") as f:
    lines = f.readlines()
    print("Readlines:", lines)

import os
os.rename("file_example.txt", "renamed_file.txt")
print("File renamed.")

os.remove("renamed_file.txt")
print("File deleted.")
