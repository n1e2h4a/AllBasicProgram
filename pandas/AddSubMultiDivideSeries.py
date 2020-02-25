import pandas as pd
samplespace1=pd.Series([4,8,12,16,20])
samplespace2=pd.Series([2,4,6,8,10])
sumresult = samplespace1+samplespace2
print("Add of two pandas series:-")
print(sumresult)
print("Substraction of two pandas series:-")
subresult = samplespace1-samplespace2
print(subresult)
print("multiplication of two pandas series:-")
multiresult = samplespace1*samplespace2
print(multiresult)
print("Division of two pandas series:-")
Divresult = samplespace1/samplespace2
print(Divresult)

