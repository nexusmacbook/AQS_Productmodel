import MetaTrader5 as mt5
import inquirer,datetime,os,sys
from module import LineNotify

STbalance = 0.0

class init:
    def CLI_account(accountSet,MT5_init):
        while(accountSet):
            SETaccount = [inquirer.List(
                        "account",
                        message = "Please select the AXIORY account",
                        choices = ["Demo1", "Demo2", "Demo3","Demo4","Demo5","AxioryLive","XMTradingLive"],
                        carousel= True,)
            ]
            SETaccount = inquirer.prompt(SETaccount)
            SETaccount_val = SETaccount["account"]
            print(f"Select The {SETaccount_val} account.\nPlease Standby...\n")
            if   SETaccount_val == "Demo1":
                acNo = 20010539
                acPass = "Kouhei1989"
                acSer  = "Axiory-Demo"
            elif SETaccount_val == "Demo2":
                acNo   = 20010556
                acPass = "Kouhei1989"
                acSer  = "Axiory-Demo"
            elif SETaccount_val == "Demo3": 
                acNo   = 20010557
                acPass = "Kouhei1989"
                acSer  = "Axiory-Demo"
            elif SETaccount_val == "Demo4":
                acNo   = 20010582
                acPass = "Kouhei1989"
                acSer  = "Axiory-Demo"
            elif SETaccount_val == "Demo5":
                acNo   = 20010594
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

            Timeinter   = [inquirer.List(
                        "Timeinter",
                        message = "Please select the interval",
                        choices = ["15","30","45","60","75","90","105","120","135","150"],
                        carousel= True,)
            ]
            Timeinter = inquirer.prompt(Timeinter)
            Timeinter_var = Timeinter["Timeinter"]

            lotsaiz   = [inquirer.List(
                        "lotsaiz",
                        message = "Please select the lot Size",
                        choices = ["1","5","10","15","20","25","30"],
                        carousel= True,)
            ]
            lotsaiz = inquirer.prompt(lotsaiz)
            lotsaiz_Val = lotsaiz["lotsaiz"]

            traillimit   = [inquirer.List(
                        "traillimit",
                        message = "Please select the traillimit",
                        choices = ["10%","20%","30%","40%","50%","60%","70%","80%"],
                        carousel= True,)
            ]
            traillimit = inquirer.prompt(traillimit)
            traillimit_Val = traillimit["traillimit"]
            if   traillimit_Val == "10%":
                traillimit_Val = 0.10
            elif traillimit_Val == "20%":
                traillimit_Val = 0.20
            elif traillimit_Val == "30%":
                traillimit_Val = 0.30
            elif traillimit_Val == "40%":
                traillimit_Val = 0.40
            elif traillimit_Val == "50%":
                traillimit_Val = 0.50
            elif traillimit_Val == "60%":
                traillimit_Val = 0.60
            elif traillimit_Val == "70%":
                traillimit_Val = 0.70
            elif traillimit_Val == "80%":
                traillimit_Val = 0.80


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
                returnAcNo,STbalance = init.MT5(acNo,acPass,acSer)
                return returnAcNo,Timeinter_var,lotsaiz_Val,traillimit_Val,soundAct,STbalance

            elif accCheckans_val == "No":
                print(f"\nPlease try again.\n\n")

    def CLI_account_Tsuyoshi(accountSet,MT5_init):
        while(accountSet):
            SETaccount = [inquirer.List(
                        "account",
                        message = "Please select the AXIORY account",
                        choices = ["Demo1"],
                        carousel= True,)
            ]
            SETaccount = inquirer.prompt(SETaccount)
            SETaccount_val = SETaccount["account"]
            print(f"Select The {SETaccount_val} account.\nPlease Standby...\n")
            if   SETaccount_val == "Demo1":
                acNo   =  5009661332
                acPass = "roeog1wu"
                acSer  = "MetaQuotes-Demo"
            else:
                pass

            accCheckCLI = [inquirer.List(
                "finalCheck",
                message = "Please select the answer. Are you sure this is your choice?",
                choices = ["No", "Yes"],
                carousel= True,)
            ]

            Timeinter   = [inquirer.List(
                        "Timeinter",
                        message = "Please select the interval",
                        choices = ["15","30","45","60","75","90","105","120","135","150"],
                        carousel= True,)
            ]
            Timeinter = inquirer.prompt(Timeinter)
            Timeinter_var = Timeinter["Timeinter"]

            lotsaiz   = [inquirer.List(
                        "lotsaiz",
                        message = "Please select the lot Size",
                        choices = ["1","5","10","15","20","25","30"],
                        carousel= True,)
            ]
            lotsaiz = inquirer.prompt(lotsaiz)
            lotsaiz_Val = lotsaiz["lotsaiz"]

            traillimit   = [inquirer.List(
                        "traillimit",
                        message = "Please select the traillimit",
                        choices = ["10%","20%","30%","40%","50%","60%","70%","80%"],
                        carousel= True,)
            ]
            traillimit = inquirer.prompt(traillimit)
            traillimit_Val = traillimit["traillimit"]
            if   traillimit_Val == "10%":
                traillimit_Val = 0.10
            elif traillimit_Val == "20%":
                traillimit_Val = 0.20
            elif traillimit_Val == "30%":
                traillimit_Val = 0.30
            elif traillimit_Val == "40%":
                traillimit_Val = 0.40
            elif traillimit_Val == "50%":
                traillimit_Val = 0.50
            elif traillimit_Val == "60%":
                traillimit_Val = 0.60
            elif traillimit_Val == "70%":
                traillimit_Val = 0.70
            elif traillimit_Val == "80%":
                traillimit_Val = 0.80


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
                returnAcNo,STbalance = init.MT5(acNo,acPass,acSer)
                return returnAcNo,STbalance,Timeinter_var,lotsaiz_Val,traillimit_Val,soundAct

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