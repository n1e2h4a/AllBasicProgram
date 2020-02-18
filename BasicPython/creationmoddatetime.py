import os.path, time
file=input("Enter the file which you want to check:--")
print("last time modification: %s" % time.ctime(os.path.getmtime(file)))
print("creation time: %s" % time.ctime(os.path.getctime(file)))