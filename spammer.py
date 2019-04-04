#!/usr/bin/python

# - Spammer v3.1
# | Description: spams a phone number by sending it a lot of sms by using Grab API
# | Author: P4kL0nc4t & Noxturnix
# | Date: 25/04/2018
# | Disclaimer: Editing author will not make you the real coder
# | What's New?
# | - Fixed 403 forbidden
# | - Use less CPU

import spammer_class
spammer = spammer_class.Spammer()
spammer.author = "P4kL0nc4t & Noxturnix"
try:
    spammer.main()
except KeyboardInterrupt:
    print spammer_class.color.FAIL+spammer_class.color.REVERSE+"\r[!][except] KeyboardInterrupt detected! Exiting . . ."+spammer_class.color.ENDC+"\n"
    exit()
