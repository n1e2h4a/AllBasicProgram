import mysql.connector

db = mysql.connector.connect(host='localhost', user='root',database="pycharm",password="neha")
myCursor = db.cursor()
#tbl="create table myprogram(name varchar(50),rank int not null,city varchar(50))"
new="delete from myprogram where city = 'delhi'"

myCursor.execute(new)
db.commit()
