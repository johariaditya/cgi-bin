#!/usr/bin/python2

import os,commands,time,socket,sys,cgitb,cgi

cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print " "
data=cgi.FieldStorage()
d_name=data.getvalue('dname')
d_size=data.getvalue('dsize')
cliaddr=data.getvalue('ip')





lvcreate=commands.getstatusoutput('sudo lvcreate --name '+d_name+' --size '+d_size+'M adhocvg -y')
lvformat=commands.getstatusoutput('sudo mkfs.ext4 /dev/adhocvg/'+d_name)
lvmkdir=commands.getstatusoutput('sudo mkdir /mnt/'+d_name)
commands.getstatusoutput('exportfs -arv')
os.system('sudo mount /dev/adhocvg/'+d_name+' /mnt/'+d_name)

entry="/mnt/"+d_name+" " +cliaddr+ "(rw,no_root_squash) "

f=open('/etc/exports','a')
f.write(entry)
f.write("\n")
f.close()
os.system('sudo systemctl restart nfs-server')
os.system('sudo systemctl enable nfs-server')
commands.getstatusoutput('exportfs -arv')



make_dr='sudo echo mkdir /media/{} > obclientlinux.sh'.format(d_name)
make_sh='sudo echo mount 192.168.122.240:/mnt/{}   /media/{}>> obclientlinux.sh'.format(d_name,d_name)
make_dir=commands.getstatusoutput(make_dr)
make_sh_file=commands.getstatusoutput(make_sh)

perm=commands.getstatusoutput('sudo chmod   +x   obclientlinux.sh')



tar_cmd="sudo tar cvf     ../html/obclient.tar    obclientlinux.sh"
tar_create=commands.getstatusoutput(tar_cmd)

print "<META HTTP-EQUIV='refresh' content='0; url=/obclient.tar'>"

