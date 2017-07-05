#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb

cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print ""

data=cgi.FieldStorage()
dname=data.getvalue('dname')
dsize=data.getvalue('dsize')

commands.getstatusoutput('sudo lvcreate --name {} --size {}M adhocvg -y'.format(dname,dsize))
commands.getstatusoutput('sudo echo "<target {}>" >>/etc/tgt/targets.conf'.format(dname))
commands.getstatusoutput('sudo echo "backing-store /dev/myadhocvg/{}" >>/etc/tgt/targets.conf'.format(dname))
commands.getstatusoutput('sudo echo "</target>" >>/etc/tgt/targets.conf'.format(dname))
commands.getstatusoutput('sudo echo " " >>/etc/tgt/targets.conf')

commands.getstatusoutput('sudo systemctl restart tgtd')
commands.getstatusoutput('sudo systemctl enable tgtd')

os.system('sudo echo yum install iscsi-initiator-utils -y > /var/www/cgi-bin/bstorage.sh')
os.system('sudo echo iscsiadm --mode node --targetname {} --portal 192.168.122.240:3260 --login >> /var/www/cgi-bin/bstorage.sh'.format(dname))

commands.getstatusoutput('sudo chmod   777   bstorage.sh')

commands.getstatusoutput('sudo tar cvf     ../html/blockstorage.tar    bstorage.sh')



print "<META HTTP-EQUIV='refresh' content='0; url=/blockstorage.tar'>"




