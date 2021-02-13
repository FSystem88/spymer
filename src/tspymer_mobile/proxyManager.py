import threading
import requests
import time
import random
from threading import Thread
from colorama import Fore, Back, Style

class ProxyManager:

    def __init__(self):
        self.autoChangeProxy = False
        self.proxyStatus = "localhost"
        self.proxyList = []


    def updateproxy(self):
        try:
            print ("Введите proxy в формате ip:port.")
            print ("Пример: "+Fore.GREEN+"123.45.6.78:8080"+Style.RESET_ALL)
            print ("Для отмены нажмите Ctrl+C")
            newProxy = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
            if newProxy == "":
                return Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
            print("Проверяю прокси...")
            self.checkProxy(newProxy)

            if not self.proxyList:
                return Fore.GREEN+"Proxy рабочий."+Style.RESET_ALL
            else:
                print(Fore.RED+"{} не работает. Введите новый!".format(newProxy)+Style.RESET_ALL)
                self.updateproxy()
        except:
            return Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL

    def getProxies(self):
        if self.autoChangeProxy:
            self.generateProxyList()

        if self.proxyList==[]:
            return None
        else:
            return self.proxyList

    def generateProxyList(self):
            print(Fore.YELLOW+"\nПодождите генерируем рабочий прокси.\nОбычно это занимает не больше 30 секунд..."+Style.RESET_ALL)
            url="https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=RU"
            req = requests.get(url)
            proxies = req.text.split()

            self.proxyList = []
            thread_list = []
            for prox in proxies:
                # print(prox)
                t = threading.Thread (target=self.checkProxy, args=(prox,))
                thread_list.append(t)
                t.start()
            # Wait for threads to finish:
            for x in thread_list:
                 x.join()
            while not self.proxyList:
                self.generateProxyList()

    def generateproxy(self):
            self.generateProxyList()
            return Fore.GREEN+"Рабочий прокси успешно найден!"+Style.RESET_ALL


    def checkProxy(self, prox):
        try:
             requests.get("http://www.google.com", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}, verify=False, timeout=10).text
             self.proxyList.append(prox)
        except:
            pass




