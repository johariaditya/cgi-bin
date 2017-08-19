#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

#Data is retrieved
data=cgi.FieldStorage()
choice=data.getvalue('ch')




if  choice == "Firefox":

	print "<META HTTP-EQUIV='refresh' content='0; url=/firefox.tar'/>"
	
	
elif  choice == "Calculator":

	print "<META HTTP-EQUIV='refresh' content='0; url=/calculator.tar'>"
	
elif  choice == "Webcam":

	print "<META HTTP-EQUIV='refresh' content='0; url=/webcam.tar'>"

elif  choice == "Screenshot":

	print "<META HTTP-EQUIV='refresh' content='0; url=/screenshot.tar'>"

elif  choice == "Office":

	print "<META HTTP-EQUIV='refresh' content='0; url=/office.tar'>"

elif  choice == "VLC":

	print "<META HTTP-EQUIV='refresh' content='0; url=/vlc.tar'>"


