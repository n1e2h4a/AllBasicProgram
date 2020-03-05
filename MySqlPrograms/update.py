import mysql.connector

db = mysql.connector.connect(host='localhost', user='root',database="pycharm",password="neha")
myCursor = db.cursor()
new="update myprogram set name='niharika',city='bhopal' where rank=1"
myCursor.execute(new)
db.commit()
