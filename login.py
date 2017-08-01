#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

import mysql.connector as mariadb

#Establishing a connection between the database and python
mariadb_connection = mariadb.connect(user='root', password='redhat', database='login')
cursor = mariadb_connection.cursor()

cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print ""

data=cgi.FieldStorage()

#Retrieving the values of username and password from the user
uname=data.getvalue('usr')
passwd=data.getvalue('passwd')

#Selecting the values from the database
cursor.execute("SELECT username,password FROM login")
flag=0;

#Checking whether the input username and password matches that in the databse
for username, password in cursor:
	if  uname == username and passwd == password:
		flag=1;
		break;
	
	elif uname!=username or passwd!=password:
		flag=0;
		

#If there is a match, the user is logged in	
if flag==1:
	print "<META HTTP-EQUIV='refresh' content='0; url=/services.html'>"

#If there is not a match the user is not allowed further
elif flag==0:
	print "<script>alert('Wrong Password')</script>" 
	print "<META HTTP-EQUIV='refresh' content='0; url=/index.html'/>"	


