# https://confiraloterias.com.br/api/megasena/
import urllib2, json
import collections, numpy

token = '3YdNWdm1mmk1oxE'
total = []

def duplasena():
  return getResults('duplasena')

def lotofacil():
  return getResults('lotofacil')

def lotomania():
  return getResults('lotomania')

def megasena():
  return getResults('megasena')

def quina():
  return getResults('quina')

def readAPI(category):
  opener = urllib2.build_opener()
  opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
  response = opener.open('http://confiraloterias.com.br/api0/json.php?loteria='+category+'&lista=true&concurso=1&token='+token)
  return json.loads(response.read().decode('utf_8', 'ignore'))

def getResults(category):
  results = []
  for pair in readAPI(category):
    if category != 'duplasena':
      for value in pair.get("concurso").get("dezenas"):
        results.append(value)
        total.append(value)
    else:
      for value in pair.get("concurso").get("dezenas_1"):
        results.append(value)
        total.append(value)
      for value in pair.get("concurso").get("dezenas_2"):
        results.append(value)
        total.append(value)
  return results

print 'Duplasena:'
for value in collections.Counter(duplasena()).most_common():
  print value[0]+' appeared '+str(value[1])+' times'

print '\nLotofacil:'
for value in collections.Counter(lotofacil()).most_common():
  print value[0]+' appeared '+str(value[1])+' times'

print '\nLotomania:'
for value in collections.Counter(lotomania()).most_common():
  print value[0]+' appeared '+str(value[1])+' times'

print '\nMegasena:'
for value in collections.Counter(megasena()).most_common():
  print value[0]+' appeared '+str(value[1])+' times'

print '\nQuina:'
for value in collections.Counter(quina()).most_common():
  print value[0]+' appeared '+str(value[1])+' times'

print '\n----\nEverything:'
for value in collections.Counter(total).most_common():
  print value[0]+' appeared '+str(value[1])+' times'