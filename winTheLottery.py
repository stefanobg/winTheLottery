from requestAPI import lotteryAPI

# https://confiraloterias.com.br/api/megasena/
goldenPot = lotteryAPI(False, 'lX1CWmcqaqVmCP5')
goldenPot.megasena()
print goldenPot.makeABet(6, 60)
