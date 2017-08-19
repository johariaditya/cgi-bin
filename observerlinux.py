#!/usr/bin/python2

import os,commands,time,socket,sys,cgitb,cgi
import mysql.connector as mariadb

#connection is establshed between mysql and python
mariadb_connection = mariadb.connect(user='root', password='redhat', database='adhoc')
cursor = mariadb_connection.cursor()

cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print " "

#Data is retrieved
data=cgi.FieldStorage()
d_name=data.getvalue('dname')
d_size=data.getvalue('dsize')
cliaddr=data.getvalue('ip')

try:
	#Data is inserted into the database	
	cursor.execute("INSERT INTO drive (drivename,drivesize) VALUES (%s,%s)",(d_name,d_size))
	mariadb_connection.commit()

	#Logical volume is created
	lvcreate=commands.getstatusoutput('sudo lvcreate -V'+d_size+'G --name '+d_name+' --thin adhocvg/pool1 -y')
	#The drive is formatted with ext4	
	lvformat=commands.getstatusoutput('sudo mkfs.ext4 /dev/adhocvg/'+d_name)
	
	#Directory which is to be mount from the server is created		
	lvmkdir=commands.getstatusoutput('sudo mkdir /mnt/'+d_name)
	commands.getstatusoutput('exportfs -arv')
	
	#The drive is then mounted on to the directory on the server side
	os.system('sudo mount /dev/adhocvg/'+d_name+' /mnt/'+d_name)

	entry="/mnt/"+d_name+" " +cliaddr+ "(rw,no_root_squash) "

	#Thr exports file is appended with the information about the drive
	f=open('/etc/exports','a')
	f.write(entry)
	f.write("\n")
	f.close()

	#nfs services are restarted and enabled
	os.system('sudo systemctl restart nfs-server')
	os.system('sudo systemctl enable nfs-server')
	commands.getstatusoutput('exportfs -arv')


	#The client side code is put into a file

	#The direcory is made on the client side on which the drive would be mounted
	commands.getstatusoutput('sudo echo mkdir /media/{} > obclientlinux.sh'.format(d_name))

	#The drive from the server side is mounted on to the client side
	commands.getstatusoutput('sudo echo mount 192.168.122.240:/mnt/{}   /media/{}>> obclientlinux.sh'.format(d_name,d_name))
	#make_dir=commands.getstatusoutput(make_dr)
	#make_sh_file=commands.getstatusoutput(make_sh)

	#Executable Permission is given to the client file	
	perm=commands.getstatusoutput('sudo chmod   +x   obclientlinux.sh')


	#Tar file is created of the client file
	tar_cmd="sudo tar cvf     ../html/obclient.tar    obclientlinux.sh"
	tar_create=commands.getstatusoutput(tar_cmd)

	print "<META HTTP-EQUIV='refresh' content='0; url=/obclient.tar'>"

except mariadb.Error as error:
	#if there is an error during the data insertion, error message is displayed	
	print "<script>alert('Drive name already exists/blank entry, please try again')</script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=/info.html'/>"

