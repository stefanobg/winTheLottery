# https://confiraloterias.com.br/api/megasena/
import urllib2, json
import collections, numpy

dezenas = []

opener = urllib2.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
response = opener.open('http://confiraloterias.com.br/api0/json.php?loteria=megasena&lista=true&concurso=1&token=t6gmJaewcjkI7xf')
data = json.loads(response.read())

for pair in data:
  for value in pair.get("concurso").get("dezenas"):
    dezenas.append(value)

ocurrencies = collections.Counter(dezenas)
items = collections.Counter(str(item) for item in ocurrencies)

print ocurrencies
