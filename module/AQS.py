import time,datetime,requests,traceback
from module import LineNotify,Order

Datalist = []
timeDef  = 45

try:
    def AQcheck(flg):
        TIMESP = timeDef
        while(flg):
            TimeA = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
            now = TimeA + datetime.timedelta(seconds=-5)
            TimeST = now.strftime('%Y%m%d%H%M%S')
            URL = "http://www.kmoni.bosai.go.jp/webservice/hypo/eew/" + TimeST + ".json"
            raw = requests.get(URL)
            Data = raw.json()   #辞書型（dict)
            AQ = Data["result"]["message"]
            if AQ == '':
                trigger(Data,TimeST,flg)
            time.sleep(TIMESP)

    def trigger(Data,TimeST,flg):
        TIMESP = 5
        firstLine = 0
        lastLine  = 0
        while(flg):
            time.sleep(TIMESP)
            TimeA = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
            now = TimeA + datetime.timedelta(seconds=-5)
            TimeST = now.strftime('%Y%m%d%H%M%S')
            URL = "http://www.kmoni.bosai.go.jp/webservice/hypo/eew/" + TimeST + ".json"
            raw = requests.get(URL)
            Data = raw.json()

        # # #リクエスト時刻（str）/情報更新時刻(YYYY/MM/DD hh:mm:dd形式)/地震発生時刻/第n報/震源地/震源の深さ/最大震度/マグニチュード/最終報か否か
            Datalist = TimeST,Data["request_time"],Data["report_time"],Data["origin_time"],Data["report_num"],Data["region_name"] \
            ,Data["depth"],Data["calcintensity"],Data["magunitude"],Data["is_final"]
            # # # 地震速報第一報をライン通知するだけ
            if  firstLine == 0:
                preShindo = Data["calcintensity"]
                LineNotify.LINE("地震速報検出\n第一報震度:%s" % preShindo)
                firstLine = 1

        # # # 最終報告かいなかの判定
            if Data["is_final"] == True:
                AQscale = Data["calcintensity"]
                if lastLine == 0:
                    AQscale = Data["calcintensity"]
                    LineNotify.LINE("地震速報\n最終報震度:%s" % AQscale)
                    lastLine = 1
                    
        # # # 最終報ならその震度を判定。震度1以上で発注（上段が半角下段が全角）
                if  AQscale == '1' or AQscale == '2' or AQscale == '3' or AQscale == '4' or AQscale == '5弱' or AQscale == '5強' or AQscale == '6弱' \
                    or AQscale == '6強' or AQscale == '7':
                    LineNotify.LINE("震度:%s\n規定震度到達\n発注しました" % AQscale)
                    firstLine  = 0
                    lastLine   = 0
                    AQscale = ""
                    TIMESP = timeDef
                    return AQscale
                else:
                    firstLine  = 0
                    lastLine   = 0
                    AQscale = ""
                    TIMESP = timeDef
                    LineNotify("震度:%s\n規定震度以下です。\n発注キャンセル致しました" % AQscale)
                    return AQscale

except BaseException as be:

    traceerror = traceback.print_exc()
    LineNotify.LINE(f"\n例外発生:{be}\n{str(traceerror)}")