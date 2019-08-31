#! /bin/sh
cd
apt install python
apt install python3
apt install python3-pip
pip3 install requests
pip3 install colorama
echo clear>.bashrc
echo alias spymer-update="'clear && cd && rm -rf spymer && git clone https://github.com/FSystem88/spymer && clear && sh spymer/install.sh'">>.bashrc
echo alias spymer="'clear && cd && python3 spymer/spammer.py'">>.bashrc
clear
cd
python3 spymer/spammer.py
