import MetaTrader5 as mt5
from module import LoginInfo,LineNotify,AQS

flg = True

acNo,STbalance = LoginInfo()
AQS(flg)

