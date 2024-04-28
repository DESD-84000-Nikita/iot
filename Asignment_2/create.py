# import module of mysql connector
import dbconn

# create a query
empid = int(input("Enter empid : "))
name = input("Enter name : ")
department = input("Enter department : ")
email = input("Enter email  :")
salary = float(input("Enter salary : "))
DOJ = float(input("Enter Date of joining : "))



query = f"insert into employee values({empid}, '{name}', '{department}', '{email}', {salary},{DOJ});"








