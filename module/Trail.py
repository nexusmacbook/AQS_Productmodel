import MetaTrader5 as mt5
import time,traceback
from module import LineNotify,Close,Voice,retcode
profitA = 0
profitB = 0
profitStertStep  = 0.70 # 1000円なら750円のプロフィット
profitSecondStep = 1.30 # 1000円なら1250円
DealingTime = 0.0

try:
    def TakeProfit(TLProfit,POSdata):
        positions = mt5.positions_get()
        lenCK = len(positions)
        if lenCK == 0:
            profit = 0
            closePrice  = 0
            DealingTime = 0
            return profit,closePrice,DealingTime

        else:
            profitA = TLProfit *profitStertStep
            profitB = TLProfit *profitSecondStep
            while(1):
                positions = mt5.positions_get()
                lenCK = len(positions)
                if lenCK == 0:
                    return profit,closePrice,DealingTime

                else:
                    POSdata   = positions[-1]
                    nowProfit = POSdata.profit
                    if  nowProfit <= profitA:
                        positions = mt5.positions_get()
                        POSdata = positions[-1]
                        profit  = POSdata.profit
                        LineNotify.LINE(f"\n取引終了\n概算損益:{profit}")
                        # ポジションクローズ
                        Closeresult = Close.close(POSdata)
                        closePrice = Closeresult.price
                        retcode.returnCode(Closeresult.retcode)
                        # 通知
                        account_info = mt5.account_info()
                        LineNotify.LINE(f"\nOrderClose完了\n口座残高: {account_info.balance}\n現在の利益: {account_info.profit}\n")
                        return profit,closePrice,DealingTime

                    elif nowProfit >= profitB:
                        profitA = round(nowProfit *profitStertStep,5)
                        profitB = round(nowProfit *profitSecondStep,5)

                    print("\r\n\n トレーリングリアルタイム損益 :" + str(nowProfit) + "\n TLStop価格 : " + str(profitA) + "\033[6A\n\n\n",end="")
                    DealingTime = DealingTime +0.25
                    time.sleep(0.25)
                    
except BaseException as be:

    traceerror = traceback.print_exc()
    LineNotify.LINE(f"\n例外発生:{be}\n{str(traceerror)}")