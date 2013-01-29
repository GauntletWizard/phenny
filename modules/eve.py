#!/usr/bin/env python
"""
eve.py - Query eve-central market data.
Copyright 2013 Google Inc
@author thahn+github@google.com

"""

import xml.etree.ElementTree as ET
import re
import sqlite3
import urllib2 as urllib


def minerals(phenny, input):
  urllib.urlopen("http://api.eve-central.com/api/marketstat?typeid=34")
minerals.commands = ['minerals']
minerals.priority = 'low'

def prices(phenny, input):
  names = nametotype(input.split()[1])
  if len(names) > 1:
    phenny.say("I'm uncertain what you were looking for; Perhaps one of these?")
    for (name, typeid) in names:
      phenny.say("%d - %s" % (typeid, name))
    return
  else:
    phenny.say('%r' % names)
    items = query(names[0][1])
    item = items[0]
    phenny.say("%s: Mean: %d Max: %d Volume: %d" % (item.name, item.all['avg'], item.all['median'], item.all['volume']))
    
prices.commands = ['prices']
prices.priority = 'low'

def query(typeid):
  if isinstance(typeid, list):
    query = '&typeid='.join(typeid)
  else:
    query = str(typeid)
  foo = urllib.urlopen("http://api.eve-central.com/api/marketstat?typeid=%s" % query)
  root = ET.fromstring(foo.read())
  results = []
  for item in root.findall('./marketstat/type'):
    results.append(Itemtype(item))
  return results

class Itemtype(object):
  def __init__(self, item):
    self.type = item.get('id')
    self.name = nametotype(item.get('id'))[0][0]
    self.buy = {}
    self.sell = {}
    self.all = {}
    for name, d in [('buy', self.buy), ('sell', self.sell), ('all', self.all)]:
      for val in item.find(name).getchildren():
        d[val.tag] = float(val.text)

def nametotype(name):
  """Query the database for names and typeids
  
  Args:
          name: Short string representation of a 
          
  Returns:  An array of typeName, typeID tuples, or None
  """
  db = sqlite3.connect('/home/ted/dev/eve/eve.sqlite')
  try:
    typeid = int(name)
    results = db.execute("select typeName, typeID from invTypes where typeID = ?",
                    [typeid])
    return results.fetchall()
  except ValueError:
    pass
  print "querying on name"
  results = db.execute("select typeName, typeID from invTypes where typeName LIKE ?",
                  ["%" + name + "%"])
  return results.fetchall()
