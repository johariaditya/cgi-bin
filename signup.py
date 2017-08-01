#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

import mysql.connector as mariadb


cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print ""


mariadb_connection = mariadb.connect(user='root', password='redhat', database='login')
cursor = mariadb_connection.cursor()


data=cgi.FieldStorage()
uname=data.getvalue('uname')
passwd=data.getvalue('pass')

try:
	cursor.execute("INSERT INTO login (username,password) VALUES (%s,%s)", (uname,passwd))
	mariadb_connection.commit()
	print "<script>alert('Username created!')</script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=/index.html'/>"

except mariadb.Error as error:
	print "<script>alert('Username already exists/blank entry, please try again')</script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=/signup.html'/>"


	



