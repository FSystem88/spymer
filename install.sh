#! /bin/sh
cd
apt install python
apt install python3
apt install python3-pip
pip3 install requests
pip3 install colorama
echo clear>>.bashrc
echo alias spymer-update="'clear && cd && rm -rf spymer && git clone https://github.com/FSystem88/spymer && clear && spymer -h '">>.bashrc
echo alias spymer="'clear && cd && python3 spymer/spammer.py'">>.bashrc
echo "\033[37;1;42m G O O D !! \033[0m"
cd
clear
python3 spymer/spammer.py -h
