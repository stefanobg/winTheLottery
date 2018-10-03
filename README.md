# Win the Lottery! [![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
Python script to read the most common APIs from Brazil's lotteries and return insights to make your bet.
<br/>

## 🔥 Motivation
In **Brazil**, we have several lottery games that use the same drawable mechanism. Whether it's luck or not, everyone still doubts.
So it's time to understand the overall patterns and start earning some money! ;)
<br/>

## 🎲 How it works?
Fortunatelly we have an Open API with all the results, since it was born. You can found it [here](https://confiraloterias.com.br/api/megasena/) and see for yourself!

Basically, the script collects all the raffles already made and makes a conglomerate of information to analyze what is common in the results and identify the patterns in order to make a more accurate bet for you!
<br/>

## 🖥 Running the script
1. First you need to be sure that you have **Python 2.7.x** or more installed.
- [Install Python on Mac OS X](https://docs.python-guide.org/starting/install/osx/)
- [Install Python on Linux](https://docs.python-guide.org/starting/install/linux/)
- [Install Python on Windows](https://docs.python-guide.org/starting/install/win/)

2. After that, you need to install **PIP** to manage your packages.
- [Install PIP on Windows, Mac OS X and Linux](https://www.makeuseof.com/tag/install-pip-for-python/)

3. Now that you have both **Python** and **PIP**, you can download the repositorie to the folder you want by opening your ``terminal`` and typing:
```sh
$ git clone https://github.com/stefanobg/winTheLottery/
```

4. Once you have it cloned, go there:
```sh
$ cd winTheLottery
```

5. Before running ``winTheLottery.py`` you need to refresh the **Token** inside it. So, go to the API page, by clicking [here](https://confiraloterias.com.br/api/megasena/) and copy the *authorized Token*:
<img src="https://github.com/stefanobg/winTheLottery/raw/readme/assets/TokenCopy.png">

6. Now, paste it here, and keep in mind that you'll need to do it many times to not loose your access:
<br/>
<img src="https://github.com/stefanobg/winTheLottery/raw/readme/assets/TokenPaste.png">

7. With terminal open on the correct folder type:
```sh
$ python winTheLottery
```
<img src="https://github.com/stefanobg/winTheLottery/raw/readme/assets/Running.gif">
<br/>

## ⚡️ Modifying the output
Open ``winTheLottery.py``and insert **some or all of these lines** to collect different data to improve the accuracy:
```python
  from requestAPI import lotteryAPI

  goldenPot = lotteryAPI(False, 'Updated Token Here')

  goldenPot.duplasena()
  goldenPot.lotofacil()
  goldenPot.megasena()
  goldenPot.lotomania()
  goldenPot.quina()

  for i in xrange(2):
    print goldenPot.makeABet(6, 60)
```
<br/>

If you want to print all the raffles you need to insert this line after creating the ``lotteryAPI`` and before making a request:
```python
  lotteryAPI.enablePrint()
  lotteryAPI.disablePrint()
```
<br/>








