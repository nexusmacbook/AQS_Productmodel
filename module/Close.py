import MetaTrader5 as mt5
from module import LineNotify
import time,datetime,traceback

try:
    def close(POSdata):
        #ポジションに合わせた決済情報を作成する
        posTicket = POSdata.ticket 
        posLot    = POSdata.volume
        posSymbol = POSdata.symbol
        posMagic  = POSdata.magic
        posType   = POSdata.type

        #ポジションのtype（売買）に応じて、決済のtypeを指定（反対売買を行う）
        if posType == mt5.ORDER_TYPE_BUY:
            price = mt5.symbol_info_tick(posSymbol).bid
            type = mt5.ORDER_TYPE_SELL
        if posType == mt5.ORDER_TYPE_SELL:
            price = mt5.symbol_info_tick(posSymbol).ask
            type = mt5.ORDER_TYPE_BUY
            
        deviation = 500
        request={
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": posSymbol,
            "volume": posLot,
            "type": type,
            "position": posTicket,
            "price": price,
            "deviation": deviation,
            "magic": posMagic,
            "comment": "python script close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        # 取引リクエストを送信する
        Closeresult = mt5.order_send(request)
        ClosePrice  = Closeresult.price
        return Closeresult,ClosePrice
    
except BaseException as be:

    traceerror = traceback.print_exc()
    LineNotify.LINE(f"\n例外発生:{be}\n{str(traceerror)}")