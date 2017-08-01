#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"


#Choice is retrieved
data=cgi.FieldStorage()
choice=data.getvalue('ch')

#Condition if the choice is linux
if  choice == "linux":

	print "<META HTTP-EQUIV='refresh' content='0; url=/info.html'>"
	

#Condition if the choice is windows	
elif  choice == "windows":

	print "<META HTTP-EQUIV='refresh' content='0; url=/obsamba.html'>"
	

