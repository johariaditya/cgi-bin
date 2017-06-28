#!/usr/bin/python2

import os,commands,time,socket,sys
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sip="192.168.122.240"
s_port=8888

drive_name=raw_input("Enter storage drive name: ")
drive_size=raw_input("Enter drive size MB : ")
s.sendto(drive_name,(sip,s_port))
s.sendto(drive_size,(sip,s_port))

res=s.recvfrom(4)
if res[0] == "done":
	os.system('mkdir /media/'+drive_name)
	os.system('mount '+s_ip+':/mnt/'+drive_name+'  /media/'+drive_name)
else:
	print "No response from storage cloud"
