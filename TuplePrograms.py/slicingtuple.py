top = (2,3,6,7,8,7,9,0,5,4,3,2,8,9,4)
#used tuple[start:stop] the start index is inclusive and the stop index
slice = top[3:5]
#is exclusive
print(slice)
#if the start index isn't defined, is taken from the beg inning of the tuple
_slice = top[:6]
print(_slice)
#if the end index isn't defined, is taken until the end of the tuple
_slice = top[5:]
print(_slice)
#if neither is defined, returns the full tuple
_slice = top[:]
print(_slice)
#The indexes can be defined with negative values
_slice = top[-8:-4]
print(_slice)
#create another tuple
top = tuple("PYTHON EASY")
print(top)
#step specify an increment between the elements to cut of the tuple
#tuple[start:stop:step]
_slice = top[2:9:2]
print(_slice)
#returns a tuple with a jump every 3 items
_slice = top[::4]
print(_slice)
#when step is negative the jump is made back
slice = top[9:2:-4]
print(_slice)
