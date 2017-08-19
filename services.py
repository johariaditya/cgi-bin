#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print ""

data=cgi.FieldStorage()
choice=data.getvalue('ch')


if  choice == "saas":
	print "<META HTTP-EQUIV='refresh' content='0; url=/saas.html'>"
	
	
elif choice == "staas":	
	 print "<META HTTP-EQUIV='refresh' content='0; url=/staas.html'>"
	
	
elif choice == "iaas":	
	 print "<META HTTP-EQUIV='refresh' content='0; url=/iaasinfo.html'>"

if  choice == "paas":
	print "<META HTTP-EQUIV='refresh' content='0; url=/paas.html'>"
	
