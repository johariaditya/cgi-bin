yum install cifs-utils samba-client -y
mkdir /media/drive2
mount -o username=test //192.168.122.240/drive2 /media/drive2
