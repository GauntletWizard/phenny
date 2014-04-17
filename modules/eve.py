#!/usr/bin/env python
"""
eve.py - Query eve-central market data.
Copyright 2013 Google Inc
@author thahn+github@google.com

"""

import xml.etree.ElementTree as ET
import re
import sqlite3
import threading
import urllib2 as urllib


def thread():
  print "Thread: ", threading.current_thread().ident

def minerals(phenny, input):
  thread()
  query(min_types)
  for item in min_types:
    phenny.say("%s: Mean: %g Median: %g Volume: %g" % (item.name, item.all['avg'], item.all['median'], item.all['volume']))

minerals.commands = ['minerals']
minerals.priority = 'low'

def prices(phenny, input):
  thread()
  items = nametotype(input.split()[1])
  if len(items) > 1:
    phenny.say("I'm uncertain what you were looking for; Perhaps one of these?" + " ".join()
    for item in items:
      phenny.say("%d - %s" % (item.typeid, item.name))
    return
  else:
    query(items)
    item = items[0]
    phenny.say("%s: Mean: %g Median: %g Volume: %g" % (item.name, item.all['avg'], item.all['median'], item.all['volume']))
    
prices.commands = ['prices']
prices.priority = 'low'

def route(phenny, input):
  who, where, to = input.split()
  foo = urllib.urlopen("http://api.eve-central.com/api/route/from/%s/to/%s" % (where, to))


def query(typeid):
  if isinstance(typeid, list):
    query = '&typeid='.join(map(lambda x: str(x.typeid) , typeid))
  else:
    query = str(typeid.typeid)
    typeid = [typeid]
  foo = urllib.urlopen("http://api.eve-central.com/api/marketstat?typeid=%s" % query)
  root = ET.fromstring(foo.read())
  i = 0
  for item in root.findall('./marketstat/type'):
    typeid[i].setPrices(item)
    i += 1

class WrongTypeException(Exception):
  pass

class Itemtype(object):
  def __init__(self, name, typeid):
    self.name = name
    self.typeid = typeid

  def setPrices(self, item):
		
    if not self.typeid == int(item.get('id')):
      raise WrongTypeException("Expected: %s Got: %s" % (item.get('id'), self.typeid))
      self.name = nametotype(item.get('id'))[0].name
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
  db = sqlite3.connect('/home/ted/dev/eve/eve.sqlite', check_same_thread=False)
  try:
    typeid = int(name)
    results = db.execute("select typeName, typeID from invTypes where typeID = ?",
                    [typeid])
    return [Itemtype(x,y) for (x, y) in results.fetchall()]
  except ValueError:
    pass
  results = db.execute("select typeName, typeID from invTypes where typeName LIKE ?",
                  ["" + name + ""])
  items = [Itemtype(x,y) for (x, y) in results.fetchall()]
  if items:
    return items
  results = db.execute("select typeName, typeID from invTypes where typeName LIKE ?",
                  ["%" + name + "%"])
  return [Itemtype(x,y) for (x, y) in results.fetchall()]

min_types = map(nametotype, range(34,41))
min_types.append(nametotype(29668))
min_types = map(lambda x: x[0], min_types)
