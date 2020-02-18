from datetime import datetime
#datetime object containing current date and time
now = datetime.now()
print("now =", now)
#dd/mm/yy H:M:S
dt_string =now.strftime("%d/%m/%y  %H:%M:%S")
print("date and time =", dt_string)