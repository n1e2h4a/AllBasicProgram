# import date function from datetime package
from datetime import date

# input year , month and day 2 times for extracting difference of days
FirstYear = int(input("enter the Year:--"))
FirstMonth = int(input("enter the month:--"))
FirstDay = int(input("enter the day:--"))
SecondYear = int(input("enter the Year:--"))
SecondMonth = int(input("enter the month:--"))
SecondDay = int(input("enter the day:--"))
# passing inputs in date function
First = date(FirstYear, FirstMonth, FirstDay)
Second = date(SecondYear, SecondMonth, SecondDay)
Days = Second - First
# print difference between the dates
print(f'Number of Days between the Dates', Days.days)
