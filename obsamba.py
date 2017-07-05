#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"

data=cgi.FieldStorage()
dname=data.getvalue('dname')
ip=data.getvalue('ip')


commands.getstatusoutput('sudo mkdir /{}'.format(dname))
commands.getstatusoutput('sudo chmod o+w /{}'.format(dname))
commands.getstatusoutput('sudo echo [{}] >> /etc/samba/smb.conf'.format(dname))
commands.getstatusoutput('sudo echo path =/{} >> /etc/samba/smb.conf'.format(dname))
commands.getstatusoutput('sudo echo hosts allow={} >> /etc/samba/smb.conf'.format(ip))
commands.getstatusoutput('sudo echo writable=yes >> /etc/samba/smb.conf')
commands.getstatusoutput('sudo echo valid users=test >> /etc/samba/smb.conf')
commands.getstatusoutput('sudo echo browsable=yes >> /etc/samba/smb.conf')
commands.getstatusoutput('sudo echo  >> /etc/samba/smb.conf')
commands.getstatusoutput('sudo systemctl restart smb')
commands.getstatusoutput('sudo systemctl enable smb')

commands.getstatusoutput('sudo echo yum install cifs-utils samba-client -y > obsambaclient.sh')
commands.getstatusoutput('sudo echo mkdir /media/{} >> obsambaclient.sh'.format(dname))
commands.getstatusoutput('sudo echo mount -o username=test //192.168.122.240/{} /media/{} >> obsambaclient.sh'.format(dname,dname))

commands.getstatusoutput('sudo chmod   +x   obsambaclient.sh')



tar_cmd="sudo tar cvf     ../html/obsambaclient.tar    obsambaclient.sh"
tar_create=commands.getstatusoutput(tar_cmd)

print "<META HTTP-EQUIV='refresh' content='0; url=/obsambaclient.tar'>"


	

