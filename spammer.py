#!/usr/bin/python3
# -*- coding: utf-8 -*-
# spymer v9.0
# Author: FSystem88
import os
def MAIN():


        def clear():
                os.system('cls' if os.name=='nt' else 'clear')

        def checkver():
                global info
                ver = '90'
                version = requests.post("https://fsystem88.ru/spymer/version.php").json()["version"]
                if int(ver) < int(version):
                        info=Back.RED+"\nВерсия устарела и нуждается в обновлении!"+Style.RESET_ALL

        def logo():
                r = Fore.RED
                g = Fore.GREEN
                y = Fore.YELLOW
                s = Style.RESET_ALL
                logo = r+"░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n░"+g+"██████"+r+"╗"+g+"██████"+r+"╗░"+g+"██"+r+"╗░░░"+g+"██"+r+"╗"+g+"███"+r+"╗░░░"+g+"███"+r+"╗"+g+"███████"+r+"╗"+g+"██████"+r+"╗░\n"+g+"██"+r+"╔════╝"+g+"██"+r+"╔══"+g+"██"+r+"╗╚"+g+"██"+r+"╗░"+g+"██"+r+"╔╝"+g+"████"+r+"╗░"+g+"████"+r+"║"+g+"██"+r+"╔════╝"+g+"██"+r+"╔══"+g+"██"+r+"╗\n"+r+"╚"+g+"█████"+r+"╗░"+g+"██████"+r+"╔╝░"+r+"╚"+g+"████"+r+"╔╝"+r+"░"+g+"██"+r+"╔"+g+"████"+r+"╔"+g+"██"+r+"║"+g+"█████"+r+"╗░░"+g+"██████"+r+"╔╝\n░"+r+"╚═══"+g+"██"+r+"╗"+g+"██"+r+"╔═══╝░░░"+r+"╚"+g+"██"+r+"╔╝░░"+g+"██"+r+"║╚"+g+"██"+r+"╔╝"+g+"██"+r+"║"+g+"██"+r+"╔══╝░░"+g+"██"+r+"╔══"+g+"██"+r+"╗\n"+g+"██████"+r+"╔╝"+g+"██"+r+"║░░░░░░░░"+g+"██"+r+"║░░░"+g+"██"+r+"║░"+r+"╚═╝░"+g+"██"+r+"║"+g+"███████"+r+"╗"+g+"██"+r+"║░░"+g+"██"+r+"║\n"+r+"╚═════╝░"+r+"╚═╝░░░░░░░░"+r+"╚═╝░░░"+r+"╚═╝░░░░░"+r+"╚═╝╚══════╝╚═╝░░"+r+"╚═╝\n░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░ "+s+"by FSystem88"+r+" ░░░\n"+y+" [ SMS Spammer ~ v.9.0 ~ MPL-2.0 ]\n [ Dev: FSystem88 ~ prod. by Ca$h&Мир® ]"+s
                print(logo)




        def update():
                a=input("Вы уверены, что хотите обновить? (y/n) ")
                if a=="y":
                        os.system("cd && rm -rf spymer && git clone https://github.com/FSystem88/spymer && cd spymer && sh install.sh")
                        exit()
                else:
                        print("Отменено")

        def onesend():
                global phone
                global info
                global proxyManager
                clear()
                logo()
                print(info)
                print('Введите телефон ("Enter" - отмена):')
                phone = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
                try:
                        if int(phone):
                                print('Введите количество кругов ("Enter" - отмена):')
                                count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
                                try:
                                        if int(count):
                                                count=int(count)
                                                iteration = 0
                                                info = '\nТелефон: {}\nКол-во кругов: {}'.format(phone, count)+'\nСпамер запущен.\nЕсли хочешь остановить - нажмите Ctrl+Z.'
                                                clear()
                                                logo()
                                                print(info)

                                                spammer = SmsSpammer(phone)
                                                while iteration < count:
                                                        proxies = proxyManager.getProxies()
                                                        spammer.setProxies(proxies)
                                                        spammer.startSending()
                                                        iteration+=1
                                                        print("{} круг пройден.".format(iteration))

                                                info = Fore.BLUE+"\nГотово.\nТелефон: {}\nКол-во кругов: {}".format(phone, iteration)+Style.RESET_ALL
                                except:
                                        info=Fore.RED+"Неверно введено кол-во кругов"+Style.RESET_ALL
                except:
                        info=Fore.RED+"Неверно введен номер телефона"+Style.RESET_ALL

        def filesend():
                global phone
                global info
                clear()
                logo()
                print(info)
                print("Введите путь к файлу: ")
                print("(Папка с файлом должна находиться в домашней дирректории!)")
                print("Не знаешь, как создать файл в терминале - воспользуйся токеном!")
                f_name=input(Fore.BLUE+"spymer > "+Style.RESET_ALL+"~/")
                clear()
                logo()
                print(info)
                try:
                        os.chdir(os.getenv("HOME"))
                        file=open("{}".format(f_name))
                        array=file.read().splitlines()
                        if array[-1] == '':
                                array.pop()
                        print("Файл найден.\nНомера:\n{}".format(array))
                        print('Введите количество кругов ("Enter" - отмена):')
                        count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
                        try:
                                if int(count):
                                        count=int(count)
                                        info = '\nФайл: ~/{}\nКол-во кругов: {}'.format(f_name, count)
                                        clear()
                                        logo()
                                        print(info)
                                        for phone in array:
                                                try:
                                                        if int(phone):
                                                                print('\nЗапущен спам на {}.Если хочешь остановить - нажмите Ctrl+Z.'.format(phone))
                                                                thread_list = []
                                                                t = threading.Thread (target=n_send, args=(phone,count))
                                                                thread_list.append(t)
                                                                t.start()
                                                except:
                                                        print(Fore.RED+'\n"{}" не является номером телефона.'.format(phone)+Style.RESET_ALL)
                                        for th in threading.enumerate(): 
                                                if th != threading.currentThread():
                                                        th.join()	
                        except:
                                info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

                        print(Fore.BLUE+"\nГотово.\nФайл: {}\nКол-во кругов: {}".format(f_name, count)+Style.RESET_ALL)
                        exit()
                except FileNotFoundError:
                        info=Fore.RED+"\nФайл {} не найден".format(f_name)+Style.RESET_ALL

        def tokensend():
                global phone
                global info
                clear()
                logo()
                print(info)
                print("Введите токен: ")
                print("Загрузить файл и получить токен можно по ссылке:")
                print(Fore.GREEN+"https://FSystem88.ru/spymer/\n"+Style.RESET_ALL)
                token=input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
                id=requests.post('https://fsystem88.ru/spymer/spym.php', data={'token': token}).json()["id"]
                if int(id) != 0:
                        req=requests.get("https://fsystem88.ru/spymer/token/{}".format(token))
                        info=""
                        clear()
                        logo()
                        print(info)
                        array=req.text.splitlines()
                        if "<h1>Not Found</h1>" in array:
                                info=Fore.RED+"Токен не найден на сервере.\n Загрузите файл и получите токен на сайте:\n"+Fore.GREEN+"https://FSystem88.ru/spymer"+Style.RESET_ALL
                        else:
                                if array[-1] == '':
                                        array.pop()
                                print("Файл загружен успешно.\nТелефоны:\n{}".format(req.text))
                                print('Введите количество кругов ("Enter" - отмена):')
                                count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
                                try:
                                        if int(count):
                                                count=int(count)
                                                info = '\nТокен: {}\nКол-во кругов: {}'.format(token, count)
                                                clear()
                                                logo()
                                                print(info)
                                                for phone in array:
                                                        try:
                                                                if int(phone):
                                                                        print('\nЗапущен спам на {}.Если хочешь остановить - нажмите Ctrl+Z.'.format(phone))
                                                                        thread_list = []
                                                                        t = threading.Thread (target=n_send, args=(phone,count ))
                                                                        thread_list.append(t)
                                                                        t.start()
                                                        except:
                                                                print(Fore.RED+'\n"{}" не является номером телефона.'.format(phone)+Style.RESET_ALL)
                                                for th in threading.enumerate(): 
                                                        if th != threading.currentThread():
                                                                th.join()	
                                except:
                                        info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

                                print(Fore.BLUE+"\nГотово.\nТокен: {}\nКол-во кругов: {}\n".format(token, count)+Style.RESET_ALL)
                                exit()

        def n_send(phone, count):
                global info
                global proxyManager
                iteration=0
                spammer=SmsSpammer(phone)
                while iteration < count:
                        proxies = proxyManager.getProxies()
                        spammer.setProxies(proxies)
                        spammer.startSending()
                        iteration+=1
                        print(Fore.GREEN+"{}".format(phone)+Style.RESET_ALL+": круг №{} пройден.".format(iteration))
                print(Fore.GREEN+"\nСпам на {} закончен. Кол-во кругов {}".format(phone, count)+Style.RESET_ALL)
                exit()

        def startApplication():
                global phone
                global info
                global proxyManager
                proxyManager = ProxyManager()
                
                info = " "
                while True:
                        clear()
                        logo()
                        print(info)
                        checkver()
                        print("Proxy: "+Fore.BLUE+"{}".format(proxyManager.proxy)+Style.RESET_ALL)
                        if proxyManager.proxy == "localhost":
                                print(Fore.YELLOW+"Советую использовать прокси !!!"+Style.RESET_ALL)
                        print("1) СМС спамер.")
                        print("2) Обновить прокси.")
                        print("3) Обновить SPYMER.")
                        print("4) Выход.")
                        input1 = input(Fore.BLUE+"Введите номер пункта: "+Style.RESET_ALL)
                        if input1 == "1":
                                clear()
                                logo()
                                print(info)
                                print("Выберите один вариант:")
                                print("1. Запустить спамер на один номер")
                                print("2. Выгрузить номера из TXT файла ")
                                print("3. Выгрузить номера по токену")
                                input11= input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
                                if input11 == "1":
                                        onesend()

                                elif input11 == "2":
                                        filesend()

                                elif input11 == "3":
                                        tokensend()
                                else:
                                        print("Некорректно")
                        
                        elif input1 == "2":
                                print("1. Удалить прокси")
                                print("2. Ввести свой прокси")
                                print("3. Сгенерировать прокси")
                                print("4. Включить автоматическую смену прокси после каждого круга")
                                input51 = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
                                if input51=="1":
                                        proxyManager.proxy = "localhost"
                                
                                elif input51=="2":
                                        proxyManager.updateproxy()

                                elif input51=="3":
                                        proxyManager.generateproxy()
                                elif input51=="4":
                                        proxyManager.autoChangeProxy = True

                        elif input1 == "3":
                                update()
                        
                        elif input1 == "4":
                                print (Fore.BLUE+"\nДо скорой встречи!)\n"+Style.RESET_ALL)
                                exit()


        try:
                import random
                import requests
                import urllib3
                import sys
                import re
                import time
                import datetime
                import json
                import threading
                from threading import Thread
                from sms import SmsSpammer
                from proxyManager import ProxyManager
                from colorama import Fore, Back, Style
                from random import randint
        except ModuleNotFoundError:
                os.system('cls' if os.name=='nt' else 'clear')
                print("Нажмите Enter чтобы установить недостающие библиотеки...")
                input()
                os.system("python -m pip install requests colorama")

        global phone
        global info
        global proxyManager
        #delete old list with proxies at start:
        try:
            f = open("proxies.txt")
            f.close()
            os.remove("proxies.txt")
        except IOError:
            pass

        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        startApplication()

MAIN()
