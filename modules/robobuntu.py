#!/usr/bin/env python
"""
robobuntu.py - Make annoying sounds in IRC channel
Copyright 2013 Google Inc
@author thahn+github@tcbtech.com

"""

import re

def robobuntu(phenny, input):
				#oo-BUN-too
				phenny.say("oo-BOON-too!")
				print "called: ", input
robobuntu.priority = 'high'
robobuntu.commands = ["ubuntu"]
robobuntu.r_commands = [re.compile(r'.*ubuntu.*', re.IGNORECASE)]

pokere = re.compile(r'(\w*)\W(ten|10)\W(\w*)', re.IGNORECASE)
def pokemans(phenny, input):
				# You can't X ten Y!
				print "pokemans"
				x, ten, y = pokere.search(input).groups()
				phenny.say("You can't %s ten %s!" % (x, y))
pokemans.rule = r'(\w*)\W(ten|10)\W(\w*)'
pokemans.priority = 'high'
pokemans.r_commands = [pokere]
