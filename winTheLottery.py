from requestAPI import lotteryAPI

# https://confiraloterias.com.br/api/megasena/
goldenPot = lotteryAPI(False, '47jk3cGexyCxJjS')
goldenPot.megasena()
print goldenPot.makeABet(6, 60)
