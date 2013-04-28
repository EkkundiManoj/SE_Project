#	AUTHOR : Manoj E.
#	Created On : 21 Apr 2013
#	Modified On : 21 Apr 2013

#	The following Python file is used
#	by the Faculty user to view
#	his/her profile.

#	The following import is essential
#	as it is used to interface between
#	the database and the program

import MySQLdb;

def viewFacultyProfile(facid):
	try:
		db = MySQLdb.connect("localhost","root","manoj","faculty_details");
		cursor = db.cursor();
		sqlQuery = "SELECT * FROM FACULTY_DETAILS WHERE FACID = \'" + facid + "\'";
		cursor.execute(sqlQuery);
		resultSet = cursor.fetchall();
		print(resultSet);
		db.commit();
	except:
		db.rollback();
	finally:
		db.close();
	return;

viewFacultyProfile('fac001');
