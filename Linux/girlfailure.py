import os
import subprocess

path = input("Enter path: ")
file_substr = input("Enter file name substring: ")
dest = input("Enter destination directory: ")
mvd = 0

src_list = os.listdir(path=path)

print(f"Getting images in directory: {path}")
print("------------")

for img in src_list:
    full_path = path + img
    cmd = f"mv {full_path} {dest}"
    result = subprocess.run(
        cmd,
        shell=True,
        capture_output=True,
        text=True,
    )
    print(result.stderr)
    print(f"moved {mvd}")
    mvd += 1
    break
else:
    print("Nothing found")
