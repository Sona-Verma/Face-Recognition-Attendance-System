import mysql.connector
#conn=mysql.connector.connect(host="localhost",user="root",password="123456789",database="face_recognizer")
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456789",database="face_recognizer")
mycursor=mydb.cursor()
update="UPDATE student SET Dep='a' WHERE Student id='1'"
#value=("a","1")
mycursor.execute(update)
#result=mycursor.fetchall()
#for i in result:
 #   print(i)
 