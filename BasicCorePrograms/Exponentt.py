Exponent = int(input('Enter the Exponent Value:- '))
Number = 2
i = 0
while (i <= Exponent):
    power = Number ** i
    i = i + 1
    if ((power % 4 == 0) or ((power % 400 == 0) and (power % 100 != 0))):
        print("%d = is a Leap Year" % power)
    else:
        print("%d = is  not a Leap Year" % power)
