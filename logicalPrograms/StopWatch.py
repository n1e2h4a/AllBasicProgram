import time
try:
    Start = int(input("Enter 1 to start time:--"))
    Start=time.time()
    print(Start)

    End = int(input('Enter 4 to End time:--'))
    End=time.time()
    print(End)

    Elapsed = End - Start
    print("The time gap between  the Start and End {}".format(Elapsed))
except:
    print("valid time provide!")
