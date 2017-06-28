#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

data=cgi.FieldStorage()
choice=data.getvalue('ch')


#a=commands.getstatusoutput("sudo cat /var/www/html/users.txt | grep "+username+" | awk '{print $1}'")
#b=commands.getstatusoutput("sudo cat /var/www/html/users.txt | grep "+username+" | awk '{print $3}'")



if  choice == "Firefox":

	print "<META HTTP-EQUIV='refresh' content='0; url=/firefox.sh'/>"
	
	
elif  choice == "Calculator":

	print "<META HTTP-EQUIV='refresh' content='0; url=/calculator.sh'>"
	
elif  choice == "Webcam":

	print "<META HTTP-EQUIV='refresh' content='0; url=/webcam.sh'>"

elif  choice == "Screenshot":

	print "<META HTTP-EQUIV='refresh' content='0; url=/screenshot.sh'>"

elif  choice == "Office":

	print "<META HTTP-EQUIV='refresh' content='0; url=/office.sh'>"

elif  choice == "VLC":

	print "<META HTTP-EQUIV='refresh' content='0; url=/vlc.tar'>"


