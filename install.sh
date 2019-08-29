#! /bin/sh
cd
apt install python
apt install python3
apt install python3-pip
pip3 install requests
pip3 install colorama
echo clear>.bashrc
echo alias spymer-update="'clear && cd && rm -rf spymer && git clone https://github.com/FSystem88/spymer && clear && spymer'">>.bashrc
echo alias spymer="'clear && cd && python3 spymer/spammer.py'">>.bashrc
clear
cd
python3 spymer/spammer.py
echo "\033[37;1;42m Done. Please restart your Terminal... \033[0m"
