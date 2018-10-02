# https://confiraloterias.com.br/api/megasena/
import collections, numpy
import urllib2, json
import random

class lotteryAPI(object):
  printable = False
  total = []
  token = ''

  def __init__(self, printData, tokenAPI):
    self.printable = printData
    self.token = tokenAPI
    print "It's time to earn money :D"

  def disablePrint(self):
    self.printable = False

  def enablePrint(self):
    self.printable = True
    print 'Now you can print the values!'

  def printArray(self, data, category):
    if not self.printable:
      return data
    else:
      print '\n' + category.capitalize()
      for value in collections.Counter(data).most_common():
        print value[0]+' appeared '+str(value[1])+' times'
      return 0

  def duplasena(self):
    return self.printArray(self.getResults('duplasena'), 'duplasena')

  def lotofacil(self):
    return self.printArray(self.getResults('lotofacil'), 'lotofacil')

  def lotomania(self):
    return self.printArray(self.getResults('lotomania'), 'lotomania')

  def megasena(self):
    return self.printArray(self.getResults('megasena'), 'megasena')

  def quina(self):
    return self.printArray(self.getResults('quina'), 'quina')

  def readAPI(self, category):
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
    response = opener.open('http://confiraloterias.com.br/api0/json.php?loteria='+category+'&lista=true&concurso=1&token='+self.token)
    data = json.loads(response.read().decode('utf_8', 'ignore'))
    if "erro" in data:
      print 'Please, update the Token from API website to move on.'
      exit()
    else:
      return data

  def getResults(self, category):
    results = []
    for pair in self.readAPI(category):
      if category != 'duplasena':
        for value in pair.get("concurso").get("dezenas"):
          results.append(value)
          self.total.append(value)
      else:
        for value in pair.get("concurso").get("dezenas_1"):
          results.append(value)
          self.total.append(value)
        for value in pair.get("concurso").get("dezenas_2"):
          results.append(value)
          self.total.append(value)
    return results

  def makeABet(self, amount, rangeSize):
    if self.total:
      bet = []
      while len(bet) < amount:
        number = random.randint(1, len(self.total))
        if (self.total[number] not in bet) and (number < rangeSize):
          bet.append(self.total[number])
      bet.sort()
      result = '\nThis is your game:\n'
      for x in bet:
        result += x
        if x != bet[len(bet) - 1]:
          result += ' - '
        else:
          result += '\n'
      return result
    else:
      print 'First you need to consume the API with some game.'