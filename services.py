#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print ""

data=cgi.FieldStorage()
choice=data.getvalue('ch')


#a=commands.getstatusoutput("sudo cat /var/www/html/users.txt | grep "+username+" | awk '{print $1}'")
#b=commands.getstatusoutput("sudo cat /var/www/html/users.txt | grep "+username+" | awk '{print $3}'")



if  choice == "saas":
	print "<META HTTP-EQUIV='refresh' content='0; url=/saas.html'>"
	
	
elif choice == "staas":	
	 print "<META HTTP-EQUIV='refresh' content='0; url=/staas.html'>"
	


