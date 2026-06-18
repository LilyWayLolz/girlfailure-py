import os
import subprocess

path = input("Enter path: ")
file_substr = input("Enter file name substring: ")
dest = input("Enter destination directory: ")
mvd = 0

src_list = os.listdir(path=path)

print("------------")
print(f"Getting files in directory: {path}")
print("------------")

for img in src_list:
    if file_substr in img:
        full_path = path + img
        cmd = f"move {full_path} {dest}"
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
        )
        print(result.stderr)
        print(f"moved {mvd}")
        if result != "The system cannot find the path specified.":
            mvd += 1
    else:
        print("Nothing found")
