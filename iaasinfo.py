#!/usr/bin/python2

import os,commands,time,socket,sys,cgitb,cgi

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

data=cgi.FieldStorage()

#Taking os name as input
osname=data.getvalue('osname')
#Taking os cpu as input
oscpu=data.getvalue('oscpu')
#Taking os ram as input
osram=data.getvalue('osram')
#Taking os hard disk as input
oshdd=data.getvalue('oshdd')
#Taking port number as input
portno=data.getvalue('portno')

#Conditon to check the osname and os hardisk
if osname=="rhel7" and oshdd=="no":
	#Creating a snaphot of the pre-installed os
	image=commands.getstatusoutput('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhel7.1.qcow2 /var/lib/libvirt/images/{}.qcow2'.format(osname))
	print image
	#Installing the virtual os on the virtua manager
	install=commands.getstatusoutput('sudo virt-install --name {} --ram {} --vcpu {} --disk path=/var/lib/libvirt/images/{}.qcow2 --import --graphics vnc,listen=192.168.122.1,port=5989 --noautoconsole '.format(osname,osram,oscpu,osname))
	print install	
	#Using websockify to allow the user to access the os from the browser
	os.system('sudo websockify -D --web=/usr/share/novnc {} 192.168.122.1:5989'.format(portno))	
	print "<META HTTP-EQUIV=refresh content='0; url=http://192.168.122.1:{}'/>".format(portno)

elif osname=="rhel7":
	#Creating a snapshot of the os
	image=commands.getstatusoutput('sudo qemu-img create -f qcow2 -b /var/lib/libvirt/images/rhel7.1.qcow2 /var/lib/libvirt/images/{}.qcow2'.format(osname))
	print image
	#Installing the os with the specific requirements
	install=commands.getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.122.1,port=5989 --cdrom /root/Downloads/rhel.iso --ram {} --vcpu {}  --disk path=/var/lib/libvirt/images/{}.qcow2,size={} --name {} --noautoconsole '.format(osram,oscpu,osname,oshdd,osname))
	print install	
	#Using websockify to allow the user to access the os from the browser
	os.system('sudo websockify -D --web=/usr/share/novnc {} 192.168.122.1:5989'.format(portno))	
	print "<META HTTP-EQUIV=refresh content='0; url=http://192.168.122.1:{}'/>".format(portno)

if osname=="kali" and oshdd=="no":
	#Creating a snapshot of the os
	install=commands.getstatusoutput('sudo virt-install --graphics vnc,listen=192.168.122.1,port=5989 --cdrom /root/Downloads/kali.iso --ram {} --vcpu {}  --nodisk --name {} --noautoconsole '.format(osram,oscpu,osname))
	print install	
	#Using websockify to allow the user to access the os from the browser	
	os.system('sudo websockify -D --web=/usr/share/novnc {} 192.168.122.1:5989'.format(portno))	
	print "<META HTTP-EQUIV=refresh content='0; url=http://192.168.122.1:{}'/>".format(portno)

elif osname=="kali":
	#Error message if kali is not run in live mode
	print "<script>alert('Kali does not require any hard disk. Please choose the LIVE option')</script>"	
	print "<META HTTP-EQUIV='refresh' content='0; url=/iaasinfo.html'>"


