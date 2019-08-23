#! /bin/sh
cd
pkg install python
pkg install python3
pkg install python3-pip
pip3 install requests
pip3 install colorama
echo alias spymer="'clear && cd && python3 spymer/spammer.py'">>.bashrc
echo "\033[37;1;42m G O O D !! \033[0m"
cd
python3 spymer/spammer.py -h