#!/bin/bash
pkg install python
pkg install python3
pkg install python3-pip
pkg install dos2unix
pip3 install requests
pip3 install colorama
cp ~/spymer/spammer.py /data/data/com.termux/files/usr/bin/spymer
cp -R ~/spymer/pytransform /data/data/com.termux/files/usr/bin/pytransform/
dos2unix /data/data/com.termux/files/usr/bin/spymer
chmod 777 /data/data/com.termux/files/usr/bin/spymer
chmod 777 /data/data/com.termux/files/usr/bin/pytransform
spymer
