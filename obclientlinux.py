#!/usr/bin/python2

import os,commands,time,socket,sys,cgitb,cgi

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

#Retrieving the values of drive name and drive size from the user
data=cgi.FieldStorage()
d_name=data.getvalue('dname')
d_size=data.getvalue('dsize')

#Creating the logical volume
os.system('sudo lvcreate --name '+d_name+' --size '+d_size+'M adhocvg')

#Formatting the drive with ext4 
os.system('sudo mkfs.ext4  /dev/adhocvg/' +d_name)

#Creating a directory of the corresponding drive
os.system(' sudo mkdir /mnt/' +d_name)

#Mounting the drive on to the server
os.system('sudo mount /dev/adhocvg/' +d_name+' /mnt/' +d_name)

#Installing the software, if not present
os.system('sudo yum install nfs-utils -y')

#Entering the data into the export file
entry="/mnt/"+d_name+" " +cliaddr+ "(rw,no_root_squash) "

f=open('/etc/exports','a')
f.write(entry)
f.write("\n")
f.close()

#Restarting and enabling the nfs server
os.system('systemctl restart nfs-server')
os.system('systemctl enable nfs-server')
entry="""
#!/usr/bin/python2

import os,commands,time,socket,sys

os.system('echo dname') """


f=open('/var/www/html/obclientlinux.sh','w')
f.write(entry)
f.write("\n")
f.close()

print "<META HTTP-EQUIV='refresh' content='0; url=/test.sh'>"
	
