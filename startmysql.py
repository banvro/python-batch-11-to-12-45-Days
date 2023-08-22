# DataBase : 
    # Mysql
    # Postgrace
    # SQllite

# sql = structured query language

# 1) DDl
# 2) DML
# 3) DCl
# 4) TCL


# to install mysql connector the command is : 

    # pip install mysql-connector-python

import mysql.connector

conwc = mysql.connector.connect(host = "localhost", user = "root", password = "abc@123", database = "phone", auth_plugin='mysql_native_password')


# if conwc.is_connected():
#     print("database connected")

couser = conwc.cursor()

# z = couser.execute('create database laptop;')
# z = couser.execute('insert into mobileinfo values(1, "Apple", "Red", 10000);')

couser.execute('select * from mobileinfo where mobile_s_nmbr = 3;')

y = couser.fetchall()
# print(y)

for i in y:
    print(i)

conwc.commit()





# show databases;

# create database phone;

# use phone;

# create table mobileinfo(mobile_s_nmbr INT, mobile_name varchar(50), mobile_color varchar(30), mobile_price decimal);

# insert into mobileinfo values(1, "Apple", "Red", 10000);

# show tables;

# select * from mobileinfo;