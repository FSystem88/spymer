#!/bin/bash
clear
echo "--------------------"
echo "|     Кто ты ?     |"
echo "|------------------|"
echo "| 1. Termux        |"
echo "| 2. Другой Unix   |"
echo "| 3. iSH           |"
echo "|                  |"
echo "| Введите 1/2/3:   |"
echo "--------------------"
read numb
if [ $numb = "1" ]
then
	pkg install python
	pkg install dos2unix
	pip install requests colorama proxyscrape
	cp ~/spymer/spammer.py $PREFIX/bin/spymer
	dos2unix $PREFIX/bin/spymer
	chmod -R 777 ~/spymer
	chmod 777 $PREFIX/bin/spymer
	spymer
elif [ $numb = "2" ]
then
	if [ "$(whoami)" != 'root' ];
	then
		echo "У вас нет прав. Запустите install.sh с root правами (sudo sh $PWD/install.sh)"
		exit
	else
		apt update
		apt install python3 python3-pip dos2unix -y
		pip3 install requests colorama proxyscrape
		cp ~/spymer/spammer.py $PREFIX/bin/spymer
		dos2unix $RPEFIX/bin/spymer
		chmod 777 $RPEFIX/bin/spymer
		chmod -R 777 ~/spymer
		spymer
	fi
elif [ $numb = "3" ]
then
	apk add python3 dos2unix py3-pip
	pip3 install requests colorama proxyscrape
	cp ~/spymer/spammer.py /usr/bin/spymer
	dos2unix /usr/bin/spymer
	chmod 777 /usr/bin/spymer
	spymer
else
	echo "Некорректный ввод"
fi
