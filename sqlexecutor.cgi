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

def connect_db(db_name):
	db = conn.connect(host='localhost', user='root',passwd="",database=db_name)
	cursor = db.cursor()
	return db,cursor

def connect_db():
	db = conn.connect(host='localhost', user='root',passwd="")
	cursor = db.cursor()
	return db,cursor

if __name__ == "__main__":
	try:
		htmlTop()
		db,cursor = connect_db()
		sql = "drop database studentdatabase"
		cursor.execute(sql)
		db.commit()
		cursor.close()
		htmlTail()
	except:
		cgi.print_exception()