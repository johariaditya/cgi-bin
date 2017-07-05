yum install iscsi-initiator-utils -y
iscsiadm --mode node --targetname yo --portal 192.168.122.240:3260 --login
