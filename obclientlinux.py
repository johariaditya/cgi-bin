#!/usr/bin/python2

import os,commands,time,socket,sys,cgitb,cgi

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

data=cgi.FieldStorage()
d_name=data.getvalue('dname')
d_size=data.getvalue('dsize')
os.system('sudo lvcreate --name '+d_name+' --size '+d_size+'M adhocvg')

os.system('sudo mkfs.ext4  /dev/adhocvg/' +d_name)

os.system(' sudo mkdir /mnt/' +d_name)

os.system('sudo mount /dev/adhocvg/' +d_name+' /mnt/' +d_name)

os.system('sudo yum install nfs-utils -y')

entry="/mnt/"+d_name+" " +cliaddr+ "(rw,no_root_squash) "

f=open('/etc/exports','a')
f.write(entry)
f.write("\n")
f.close()
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
	
