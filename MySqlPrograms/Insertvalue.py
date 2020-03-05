import mysql.connector

db = mysql.connector.connect(host='localhost', user='root',database="pycharm",password="neha")
myCursor = db.cursor()
#tbl="create table myprogram(name varchar(50),rank int not null,city varchar(50))"
new="insert into myprogram(name,rank,city)values(%s,%s,%s)"
new1=[("neha",1,"delhi"),("nehu",2,"delhi"),("jolly",3,"mumbai"),("amit",4,"indore")]


myCursor.executemany(new,new1)
db.commit()
