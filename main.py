import MetaTrader5 as mt5
from module import LoginInfo,LineNotify,AQS

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # UIファイルをロードする
        loadUi('top.ui', self)
        # ウィンドウを表示する
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec_())
