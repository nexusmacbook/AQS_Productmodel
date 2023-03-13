import MetaTrader5 as mt5
import os,sys,time,datetime,traceback
from module import LineNotify,AQS,Order,retcode


try:
    def orderSet(symbolVal,SLpasen,TPpasen,orderType,lotSize):
        
        Dev = 500
        
        if orderType == "Sell":
            Type         = mt5.ORDER_TYPE_SELL
            price        = mt5.symbol_info_tick(symbolVal).bid
            JPYprice     = mt5.symbol_info_tick("USDJPY").ask
            priceConask  = mt5.symbol_info_tick("USDJPY").ask
            sellMagic    = sellMagic - 1
            Magic        = sellMagic
            stopLoss     = round(price + SLpasen,3)
            takeProfit   = round(price - TPpasen,3)
        
        elif orderType == "Buy":
            Type         = mt5.ORDER_TYPE_BUY
            price        = mt5.symbol_info_tick(symbolVal).ask
            JPYprice     = mt5.symbol_info_tick("USDJPY").bid
            priceConbid  = mt5.symbol_info_tick("USDJPY").bid
            buyMagic     = buyMagic + 1
            Magic        = buyMagic
            stopLoss     = round(price - SLpasen,3)
            takeProfit   = round(price + TPpasen,3)
            
        # OrderSend
        # 成り行き売り注文を出す
        orderResult = Order.orderReq(
            SYMBOL  = symbolVal, 
            vol     = lotSize,
            Price   = price,
            dev     = Dev,
            magic   = Magic,
            type    = Type,
            sl      = stopLoss,
            tp      = takeProfit,
        )

        ticket     = orderResult.order
        Code       = orderResult.retcode
        orderprice = orderResult.price
        
        #オーダー日時取得
        now = datetime.now()
        orderDate = now.strftime("%Y-%m-%d %H:%M:%S")
        
        retcode.returnCode(Code)
        return lotSize,orderDate,orderprice
        
        
    def orderReq(SYMBOL,vol,Price,dev,magic,type,sl=None, tp=None, position=None):
        request = {
            'action': mt5.TRADE_ACTION_DEAL,
            'symbol': SYMBOL,
            'volume': vol,
            'price': Price,
            'deviation': dev,   # float型じゃだめ
            'magic': magic,
            'comment': "python script open",    # 何でもOK
            'type_time': mt5.ORDER_TIME_GTC,
            'type': type,
            'type_filling': mt5.ORDER_FILLING_IOC, # ブローカーにより異なる
        }

        if sl is not None:
            request.update({"sl": sl,})
        if tp is not None:
            request.update({"tp": tp,})
        if position is not None:
            request.update({"position": position})

        orderResult = mt5.order_send(request)
        print(orderResult)
        return orderResult

except BaseException as be:

    traceerror = traceback.print_exc()
    LineNotify.LINE(f"\n例外発生:{be}\n{str(traceerror)}")
    