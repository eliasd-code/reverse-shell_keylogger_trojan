#!/bin/bash
echo "this script only works if you run it as root!"
echo "arch or debian based?  arch/debian"
read answer
if [ "$answer" == "arch" ]
then    
        echo "update"
        sudo pacman -Syu
        sudo pacman -S vsftpd
        sudo useradd -m ftpuser
        passwd ftpuser
else
        echo "update"
        sudo apt update
        sudo apt install vsftpd
        sudo adduser ftpuser
fi
echo "new password for ftpuser"
sudo cp /etc/vsftpd.conf /etc/vsftpd.conf.orig
sudo mkdir /home/ftpuser/ftp
sudo chown nobody:nobody /home/ftpuser/ftp
sudo chmod a-w /home/ftpuser/ftp
sudo mkdir /home/ftpuser/ftp/files
sudo chown ftpuser:ftpuser /home/ftpuser/ftp/files
echo "write_enable=YES" >> /etc/vsftpd.conf
echo "chroot_local_user=YES" >> /etc/vsftpd.conf
echo "user_sub_token=$USER" >> /etc/vsftpd.conf
echo "local_root=/home/$USER/ftp" >> /etc/vsftpd.conf
echo "pasv_min_port=40000" >> /etc/vsftpd.conf
echo "pasv_max_port=50000" >> /etc/vsftpd.conf
echo "userlist_enable=YES" >> /etc/vsftpd.conf
echo "userlist_deny=NO" >> /etc/vsftpd.conf
echo "userlist_file=/etc/vsftpd.userlist" >> /etc/vsftpd.conf
echo "ftpuser" >> /etc/vsftpd.userlist
sudo systemctl start vsftpd
sudo systemctl status vsftpd
ip addr