import MetaTrader5 as mt5
import time,datetime,traceback
from module import LoginInfo,LineNotify,AQS,DB,Voice,Order,Trail,Close

#トレール注文に以降するタイミングを管理するデフォルトの利益（円）
DefProfit = 500
#ストップロス設定値（バックアップ値）
STOPrate = 0.7

#Login不調につきアキシオリーデモをデフォルトに
acNo   = 20011257
acPass = "Kouhei1989"
acSer  = "Axiory-Demo"

try:
    def initMT5():
        startUp = LoginInfo.init.CLI_account(True,False)
        acNo,lotSize,soundAct,STbalance = startUp
        StopLoss = STbalance*STOPrate
        return acNo,lotSize,soundAct,STbalance,StopLoss
    
    def StartMT5(acNo,acPass,acSer):
        startUponly = LoginInfo.init.MT5TEST
        STbalance = startUponly
        return STbalance

    def AQchechk(StopLoss):
        AQscale = AQS(True)
        
        symbolVal = "USDJPY"
        orderType = "Sell"
        
        if AQscale == "3":
            lotSize = 1
            SLpasen = 150
            TPpasen = 100
        elif AQscale == "4":
            lotSize = 1.5
            SLpasen = 150
            TPpasen = 100
        elif AQscale == "5弱":
            lotSize = 2.5
            SLpasen = 200
            TPpasen = 200
        elif AQscale == "5強":
            lotSize = 4
            SLpasen = 200
            TPpasen = 250
        elif AQscale == "6弱":
            lotSize = 6
            SLpasen = 200
            TPpasen = 300
        elif AQscale == "6強":
            lotSize = 9.5
            SLpasen = 200
            TPpasen = 400
        elif AQscale == "7":
            lotSize = 13.5
            SLpasen = 200
            TPpasen = 500
        
        orderSend = Order.orderSet(symbolVal,SLpasen,TPpasen,orderType,lotSize)
        lotSize,orderDate,orderprice = orderSend


        #トレール注文前のチェック＆ストップロスのバックアップルーチン
        TrailFlg = True
        while(TrailFlg):
            positions = mt5.positions_get()
            POSdata   = positions[-1]
            TLProfit  = POSdata.profit
            
            if TLProfit >= DefProfit:
                TrailFlg = False
                CloseResult = Trail.TakeProfit(TLProfit,POSdata)
                profit,closePrice,DealingTime = CloseResult
                return profit,closePrice,DealingTime,orderDate,orderprice,AQscale
                
            elif TLProfit <= StopLoss:
                TrailFlg = False
                CloseResult = Close.close(POSdata)
                Closeresult,closePrice = CloseResult
                return closePrice,orderDate,orderprice,AQscale
            
            else:
                pass
            
            
            

            
        
    def DBMaster(acNo,orderDate,AQscale,orderprice,closePrice):
        
        ProfitScore = round(orderprice - closePrice,3)
        DB.DataBase(acNo,orderDate,AQscale,orderprice,closePrice,ProfitScore)
    
    # strtSys = initMT5()
    # acNo,lotSize,soundAct,STbalance,StopLoss = strtSys
    
    sound = "Activate Nexus Trading Systems"
    EGNvoice = Voice.soundENG(sound,soundAct)
    
    AQSResult = AQchechk(StopLoss)
    profit,closePrice,DealingTime,orderDate,orderprice,AQscale = AQSResult
    
    DBMaster(acNo,orderDate,AQscale,orderprice,closePrice)

        
        

except BaseException as be:

    traceerror = traceback.print_exc()
    LineNotify.LINE(f"\n例外発生:{be}\n{str(traceerror)}")