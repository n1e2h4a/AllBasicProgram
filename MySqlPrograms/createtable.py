import mysql.connector

db = mysql.connector.connect(host='localhost', user='root',database="pycharm",password="neha")
myCursor = db.cursor()
tbl="create table myprogram(name varchar(50),rank int not null,city varchar(50))"
myCursor.execute(tbl)
db.commit()
