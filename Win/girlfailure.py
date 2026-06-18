import os
import subprocess

# import pathlib

path = input("Enter path: ")
file_substr = input("Enter file name substring: ")
dest = input("Enter destination directory: ")
mvd = 0

# path2 = pathlib.PureWindowsPath(path).as_posix()
# dest2 = pathlib.PureWindowsPath(dest).as_posix()
src_list = os.listdir(path=path)

print("------------")
print(f"Getting files in directory: {path}")
print("------------")

for img in src_list:
    full_path = f"{path}\\{img}"
    cmd = f"move {full_path} {dest}"
    if file_substr in img:
        print(f"moving {img} from {path} to {dest}")
        result = subprocess.run(
            cmd,
            shell=True,
            capture_output=True,
            text=True,
        )
        print(result.stderr)
        if result != "The system cannot find the path specified.":
            mvd += 1
    else:
        print("Nothing found")

print(f"moved {mvd}")
