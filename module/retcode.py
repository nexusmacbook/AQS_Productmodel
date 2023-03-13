## MT5 API URL : https://www.mql5.com/ja/docs/constants/errorswarnings/enum_trade_return_codes
from module import LineNotify
import traceback

try:

    def returnCode(reCode):
        retcode = reCode
        if   retcode == 10004:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_REQUOTE\n約定が拒否されました。価格の再提示を受けました")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_REQUOTE\n約定が拒否されました。価格の再提示を受けました")
        elif retcode == 10006:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_REJECT\nリクエストが拒否されました")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_REJECT\nリクエストが拒否されました")
        elif retcode == 10007:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_CANCEL\nトレーダーによるリクエストのキャンセル")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_CANCEL\nトレーダーによるリクエストのキャンセル")
        elif retcode == 10008:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_PLACED\n注文が出されました")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_PLACED\n注文が出されました")
        elif retcode == 10009:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_DONE\nリクエスト完了")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_DONE\nリクエスト完了")
        elif retcode == 10010:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_DONE_PARTIAL\nリクエストが一部のみ完了")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_DONE_PARTIAL\nリクエストが一部のみ完了")
        elif retcode == 10011:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_ERROR\nリクエスト処理エラー")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_ERROR\nリクエスト処理エラー")
        elif retcode == 10012:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_TIMEOUT\nリクエストが時間切れでキャンセル")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_TIMEOUT\nリクエストが時間切れでキャンセル")
        elif retcode == 10013:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID\n無効なリクエスト")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID\n無効なリクエスト")
        elif retcode == 10014:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_VOLUME\nリクエストのボリュームが無効です")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_VOLUME\nリクエストのボリュームが無効です")
        elif retcode == 10015:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_PRICE\nリクエストの価格が無効です")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_PRICE\nリクエストの価格が無効です")
        elif retcode == 10016:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_STOPS\nリクエストのストップが無効です")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_STOPS\nリクエストのストップが無効です")
        elif retcode == 10017:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_REQUOTE\n取引は無効です")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_REQUOTE\n取引は無効です")
        elif retcode == 10018:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_MARKET_CLOSED\n市場は閉鎖されています")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_MARKET_CLOSED\n市場は閉鎖されています")
        elif retcode == 10019:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_NO_MONEY\n要求を完了するのに十分な金額がありません")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_NO_MONEY\n要求を完了するのに十分な金額がありません")
        elif retcode == 10020:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_PRICE_CHANGED\n価格が変更されました")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_PRICE_CHANGED\n価格が変更されました")
        elif retcode == 10021:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_PRICE_OFF\nリクエスト処理に必要な相場が不在（意訳）")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_PRICE_OFF\nリクエスト処理に必要な相場が不在（意訳）")
        elif retcode == 10022:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_EXPIRATION\n注文有効期限のリクエストが無効です")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_EXPIRATION\n注文有効期限のリクエストが無効です")
        elif retcode == 10023:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_ORDER_CHANGED\n注文ステータスが変更されました")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_ORDER_CHANGED\n注文ステータスが変更されました")
        elif retcode == 10024:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_TOO_MANY_REQUESTS\nリクエストが多すぎます")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_TOO_MANY_REQUESTS\nリクエストが多すぎます")
        elif retcode == 10025:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_NO_CHANGES\nリクエストに変更はありません")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_NO_CHANGES\nリクエストに変更はありません")
        elif retcode == 10026:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_SERVER_DISABLES_AT\nサーバが自動取引を無効化しました")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_SERVER_DISABLES_AT\nサーバが自動取引を無効化しました")
        elif retcode == 10027:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_CLIENT_DISABLES_AT\nクライアント端末が自動取引を無効化しています")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_CLIENT_DISABLES_AT\nクライアント端末が自動取引を無効化しています")
        elif retcode == 10028:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_LOCKED\nリクエストは処理のためにロックされています")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_LOCKED\nリクエストは処理のためにロックされています")
        elif retcode == 10029:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_FROZEN\n注文やポジションが凍結されています")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_FROZEN\n注文やポジションが凍結されています")
        elif retcode == 10030:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_FILL\n無効なORDER_TYPE_FILLINGです")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_FILL\n無効なORDER_TYPE_FILLINGです")
        elif retcode == 10031:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_CONNECTION\n取引サーバに未接続")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_CONNECTION\n取引サーバに未接続")
        elif retcode == 10032:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_ONLY_REAL\nこの操作はリアル口座でないとできません")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_ONLY_REAL\nこの操作はリアル口座でないとできません")
        elif retcode == 10033:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_LIMIT_ORDERS\n未決注文数が上限に達しました")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_LIMIT_ORDERS\n未決注文数が上限に達しました")
        elif retcode == 10034:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_LIMIT_VOLUME\nシンボルの注文とポジションの量が制限に達しました")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_LIMIT_VOLUME\nシンボルの注文とポジションの量が制限に達しました")
        elif retcode == 10035:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_ORDER\nこの注文タイプは誤っているか禁止されています")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_ORDER\nこの注文タイプは誤っているか禁止されています")
        elif retcode == 10036:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_POSITION_CLOSED\n指定された「POSITION_PROPERTY_INTEGER」のポジションは既にクローズされています")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_POSITION_CLOSED\n指定された「POSITION_PROPERTY_INTEGER」のポジションは既にクローズされています")
        elif retcode == 10038:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_CLOSE_VOLUME\n決済ボリュームが現在のポジションのボリュームを超過しています")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_INVALID_CLOSE_VOLUME\n決済ボリュームが現在のポジションのボリュームを超過しています")
        elif retcode == 10039:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_CLOSE_ORDER_EXIST\n指定されたポジションの決済注文が既に存在します。これは、ヘッジ システムで作業しているときに発生する可能性があります。ポジションの決済注文がすでに存在しているときに、反対のポジションでポジションを決済しようとした場合。ポジションを完全または部分的に決済しようとした場合、既に存在するクローズ注文と新しく発注された注文の合計ボリュームが現在のポジションボリュームを超える場合")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_CLOSE_ORDER_EXIST\n指定されたポジションの決済注文が既に存在します。これは、ヘッジ システムで作業しているときに発生する可能性があります。ポジションの決済注文がすでに存在しているときに、反対のポジションでポジションを決済しようとした場合。ポジションを完全または部分的に決済しようとした場合、既に存在するクローズ注文と新しく発注された注文の合計ボリュームが現在のポジションボリュームを超える場合")
        elif retcode == 10040:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_LIMIT_POSITIONS\nアカウントに同時に存在するオープンポジションの数は、サーバー設定によって制限される場合があります。制限に達した後、注文をしようとすると、サーバーは TRADE_RETCODE_LIMIT_POSITIONS エラーを返します。制限は、ポジションの会計タイプによって異なります。ネッティング — オープン ポジションの数が考慮されます。制限に達すると、プラットフォームは、実行によってオープンポジションの数が増える可能性のある新しい注文を出すことを許可しません. 実際、このプラットフォームでは、すでにオープン ポジションを持っているシンボルに対してのみ注文を出すことができます。現在の未決注文は考慮されません。その実行は現在のポジションの変更につながる可能性がありますが、数を増やすことはできないからです。ヘッジ — 未決注文はオープン ポジションと一緒に考慮されます。これは、未決注文のアクティブ化は常に新しいポジションのオープンにつながるためです。制限に達すると、プラットフォームはポジションを開くための新しい成行注文と未決注文の両方を出すことを許可しません。")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_LIMIT_POSITIONS\nアカウントに同時に存在するオープンポジションの数は、サーバー設定によって制限される場合があります。制限に達した後、注文をしようとすると、サーバーは TRADE_RETCODE_LIMIT_POSITIONS エラーを返します。制限は、ポジションの会計タイプによって異なります。ネッティング — オープン ポジションの数が考慮されます。制限に達すると、プラットフォームは、実行によってオープンポジションの数が増える可能性のある新しい注文を出すことを許可しません. 実際、このプラットフォームでは、すでにオープン ポジションを持っているシンボルに対してのみ注文を出すことができます。現在の未決注文は考慮されません。その実行は現在のポジションの変更につながる可能性がありますが、数を増やすことはできないからです。ヘッジ — 未決注文はオープン ポジションと一緒に考慮されます。これは、未決注文のアクティブ化は常に新しいポジションのオープンにつながるためです。制限に達すると、プラットフォームはポジションを開くための新しい成行注文と未決注文の両方を出すことを許可しません。")
        elif retcode == 10041:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_REJECT_CANCEL\n保留中の注文の有効化リクエストが拒否され、注文がキャンセルされました")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_REJECT_CANCEL\n保留中の注文の有効化リクエストが拒否され、注文がキャンセルされました")
        elif retcode == 10042:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_LONG_ONLY\n「ロングポジションのみが許可される」ルールがシンボルに設定されているため、リクエストは拒否されます (POSITION_TYPE_BUY)")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_LONG_ONLY\n「ロングポジションのみが許可される」ルールがシンボルに設定されているため、リクエストは拒否されます (POSITION_TYPE_BUY)")
        elif retcode == 10043:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_SHORT_ONLY\n「ショート ポジションのみが許可される」ルールがシンボルに設定されているため、リクエストは拒否されます(POSITION_TYPE_SELL)")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_SHORT_ONLY\n「ショート ポジションのみが許可される」ルールがシンボルに設定されているため、リクエストは拒否されます(POSITION_TYPE_SELL)")
        elif retcode == 10044:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_CLOSE_ONLY\nシンボルに「ポジションの決済のみが許可される」ルールが設定されているため、リクエストは拒否されます")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_CLOSE_ONLY\nシンボルに「ポジションの決済のみが許可される」ルールが設定されているため、リクエストは拒否されます")
        elif retcode == 10045:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_FIFO_CLOSE\n「ポジションの決済は FIFO ルールによってのみ許可される」フラグが取引口座に設定されているためリクエストは拒否されました(ACCOUNT_FIFO_CLOSE = true) ")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_FIFO_CLOSE\n「ポジションの決済は FIFO ルールによってのみ許可される」フラグが取引口座に設定されているためリクエストは拒否されました(ACCOUNT_FIFO_CLOSE = true) ")
        elif retcode == 10046:
            print(f"\nreturnCode:{retcode}\nTRADE_RETCODE_HEDGE_PROHIBITED\n口座で「単一の銘柄の反対のポジションは無効にする」ルールが設定されているため、リクエストが拒否されます。たとえば、銘柄に買いポジションがある場合、売りポジションを開いたり、売り指値注文を出すことはできません。このルールは口座がヘッジ会計の場合 (ACCOUNT_MARGIN_MODE=ACCOUNT_MARGIN_MODE_RETAIL_HEDGING)のみ適用されます")
            LineNotify.LINE(f"\nreturnCode:{retcode}\nTRADE_RETCODE_HEDGE_PROHIBITED\n口座で「単一の銘柄の反対のポジションは無効にする」ルールが設定されているため、リクエストが拒否されます。たとえば、銘柄に買いポジションがある場合、売りポジションを開いたり、売り指値注文を出すことはできません。このルールは口座がヘッジ会計の場合 (ACCOUNT_MARGIN_MODE=ACCOUNT_MARGIN_MODE_RETAIL_HEDGING)のみ適用されます")
        else:
            print(f"\nother error")
            LineNotify.LINE(f"\nother error")
        
        return retcode

except BaseException as be:

    traceerror = traceback.print_exc()
    LineNotify.LINE(f"\n例外発生:{be}\n{str(traceerror)}")