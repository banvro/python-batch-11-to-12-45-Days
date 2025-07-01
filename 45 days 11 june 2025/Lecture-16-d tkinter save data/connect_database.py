import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    port = 3307,
    username = "root",
    password = "1234",
    database = "morning11"
)

cuer = conn.cursor()

cuer.execute("insert into student_info values(105, 'r', '99999999', 'this is rr addesssss')")
cuer.execute("insert into student_info values(106, 'swift', '8888888', 'this is swif addesssss')")
cuer.execute("insert into student_info values(107, 'pascal', '777772635', 'this is pascial addesssss')")

conn.commit()