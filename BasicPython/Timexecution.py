import time
try:
    def sumofnumbers(n):
        starttime = time.time()
        sum=0
        for i in range(1,n+1):
            sum = sum+i
        endtime = time.time()
        return sum,endtime-starttime
    N=int(input("Enter the number:---"))
    print("\n time taken to sum 1 to ",N,"and time to calculate is:", sumofnumbers(N))
except:
    print("Enetr valid Number:---")