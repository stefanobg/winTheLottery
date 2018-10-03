from requestAPI import lotteryAPI

# https://confiraloterias.com.br/api/megasena/
goldenPot = lotteryAPI(False, 'FQrVkXLqxm13Wcj')
goldenPot.megasena()

for i in xrange(2):
  print goldenPot.makeABet(6, 60)



