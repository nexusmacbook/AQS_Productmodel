import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.uic import loadUi
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QSizePolicy
from PySide6.QtWidgets import QHBoxLayout, QPushButton, QWidget


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # UIファイルをロードする
        loadUi('module/top.ui', self)
        # ウィジェットを作成する
        widget = QWidget()
        layout = QHBoxLayout()
        newbtn = QPushButton(u"新規口座登録")
        loginbtn = QPushButton(u"ログイン口座接続")
        changebtn = QPushButton(u"口座情報変更")
        layout.addWidget(newbtn)
        layout.addWidget(loginbtn)
        layout.addWidget(changebtn)
        widget.setLayout(layout)
        # ウィジェットをセントラルウィジェットとして設定する
        self.setCentralWidget(widget)
        # ウィンドウを表示する
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
