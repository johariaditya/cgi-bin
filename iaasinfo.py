#!/usr/bin/python2

import os,commands,time,socket,sys,cgitb,cgi

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

data=cgi.FieldStorage()
osname=data.getvalue('osname')
oscpu=data.getvalue('oscpu')
osram=data.getvalue('osram')
oshdd=data.getvalue('oshdd')
portno=data.getvalue('portno')

if osname=="rhel7" and oshdd=="no":
	image=commands.getstatusoutput('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhel7.1.qcow2 /var/lib/libvirt/images/{}.qcow2'.format(osname))
	print image
	install=commands.getstatusoutput('sudo virt-install --name {} --ram {} --vcpu {} --disk path=/var/lib/libvirt/images/{}.qcow2 --import --graphics vnc,listen=192.168.122.1,port=5989 '.format(osname,osram,oscpu,osname))
	print install	
	os.system('websockify --web=/usr/share/novnc {} 192.168.122.1:5989'.format(portno))	



print "<META HTTP-EQUIV='refresh' content='0; url=/iaasclient.sh'>"

