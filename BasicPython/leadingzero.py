mystring="python"
#print original string
print("the original string :--- "+ str(mystring))
#no of zeros want
zero=5
#using rjust()for for adding leading zero
final=mystring.rjust(zero + len(mystring), '0')
print("string after adding leading zeros : " + str(final))