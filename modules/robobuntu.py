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
	return
robobuntu.priority = 'low'
robobuntu.rule = ".*ubuntu.*"
robobuntu.ignorecase = True

def pokemans(phenny, input):
	# You can't X ten Y!
	x, ten, y = pokere.search(input).groups()
	phenny.say("You can't %s ten %ss!" % (x, y))
	return

pokemans.rule = r'(\w+)\W(ten|10)\W(\w+)s?'
pokere = re.compile(pokemans.rule, re.IGNORECASE)
pokemans.priority = 'low'
pokemans.ignorecase = True

def geodudes(phenny, input):
	phenny.say("6 geodudes, can't lose!")
	return
geodudes.rule = r'(6|six) geodudes'
pokemans.ignorecase = True

if __name__ == '__main__': 
	print __doc__.strip()


