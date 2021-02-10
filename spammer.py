#!/usr/bin/python3
# -*- coding: utf-8 -*-
# spymer v9.0
# Author: FSystem88
import os
def MAIN():


        def clear():
                os.system('cls' if os.name=='nt' else 'clear')

        def checkver():
                ver = '90'
                version = requests.post("https://fsystem88.ru/spymer/version.php").json()["version"]
                if int(ver) < int(version):
                        print(Back.RED+"\nВерсия устарела и нуждается в обновлении!"+Style.RESET_ALL)

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

        def oneNumber():
            global proxyManager
            clear()
            logo()
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
                            clear()
                            logo()
                            print('\nТелефон: {}\nКол-во кругов: {}'.format(phone, count)+'\nСпамер запущен.\nЕсли хотите остановить - нажмите Ctrl+Z.')

                            spammer = SmsSpammer(phone)
                            while iteration < count:
                                proxies = proxyManager.getProxies()
                                spammer.setProxies(proxies)
                                spammer.startSending()
                                iteration+=1
                                print("{} круг пройден.".format(iteration))

                            return Fore.BLUE+"\nГотово.\nТелефон: {}\nКол-во кругов: {}".format(phone, iteration)+Style.RESET_ALL
                    except:
                        return Fore.RED+"Неверно введено кол-во кругов"+Style.RESET_ALL
            except:
                    return Fore.RED+"Неверно введен номер телефона"+Style.RESET_ALL

        def severalNumbers():
                clear()
                logo()
                #-------- Get phone numbers ----------
                print("Вы хотите использовать файл с номерами?")
                print("1. Да")
                print("2. Нет")
                usingFile=input(Fore.BLUE+"spymer > "+Style.RESET_ALL+"~/")
                phoneNumbers=[]
                if usingFile == "1":
                    print("Введите путь к файлу: ")
                    print("(Папка с файлом должна находиться в домашней дирректории!)")
                    f_name=input(Fore.BLUE+"spymer > "+Style.RESET_ALL+"~/")
                    try:
                        os.chdir(os.getenv("HOME"))
                        file=open("{}".format(f_name))
                        phoneNumbers=file.read().splitlines()
                        if phoneNumbers[-1] == '':
                                phoneNumbers.pop()
                        print("Файл найден.\nНомера:\n{}".format(phoneNumbers))
                    except FileNotFoundError:
                        return Fore.RED+"\nФайл {} не найден".format(f_name)+Style.RESET_ALL
                else:
                    print("Вводите номера: ")
                    print("Чтобы закончить ввод номеров - введите '1'")
                    newNumber=""
                    while newNumber != "1":
                        newNumber=input(Fore.BLUE+"spymer > "+Style.RESET_ALL+"~/")
                        phoneNumbers.append(newNumber)
                    print("\nНомера:\n{}".format(phoneNumbers))
                #-------- Get phone numbers ----------

                clear()
                logo()
                print('Введите количество кругов ("Enter" - отмена):')
                count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
                try:
                    if int(count):
                        count=int(count)
                        print('\nФайл: ~/{}\nКол-во кругов: {}'.format(f_name, count))
                        clear()
                        logo()
                        for phone in phoneNumbers:
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
                    return Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

                return Fore.BLUE+"\nГотово.\nФайл: {}\nКол-во кругов: {}".format(f_name, count)+Style.RESET_ALL
                # exit()


        def n_send(phone, count):
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
                global proxyManager
                proxyManager = ProxyManager()
                
                result=""
                while True:
                        clear()
                        logo()
                        checkver()
                        print(result)
                        print("Proxy: "+Fore.BLUE+"{}".format(proxyManager.proxy)+Style.RESET_ALL)
                        if proxyManager.proxy == "localhost":
                                print(Fore.YELLOW+"Советую использовать прокси !!!"+Style.RESET_ALL)
                        print("1) Запустить спамер.")
                        print("2) Настройки прокси.")
                        print("3) Обновить SPYMER.")
                        print("4) Выход.")
                        input1 = input(Fore.BLUE+"Введите номер пункта: "+Style.RESET_ALL)
                        if input1 == "1":
                                clear()
                                logo()
                                print("Выберите один вариант:")
                                print("1. Запустить спамер на один номер")
                                print("2. Запустить спамер на несколько номеров ")
                                input11= input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
                                if input11 == "1":
                                        result=oneNumber()
                                elif input11 == "2":
                                        result=severalNumbers()
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
                                        proxyManager.proxy="auto-change"
                                        # proxyManager.generateproxy()

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
