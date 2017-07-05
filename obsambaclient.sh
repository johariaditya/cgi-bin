yum install cifs-utils samba-client -y
mkdir /media/hello
mount -o username=test //192.168.122.240/hello /media/hello
