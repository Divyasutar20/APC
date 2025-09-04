import os
import shutil

dir_name = "file_dir"
if not os.path.exists(dir_name):
    os.mkdir(dir_name)
os.chdir(dir_name)
file_name = "file_file.txt"
with open(file_name, "w") as f:
    f.write("This is an example of Directory Handling.\n")
print("Current Directory:", os.getcwd())
print("List of files and directories:", os.listdir("."))
renamed_file = "renamed_file.txt"
os.rename(file_name, renamed_file)
copied_file = "copied_file.txt"
shutil.copy(renamed_file, copied_file)
os.remove(renamed_file)
os.chdir("..")
shutil.rmtree(dir_name)
print("Directory and file operations completed.")
