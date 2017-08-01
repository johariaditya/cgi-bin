#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print ""

#Data is retrieved
data=cgi.FieldStorage()
choice=data.getvalue('ch')




if  choice == "python":
	commands.getoutput('sudo docker start 8104b5559246')
	x=commands.getoutput('sudo docker exec -it 8104b555924 /usr/bin/python')
	print "<a href='http://192.168.122.1:4200'>"
	print "Username is user4 and password is redhat to start coding"
	print "</a>"
	
	
elif  choice == "perl":

	commands.getoutput('sudo docker start 8104b5559246')
	x=commands.getoutput('sudo docker exec -it 8104b555924 /usr/bin/perl')
	print "<a href='http://192.168.122.1:4200'>"
	print "Username is user6 and password is redhat to start coding"
	print "</a>"
	

elif  choice == "ruby":

	commands.getoutput('sudo docker start 8104b5559246')
	x=commands.getoutput('sudo docker exec -it 8104b555924 /usr/bin/ruby')
	print "<a href='http://192.168.122.1:4200'>"
	print "Username is user5 and password is redhat to start coding"
	print "</a>"
	



