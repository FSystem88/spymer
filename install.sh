#! /bin/sh
apt-get install python3, python3-pip
pip3 install requests
pip3 install colorama
sudo cp ~/spymer/spammer.py /usr/bin/spymer
sudo chmod +x /usr/bin/spymer
spymer
