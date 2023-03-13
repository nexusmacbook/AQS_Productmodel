import csv,sqlite3,datetime
import os.path


def DataBase(acNo,orderDate,AQscale,orderprice,closePrice,ProfitScore):
    
    filename = f"{acNo}_Log.csv"
    
    # CSVファイルが存在するか確認し、存在しなければ作成する
    if not os.path.isfile(filename):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['LogDate','OrderDate', 'AQscale', 'OrderPrice','ClosePrice','ProfitScore'])

    # CSVファイルにデータを追記する
    with open(filename, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), orderDate, AQscale, orderprice, closePrice, ProfitScore])

    # データベースに格納する
    conn = sqlite3.connect('order.db')  # 仮のデータベース名
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS logs
                (log_date text, order_date text, aq_scale real, order_price real, close_price real, profit_score real)''')
    conn.commit()

    # CSVファイルの内容をデータベースに挿入する
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # ヘッダー行をスキップする
        for row in reader:
            c.execute("INSERT INTO logs VALUES (?, ?, ?, ?, ?, ?)", row)

    conn.commit()
    conn.close()
