#! /bin/sh
pkg install python
pkg install python3
pkg install python3-pip
pip3 install requests
pip3 install colorama
cp ~/spymer/spammer.py /data/data/com.termux/files/usr/bin/spymer
chmod +x /data/data/com.termux/files/usr/bin/spymer
dos2unix /data/data/com.termux/files/usr/bin/spymer
cp ~/spymer/spammer.py /usr/bin/spymer
chmod +x /usr/bin/spymer
dos2unix /usr/bin/spymer
spymer
