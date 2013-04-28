<!--
	AUTHOR : MANOJ E.
	CREATED ON : 25 Apr 2013
	MODIFIED ON : 25 Apr 2013
-->

<html>
<head>
	<title>Login Page</title>
</head>
<body>
	<?php
		function login($username, $password){
			if( $username != "" && $password != "" ){
				/*Establish a connection to the localhost*/
				$stat = mysql_connect("localhost","root","");
				
				if(!$stat){
					die("Cannot connect to server. Try again layer");
				}
				
				echo "Manoj";
				
				/*Connection has been established*/
				/*Select a database now*/
				
				$stat1 = mysql_select_db('user_authentication');
				
				if( !$stat1 ){
					die("Cannot open database");
				}
				
				/*Database opened for use*/
				
				
			}
		}
	?>
</body>