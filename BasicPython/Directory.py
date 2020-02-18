import os

path = "/home/bridgelabz/Desktop/AllBasicProgram"
files = []
# r=root,d=directories, f =files
for r, d, f in os.walk(path):
    for file in f:
        if '.py' in file:
            files.append(os.path.join(r, file))
for f in files:
    print(f)
           