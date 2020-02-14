year=int(input("Enter any year to check leap year: "))
try:
    if ((year % 4 == 0) or ((year % 400 == 0 ) and (year % 100 != 0))):
        print("%d is leap year" %year)
    else:
        print("%d is not leap year" %year)
except:
    print("Provide Right Input")
