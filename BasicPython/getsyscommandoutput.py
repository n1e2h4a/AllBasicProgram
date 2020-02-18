import subprocess
returned_text = subprocess.check_output("dir" , shell=True, universal_newlines=True)
print("Dir commands to list and directory")
print(returned_text)
