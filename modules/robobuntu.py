#!/usr/bin/env python
"""
robobuntu.py - Make annoying sounds in IRC channel
Copyright 2013 Google Inc
@author thahn+github@tcbtech.com

"""

import re
import urllib2 as urllib
import xml.etree.ElementTree as ET

def robobuntu(phenny, input):
  #oo-BUN-too
	phenny.say("oo-BOON-too!")
	return
robobuntu.priority = 'low'
robobuntu.rule = ".*ubuntu.*"
robobuntu.ignorecase = True

def oop(phenny, input):
	# OOPerating system
	phenny.say("that's my favorite OOPerating system")
oop.priority = 'low'
oop.rule = '.*oo-BOON-too.*'
oop.ignorecase = True

def oop2(phenny, input):
	phenny.say("Are you guys talking about oo-BOON-too?")
oop2.priority = 'low'
oop2.rule = ".*OOPerating system.*"
oop2.ignorecase = True

def pokemans(phenny, input):
	# You can't X ten Y!
	x, ten, y = pokere.search(input).groups()
	if y[-1].lower() == 's':
		y = y[0:-1]
	tens = ("You can't %s ten %ss!" % (x, y))
	if input.upper() == input:
		tens = tens.upper()
	phenny.say(tens)
	return

pokemans.rule = r'.*?(\S+)\W(ten|10)\W(\S+)'
pokere = re.compile(pokemans.rule, re.IGNORECASE)
pokemans.priority = 'low'
pokemans.ignorecase = True

def geodudes(phenny, input):
	phenny.say("6 geodudes, can't lose!")
	return
geodudes.rule = r'.*(6|six) geodudes.*'
geodudes.ignorecase = True

def fucker(phenny, input):
	print input
	phenny.say("Censor yourself, Motherfucker!")
	return
fucker.rule = r'.*(fuck|shit|cunt).*'
fucker.ignorecase = True

def warm(phenny, input):
  phenny.say("Warm yesterday.")
  return
warm.rule = r'warm today\.?'
warm.ignorecase = True

if __name__ == '__main__': 
	print __doc__.strip()


def tonight(phenny, input):
  foo = urllib.urlopen("http://geeknights-generator.herokuapp.com/").read()
  root = ET.fromstring(foo[16:])  # Hack off the DOCTYPE.
  desc = root.findall("./body/div/p")[0].text
  phenny.say("Tonight on Geeknights" + desc)
tonight.commands = ['tonight']

