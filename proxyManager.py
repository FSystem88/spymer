import threading
import requests
import time
import random
from threading import Thread
from colorama import Fore, Back, Style

class ProxyManager:

    def __init__(self):
        self.autoChangeProxy = False
        self.proxy = "localhost"


    def updateproxy(self):
            self.proxy = ""
            self.info = ""
            try:
                    print ("Введите proxy в формате ip:port.")
                    print ("Пример: "+Fore.GREEN+"123.45.6.78:8080"+Style.RESET_ALL)
                    print ("Для отмены нажмите Ctrl+C")
                    self.proxy = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
                    if self.proxy == "":
                            self.info = Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
                            self.proxy = "localhost"
                    else:
                            print("Проверяю прокси...")
                            ip = requests.get("http://fsystem88.ru/ip", verify=False, timeout=10).text
                            try:
                                    ipx = requests.get("http://fsystem88.ru/ip", proxies={'http': "http://{}".format(self.proxy), 'https':"http://{}".format(self.proxy)}, verify=False, timeout=10).text
                            except:
                                    ipx = ip
                            if ip != ipx:
                                    self.info = Fore.GREEN+"Proxy рабочий."+Style.RESET_ALL
                            else:
                                    print(Fore.RED+"{} не работает. Введите новый!".format(self.proxy)+Style.RESET_ALL)
                                    self.updateproxy()
            except:
                    self.info = Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
                    self.proxy = "localhost"

    def getProxies(self):
        proxies = ""
        if self.autoChangeProxy:
            try:
                f = open("proxies.txt")
                proxies = f.read().split()
                self.proxy = random.choice(proxies)
                f.close()
            except IOError:
                self.generateproxy()
        if self.proxy=="localhost":
                proxies=None
        else:
                proxies={'http': "http://{}".format(self.proxy), 'https':"http://{}".format(self.proxy)}
        return proxies 

    def generateproxy(self):
            self.proxy = ""
            self.info = ""

            print(Fore.YELLOW+"Подождите генерируем рабочий прокси.\nОбычно это занимает не больше 30 секунд..."+Style.RESET_ALL)
            url="https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=RU"
            req = requests.get(url)
            ip = requests.get("http://fsystem88.ru/ip").text
            array = req.text.split()
            open("proxies.txt", "w+").close()
            thread_list = []
            for prox in array:
                    t = threading.Thread (target=self.checkproxy, args=(ip, prox))
                    thread_list.append(t)
                    t.start()
            # Wait for threads to finish:
            for x in thread_list:
                x.join()
            f = open("proxies.txt")
            proxies = f.read().split()
            self.proxy = random.choice(proxies)
            self.info = Fore.GREEN+"Рабочий прокси успешно найден!"+Style.RESET_ALL
            f.close()


    def checkproxy(self, ip, prox):
            try:
                    ipx = requests.get("http://fsystem88.ru/ip", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}, verify=False, timeout=10).text
            except:
                    ipx = ip
            if ip != ipx:
                    f = open("proxies.txt", "a+")
                    f.write("{}\n".format(prox))
                    f.close()
