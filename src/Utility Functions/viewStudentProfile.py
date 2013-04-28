#	AUTHOR : Manoj E.
#	Created On : 21 Apr 2013
#	Modified On : 21 Apr 2013

#	This Python function is used
#	by the Student user to view
#	his/her profile page.

#	The following import is used
#	to interface between Python
#	script and database

import MySQLdb;

#	This function is used to view
#	the student's profile page.
#	Argument 1 : is an unique identifier
#		     for the Student user

def viewStudentProfile(usn):
	try:
		db = MySQLdb.connect("localhost","root","manoj","student_details");	# Connect to database
		cursor = db.cursor();							# Create a cursor object to execute query
		sqlQuery = "SELECT * FROM STUDENT_DETAILS WHERE USN = \'" + usn + "\'";	# Form the query string
		cursor.execute(sqlQuery);						# Execute the query
		resultSet = cursor.fetchall();						# Fetch the result set
		print(resultSet);							# Print the result set
		db.commit();								# Commit on success
	except:
		db.rollback();								# Rollback on error
	finally:
		db.close();								# Close database in any case

viewStudentProfile('1PI10CS138');							# Example input 
