yum install iscsi-initiator-utils -y
iscsiadm --mode node --targetname drive1 --portal 192.168.122.240:3260 --login
