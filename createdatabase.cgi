#!C:\Users\PUJITH SAI KUMAR K\AppData\Local\Programs\Python\Python37-32\python.exe

import cgi
import mysql.connector as conn

def htmlTop():
	print("""Content-type:text/html\n\n
			<!DOCTYPE html>
			<html lang="en">
				<head>
					<meta charset="utf-8"/>
					<title>My server-side template</title>
				</head>
				<body>""")

def htmlTail():
	print("""</body>
			</html>""")

def connectDB():
	db = conn.connect(host='localhost',user='root')
	cursor = db.cursor()
	return db,cursor

def createDB(db,cursor):
	#create a new database
	sql = "create database studentDataBase"
	cursor.execute(sql)
	db.commit()

def createEntity(db,cursor):
	#use the newly created database
	sql = "use studentDataBase"
	cursor.execute(sql)
	#create a simple entity
	sql = '''create table Student
			(StudentID int not null auto_increment,
			firstName varchar(25) not null,
			lastName varchar(25) not null,
			fatherFirstName varchar(25) not null,
			fatherLastName varchar(25) not null,
			gender char(7) not null,
			DOB DATE not null,
			address varchar(50) not null,
			state varchar(30) not null,
			city varchar(20) not null,
			pincode int(6) not null,
			emailID varchar(50) not null unique,
			phoneNo text(10) not null,
			password varchar(255) not null,			
			creationDateTime DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
			primary key(StudentID,emailID))'''
	cursor.execute(sql)
	db.commit()
#main Program
if __name__ == "__main__":
	try:
		htmlTop()
		db,cursor = connectDB()
		createDB(db,cursor)
		createEntity(db,cursor)
		#close the connection to the database
		cursor.close()
		print("Database and table created successfully")
		htmlTail()
	except:
		cgi.print_exception()