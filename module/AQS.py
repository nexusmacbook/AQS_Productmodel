import time,datetime,requests,traceback
from module import LineNotify

Datalist = []

try:
    def AQcheck(flg):
        while(flg):
            TimeA = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
            now = TimeA + datetime.timedelta(seconds=-5)
            TimeST = now.strftime('%Y%m%d%H%M%S')
            URL = "http://www.kmoni.bosai.go.jp/webservice/hypo/eew/" + TimeST + ".json"
            raw = requests.get(URL)
            Data = raw.json()   #辞書型（dict)
            AQ = Data["result"]["message"]
            if Data == '':
                TIMESP = 5
                trigger(Data,TimeST)
            time.sleep(TIMESP)

    def trigger(Data,TimeST):
    # # # 地震検知後ルーチン。地震情報検出サイクルを１秒に変更
        TIMESP = 1
    # # #リクエスト時刻（str）/情報更新時刻(YYYY/MM/DD hh:mm:dd形式)/地震発生時刻/第n報/震源地/震源の深さ/最大震度/マグニチュード/最終報か否か
        Datalist = TimeST,Data["request_time"],Data["report_time"],Data["origin_time"],Data["report_num"],Data["region_name"] \
        ,Data["depth"],Data["calcintensity"],Data["magunitude"],Data["is_final"]

    ##--####--####--####--####--####--####--##


# # # 地震速報第一報をライン通知するだけ
        if ichiflg == 0:
            preShindo = Data["calcintensity"]
            LINE("地震速報検出\n第一報震度:%s" % preShindo)
            ichiflg = 1

# # # 最終報告かいなかの判定
        if Data["is_final"] == True:
            Shindo = Data["calcintensity"]

##--####--####--####--####--####--####--##　震度変数名をlastshindoに変更（preが続くとわかりにくいので）

# # # 地震速報最終震度をライン通知するだけ
            if lastflg == 0:
                lastShindo = Data["calcintensity"]
                LINE("地震速報\n最終報震度:%s" % lastShindo)
                lastflg = 1

##--####--####--####--####--####--####--##


# # # 最終報ならその震度を判定。震度1以上で発注（上段が半角下段が全角）
            if  Shindo == '1' or Shindo == '2' or Shindo == '3' or Shindo == '4' or Shindo == '5弱' or Shindo == '5強' or Shindo == '6弱' \
                or Shindo == '6強' or Shindo == '7':
                LINE("震度:%s\n規定震度到達\n発注しました" % zishin)
                ichiflg = 0
                lastflg = 0
                main()
                TLSP()
            else:
                ichiflg = 0
                lastflg = 0
                print("規定震度以下です。\n発注キャンセル致しました")
##--####--####--####--####--####--####--##　timespを規定時間40に変更
                TIMESP = timeDef
##--####--####--####--####--####--####--##
except BaseException as be:

    traceerror = traceback.print_exc()
    LineNotify.LINE(f"\n例外発生:{be}\n{str(traceerror)}")