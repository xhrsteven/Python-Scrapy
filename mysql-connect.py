import mysql.connector

try:
    conn = mysql.connector.connect(database="cookbook",
                                   host="localhost",
                                   user="root",
                                   password="Raining2301")
    print("Connected")
except:
    print("cannot connect to server")



