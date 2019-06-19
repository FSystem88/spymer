#! /bin/sh
cd
apt install python2
apt install python-pip
pip2 install requests
echo alias spymer="'cd && python2 spymer/spammer.py'">>.bashrc
echo "\033[37;1;42m G O O D ! \033[0m"
