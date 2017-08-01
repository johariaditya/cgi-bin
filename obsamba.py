#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb
import mysql.connector as mariadb

#connection is establshed between mysql and python
mariadb_connection = mariadb.connect(user='root', password='redhat', database='adhoc')
cursor = mariadb_connection.cursor()

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

#Data is retrieved
data=cgi.FieldStorage()
dname=data.getvalue('dname')
ip=data.getvalue('ip')

try:
	#Data is inserted into the database	
	cursor.execute("INSERT INTO drive (drivename,drivesize) VALUES (%s,%s)",(dname,'NA'))
	mariadb_connection.commit()
	
	#Directory that is to be mounted is created
	commands.getstatusoutput('sudo mkdir /{}'.format(dname))
	#Permissions are given 
	commands.getstatusoutput('sudo chmod o+w /{}'.format(dname))
	#Samba configuration file is appended with the drive name 
	commands.getstatusoutput('sudo echo [{}] >> /etc/samba/smb.conf'.format(dname))
	commands.getstatusoutput('sudo echo path =/{} >> /etc/samba/smb.conf'.format(dname))
	commands.getstatusoutput('sudo echo hosts allow={} >> /etc/samba/smb.conf'.format(ip))
	commands.getstatusoutput('sudo echo writable=yes >> /etc/samba/smb.conf')
	commands.getstatusoutput('sudo echo valid users=test >> /etc/samba/smb.conf')
	commands.getstatusoutput('sudo echo browsable=yes >> /etc/samba/smb.conf')
	commands.getstatusoutput('sudo echo  >> /etc/samba/smb.conf')
	
	#Samba services are restarted and enabled
	commands.getstatusoutput('sudo systemctl restart smb')
	commands.getstatusoutput('sudo systemctl enable smb')

	
	#Client file is created
	commands.getstatusoutput('sudo echo yum install cifs-utils samba-client -y > obsambaclient.sh')
	commands.getstatusoutput('sudo echo mkdir /media/{} >> obsambaclient.sh'.format(dname))
	commands.getstatusoutput('sudo echo mount -o username=test //192.168.122.240/{} /media/{} >> obsambaclient.sh'.format(dname,dname))

	#permission are given to the client side	
	commands.getstatusoutput('sudo chmod   +x   obsambaclient.sh')

	#tar file of the client file is created
	tar_cmd="sudo tar cvf     ../html/obsambaclient.tar    obsambaclient.sh"
	tar_create=commands.getstatusoutput(tar_cmd)

	print "<META HTTP-EQUIV='refresh' content='0; url=/obsambaclient.tar'>"


	
except mariadb.Error as error:
	#if there is an error during the data insertion, error message is displayed	
	print "<script>alert('Drive name already exists/blank entry, please try again')</script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=/obsamba.html'/>"



