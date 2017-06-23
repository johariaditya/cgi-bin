#!/usr/bin/python2
import os,sys,time
import commands
import cgi,cgitb
import socket

cgitb.enable()
print "Content-type:text/html\r\n\r\n"
print ""



s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sip="192.168.122.240"
s_port=8888

os.system("SSHPASS='123' sshpass -e ssh -X test@"+sip+" firefox &")
time.sleep(3)




