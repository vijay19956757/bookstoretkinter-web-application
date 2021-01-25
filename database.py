import mysql.connector
conn = mysql.connector.connect(host ="localhost",user = "root",password = "",db ="bookstore")
cursor = conn.cursor()
print(conn)
