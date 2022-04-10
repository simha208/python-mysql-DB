
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="simha1234!",
  database="sakila"
)


mycursor = mydb.cursor()

mycursor.execute("select * from actor ")
actor= mycursor.fetchall()

for x in actor:
  print("first name:", x[1])
  print("last name:",x[2])