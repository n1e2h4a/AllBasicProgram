import mysql.connector

db = mysql.connector.connect(host='localhost', user='root',database="pycharm",password="neha")
myCursor = db.cursor()
myCursor.execute("Select * from myprogram")
myresult=myCursor.fetchall()
for row in myresult:
    print(row)