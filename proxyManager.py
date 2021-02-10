import threading
import requests
import time
import random
from threading import Thread
from colorama import Fore, Back, Style

class ProxyManager:

    def __init__(self):
        self.autoChangeProxy = False
        self.currentProxy=0
        self.proxy = "localhost"


    def updateproxy(self):
            try:
                    print ("Введите proxy в формате ip:port.")
                    print ("Пример: "+Fore.GREEN+"123.45.6.78:8080"+Style.RESET_ALL)
                    print ("Для отмены нажмите Ctrl+C")
                    newProxy = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
                    if newProxy == "":
                        return Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
                    else:
                        print("Проверяю прокси...")
                        result = requests.get("https://www.showmyip.com", verify=False, timeout=10).text
                        startIdx = result.find("Your IP</span>:")+16
                        endIdx = result.find("</span>",startIdx)
                        ownIP = result[startIdx:endIdx]
                        proxyIP = ""

                        try:
                            result = requests.get("http://www.showmyip.com", proxies={'http': "http://{}".format(newProxy), 'https':"http://{}".format(self.proxy)}, verify=False, timeout=10).text

                            startIdx = result.find("Your IP</span>:")+16
                            endIdx = result.find("</span>",startIdx)
                            proxyIP = result[startIdx:endIdx]
                        except:
                            proxyIP = ownIP

                        if ownIP != proxyIP:
                            self.proxy = newProxy
                            return Fore.GREEN+"Proxy рабочий."+Style.RESET_ALL
                        else:
                            print(Fore.RED+"{} не работает. Введите новый!".format(newProxy)+Style.RESET_ALL)
                            self.updateproxy()
            except:
                return Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL

    def getProxies(self):
        proxies = ""
        if self.autoChangeProxy:
            try:
                f = open("proxies.txt")
                proxyList = f.read().split()
                self.currentProxy = self.currentProxy+1
                if self.currentProxy >= len(proxyList):
                    self.currentProxy = 0
                    self.generateProxyList()
                self.proxy = proxyList[self.currentProxy]
                print("Смена прокси на:"+self.proxy)

                f.close()
            except IOError:
                self.generateProxyList()
                f = open("proxies.txt")
                proxyList = f.read().split()
                self.currentProxy = 0
                self.proxy = proxyList[self.currentProxy]
                print("Смена прокси на:"+self.proxy)

                f.close()
        if self.proxy=="localhost":
                proxies=None
        else:
                proxies={'http': "http://{}".format(self.proxy), 'https':"http://{}".format(self.proxy)}
        return proxies 

    def generateProxyList(self):
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

    def generateproxy(self):
            self.generateProxyList()
            f = open("proxies.txt")
            proxies = f.read().split()
            self.proxy = random.choice(proxies)
            f.close()
            return Fore.GREEN+"Рабочий прокси успешно найден!"+Style.RESET_ALL


    def checkproxy(self, ip, prox):
            try:
                ipx = requests.get("http://fsystem88.ru/ip", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(prox)}, verify=False, timeout=10).text
            except:
                ipx = ip
            if ip != ipx:
                f = open("proxies.txt", "a+")
                f.write("{}\n".format(prox))
                f.close()
        # proxyIP = ip
        # try:
            # result = requests.get("http://www.showmyip.com", proxies={'http': "http://{}".format(prox), 'https':"http://{}".format(self.proxy)}, verify=False, timeout=10).text
            # startIdx = result.find("Your IP</span>:")+16
            # endIdx = result.find("</span>",startIdx)
            # proxyIP = result[startIdx:endIdx]
        # except:
            # proxyIP = ip
        # if ip != proxyIP:
            # f = open("proxies.txt", "a+")
            # f.write("{}\n".format(prox))
            # f.close()
