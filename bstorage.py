#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='root', password='redhat', database='adhoc')
cursor = mariadb_connection.cursor()

cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print ""

data=cgi.FieldStorage()
#Taking the drive name as input
dname=data.getvalue('dname')
#Taking the drive size as input
dsize=data.getvalue('dsize')

try:
	cursor.execute("INSERT INTO drive (drivename,drivesize) VALUES (%s,%s)", (dname,dsize))
	mariadb_connection.commit()
	

	#Creating a logical volume
	commands.getstatusoutput('sudo lvcreate --name {} --size {}M adhocvg -y'.format(dname,dsize))

	#Writing in to the targets.conf file
	commands.getstatusoutput('sudo echo "<target {}>" >>/etc/tgt/targets.conf'.format(dname))
	commands.getstatusoutput('sudo echo "backing-store /dev/myadhocvg/{}" >>/etc/tgt/targets.conf'.format(dname))
	commands.getstatusoutput('sudo echo "</target>" >>/etc/tgt/targets.conf'.format(dname))
	commands.getstatusoutput('sudo echo " " >>/etc/tgt/targets.conf')

	#Restarting and enabling tgtd
	commands.getstatusoutput('sudo systemctl restart tgtd')
	commands.getstatusoutput('sudo systemctl enable tgtd')

	#installation if iscsi utils if not present
	os.system('sudo echo yum install iscsi-initiator-utils -y > /var/www/cgi-bin/bstorage.sh')

	#Preparing the code for he client side
	os.system('sudo echo iscsiadm --mode node --targetname {} --portal 192.168.122.240:3260 --login >> /var/www/cgi-bin/bstorage.sh'.format(dname))

	#Giving the client side file the permission of execution
	commands.getstatusoutput('sudo chmod  +x   bstorage.sh')

	#Creating a tar file of the file
	commands.getstatusoutput('sudo tar cvf     ../html/blockstorage.tar    bstorage.sh')



	print "<META HTTP-EQUIV='refresh' content='0; url=/blockstorage.tar'>"



except mariadb.Error as error:
	print "<script>alert('Drive name already exists/blank entry, please try again')</script>"
	print "<META HTTP-EQUIV='refresh' content='0; url=/bstorage.html'/>"




