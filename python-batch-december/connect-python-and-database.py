# pip install mysql-connector-python

import mysql.connector

conn = mysql.connector.connect(host = "localhost", username = "root", password = "1234", database = "saturday")

mycurser = conn.cursor()

# mycurser.execute("insert into contactus values('python', '98234693', 'python@gmail.com', 'this is python message', 20, 'this is python address')")

# conn.commit()

mycurser.execute("select * from contactus")

data = mycurser.fetchall()

print(data)
