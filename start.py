#!/usr/bin/python3

import os
def MAIN():

        def checkver():
            global ui
            result = subprocess.check_output(["git", "diff"]).decode("utf-8") 
            if result != "":
                ui.printError("\nВерсия устарела и нуждается в обновлении!")


        def update():
            global ui
            print("Вы уверены, что хотите обновить?")
            menuInput = ui.getUserInput("spymer > ", ["Да","Нет"])
            if menuInput==1:
                os.system("cd && rm -rf spymer && git clone https://github.com/s0563858/spymer && cd spymer && sh install.sh")
                ui.printWarning("Успех! Теперь перезапустите программу!")
                exit()
            else:
                return "Отменено"

        def oneNumber():
            global proxyManager
            global ui
            ui.clear()
            ui.logo()
            print('Введите телефон ("Enter" - отмена):')
            phone = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
            try:
                int(phone)
            except:
                return Fore.RED+"Неверно введен номер телефона"+Style.RESET_ALL

            print('Введите количество кругов ("Enter" - отмена):')
            iterationsNumber = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
            try:
                int(iterationsNumber)
            except:
                return Fore.RED+"Неверно введено кол-во кругов"+Style.RESET_ALL
            
            ui.clear()
            ui.logo()
            print('\nТелефон: {}\nКол-во кругов: {}'.format(phone,iterationsNumber)+'\nСпамер запущен.\nЕсли хотите остановить - нажмите Ctrl+Z.')
            doSpamming(phone, int(iterationsNumber))
            # t = threading.Thread (target=doSpamming, args=(phone,int(iterationsNumber)))
            # t.start()
            #wait for thread to finish:
            # t.join()

            return Fore.BLUE+"\nГотово.\nТелефон: {}\nКол-во кругов: {}".format(phone, iterationsNumber)+Style.RESET_ALL




        def severalNumbers():
            global ui
            ui.clear()
            ui.logo()
            #-------- Get phone numbers ----------
            print("Вы хотите использовать файл с номерами?")
            menuInput = ui.getUserInput("spymer > ", ["Да","Нет"])
            phoneNumbers=[]
            if menuInput == 1:
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
                print("Чтобы закончить ввод номеров 'Enter'")
                newNumber="a"
                while newNumber != "":
                    newNumber=input(Fore.BLUE+"spymer > "+Style.RESET_ALL+"~/")
                    phoneNumbers.append(newNumber)
                phoneNumbers.pop()
                print("\nНомера:\n{}".format(phoneNumbers))
            #check if the numbers are correct:
            for phone in phoneNumbers:
                try:
                    a = int(phone)
                except:
                    return Fore.RED+"\nОдин из номеров состоит не только из цифр!"+Style.RESET_ALL
            #-------- Get phone numbers ----------

            ui.clear()
            ui.logo()
            print('Введите количество кругов ("Enter" - отмена):')
            iterationsNumber=0
            try:
                iterationsNumber= int(input(Fore.BLUE+"spymer > "+Style.RESET_ALL))
            except:
                return Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

            ui.clear()
            ui.logo()
            print('\nКол-во кругов: {}'.format(iterationsNumber))
            thread_list = []
            for phone in phoneNumbers:
                print('\nЗапущен спам на {}.Если хочешь остановить - нажмите Ctrl+Z.'.format(phone))
                t = threading.Thread (target=doSpamming, args=(phone,iterationsNumber))
                thread_list.append(t)
                t.start()
            #wait for all threads to finish:
            for x in thread_list:
                x.join()
            return Fore.BLUE+"\nГотово.\nНомера:{}\nКол-во кругов: {}".format(phoneNumbers,iterationsNumber)+Style.RESET_ALL


        def doSpamming(phone, iterationsNumber):
            global proxyManager
            iteration=0
            spammer = SmsSpammer(phone)
            while iteration < iterationsNumber:
                proxies = proxyManager.getProxies()
                spammer.setProxies(proxies)
                spammer.startSending()
                iteration+=1
                print(Fore.GREEN+"{}".format(phone)+Style.RESET_ALL+": круг №{} пройден.".format(iteration))
                if spammer.timeoutCounter > 10:
                    print(Fore.RED+"\nМногие сообщения не были отосланы - возмножна проблема с интернет-соеденением или проблема с прокси!"+Style.RESET_ALL)
            print(Fore.GREEN+"\nСпам на {} закончен. Кол-во кругов {}".format(phone, iterationsNumber)+Style.RESET_ALL)
            # exit()

        def startApplication():
            global proxyManager
            global ui
            ui = UserInterface()
            proxyManager = ProxyManager()
            
            result=""
            while True:
                ui.clear()
                ui.logo()
                checkver()
                print(result)
                print("Proxy: "+Fore.BLUE+"{}".format(proxyManager.proxyList)+Style.RESET_ALL)
                if proxyManager.proxyList == []:
                    ui.printWarning("Советую использовать прокси !!!")

                menuInput = ui.getUserInput("Введите номер пункта: ", ["Запустить спамер","Настройки прокси","Обновить SPYMER","Выход"])
                if menuInput == 1:
                    ui.clear()
                    ui.logo()
                    menuInput = ui.getUserInput("Выберите один вариант: ", ["Запустить спамер на один номер","Запустить спамер на несколько номеров"])
                    if menuInput == 1:
                        result=oneNumber()
                    elif menuInput == 2:
                        result=severalNumbers()
                elif menuInput == 2:
                    menuInput = ui.getUserInput("spymer >  ", ["Удалить прокси","Ввести свой прокси","Сгенерировать прокси","Включить автоматическую генерацию прокси после каждого круга"])
                    ui.clear()
                    ui.logo()
                    if menuInput==1:
                        proxyManager.proxy = "localhost"
                    elif menuInput==2:
                        proxyManager.updateproxy()
                    elif menuInput==3:
                        proxyManager.generateproxy()
                    elif menuInput==4:
                        proxyManager.autoChangeProxy = True
                        proxyManager.proxy="auto-change"

                elif menuInput == 3:
                    ui.clear()
                    ui.logo()
                    result=update()
                
                elif menuInput == 4:
                    print (Fore.BLUE+"\nДо скорой встречи!)\n"+Style.RESET_ALL)
                    exit()


        try:
                import random
                import requests
                import urllib3
                import sys
                import re
                import time
                import asyncio
                import aiohttp
                import datetime
                import json
                import threading
                from threading import Thread
                import subprocess
                from src.sms import SmsSpammer
                from src.proxyManager import ProxyManager
                from src.userInterface import UserInterface
                from colorama import Fore, Back, Style
                from random import randint
        except ModuleNotFoundError:
                os.system('cls' if os.name=='nt' else 'clear')
                print("Нажмите Enter чтобы установить недостающие библиотеки...")
                input()
                os.system("python -m pip install requests colorama asyncio aiohttp")



        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        startApplication()

MAIN()
