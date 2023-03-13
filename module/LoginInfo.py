import MetaTrader5 as mt5
import inquirer,datetime,os,sys,traceback
from module import LineNotify

STbalance = 0.0

try:
    class init:
        def CLI_account(accountSet,MT5_init):
            while(accountSet):
                SETaccount = [inquirer.List(
                            "account",
                            message = "Please select the AXIORY account",
                            choices = ["XM-Demo1","Axiory-Demo1","AxioryLive","XMTradingLive"],
                            carousel= True,)
                ]
                SETaccount = inquirer.prompt(SETaccount)
                SETaccount_val = SETaccount["account"]
                print(f"Select The {SETaccount_val} account.\nPlease Standby...\n")
                
                if   SETaccount_val == "XM-Demo1":
                    acNo   =  27020029
                    acPass = "Kouhei1989"
                    acSer  = "XMTrading-MT5"
                elif SETaccount_val == "Axiory-Demo1":
                    acNo   = 20011257
                    acPass = "Kouhei1989"
                    acSer  = "Axiory-Demo"
                elif SETaccount_val == "AxioryLive":
                    acNo   = 2015691
                    acPass = "Kouhei1989"
                    acSer  = "Axiory-Live"
                elif SETaccount_val == "XMTradingLive":
                    acNo   = 70360710
                    acPass = "Kouhei1989"
                    acSer  = "XMTrading-MT5 3"

                accCheckCLI = [inquirer.List(
                    "finalCheck",
                    message = "Please select the answer. Are you sure this is your choice?",
                    choices = ["No", "Yes"],
                    carousel= True,)
                ]

                lotsaiz   = [inquirer.List(
                            "lotsaiz",
                            message = "Please select the lot Size",
                            choices = ["1","5","10","15","20","25","30"],
                            carousel= True,)
                ]
                lotsaiz = inquirer.prompt(lotsaiz)
                lotsaiz_Val = lotsaiz["lotsaiz"]

                soundselect   = [inquirer.List(
                            "soundselect",
                            message = "Please select the Sound",
                            choices = ["No","YES"],
                            carousel= True,)
                ]
                soundselect = inquirer.prompt(soundselect)
                soundselect_Val = soundselect["soundselect"]
                if soundselect_Val == "YES":
                    soundAct = 1
                else:
                    soundAct = 0

                if MT5_init == False:
                    if not mt5.initialize():
                        print(f"initialize error\nerror code : {mt5.last_error()}")
                        status = 1
                        return status
                    print(f"MetaTrader5 package Version : {mt5.__version__}")
                    mt5.login(acNo,acPass,acSer)
                    account_info = mt5.account_info()
                    print(f"\n最大レバレッジ: {account_info.leverage}\n現在の利益: {account_info.profit}\n口座所有者: {account_info.name}\n口座残高: {account_info.balance}\n")

                accCheckCLI = inquirer.prompt(accCheckCLI)
                accCheckans_val = accCheckCLI["finalCheck"]
                if accCheckans_val == "Yes":
                    print(f"Your Choice : {SETaccount_val} account")
                    print("\nSystem Start...\n")
                    MT5Retrun = init.MT5(acNo,acPass,acSer)
                    returnAcNo,STbalance = MT5Retrun
                    return returnAcNo,lotsaiz_Val,soundAct,STbalance

                elif accCheckans_val == "No":
                    print(f"\nPlease try again.\n\n")

        def MT5(acNo,acPass,acSer):
            if not mt5.initialize():
                print(f"initialize error\nerror code : {mt5.last_error()}")
                status = 1
                return status
            print(f"MetaTrader5 package Version : {mt5.__version__}")

            authorized = mt5.login(acNo,acPass,acSer)
            if not authorized:
                print(f"User Authorization Failed")
                status = 2
                return status
            account_info = mt5.account_info()
            STbalance = account_info.balance
            if account_info is None:
                print("Retreiving account information failed")
                status = 3
                return status

            now = datetime.datetime.now()
            startTime = now.strftime(f"{now:%Y-%m-%d %H:%M:%S}")
            print(f"\n最大レバレッジ: {account_info.leverage}\n現在の利益: {account_info.profit}\n口座所有者: {account_info.name}\n口座残高: {account_info.balance}")
            LineNotify.LINE(f"\n{startTime}\n取引開始処理終了\n{startTime}\n最大レバレッジ: {account_info.leverage}\n現在の利益: {account_info.profit}\n口座所有者: {account_info.name}\n口座残高: {account_info.balance}\n")
            return acNo,STbalance
        
        
        
        
        def MT5TEST(acNo,acPass,acSer):
            if not mt5.initialize():
                print(f"initialize error\nerror code : {mt5.last_error()}")
                status = 1
                return status
            print(f"MetaTrader5 package Version : {mt5.__version__}")

            authorized = mt5.login(acNo,acPass,acSer)
            if not authorized:
                print(f"User Authorization Failed")
                status = 2
                return status
            account_info = mt5.account_info()
            if account_info is None:
                print("Retreiving account information failed")
                status = 3
                return status
            
            STbalance = account_info.balance

            now = datetime.datetime.now()
            startTime = now.strftime(f"{now:%Y-%m-%d %H:%M:%S}")
            print(f"\n最大レバレッジ: {account_info.leverage}\n現在の利益: {account_info.profit}\n口座所有者: {account_info.name}\n口座残高: {account_info.balance}")
            LineNotify.LINE(f"\n{startTime}\n取引開始処理終了\n{startTime}\n最大レバレッジ: {account_info.leverage}\n現在の利益: {account_info.profit}\n口座所有者: {account_info.name}\n口座残高: {account_info.balance}\n")
            return STbalance
    
except BaseException as be:

    traceerror = traceback.print_exc()
    LineNotify.LINE(f"\n例外発生:{be}\n{str(traceerror)}")