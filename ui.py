from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QPlainTextEdit,
    QHBoxLayout,
    QLineEdit,
    QComboBox,
)
from PyQt5.QtGui import QIcon
from PyQt5 import QtCore


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # QPlainTextEdit 위젯 생성
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        # QPushButton 위젯 생성
        self.btn1 = QPushButton("Message", self)
        self.btn2 = QPushButton("Clear", self)

        # QLineEdit 위젯 생성
        self.le1 = QLineEdit("0", self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)

        self.le2 = QLineEdit("0", self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        # QComboBox 위젯 생성
        self.cb = QComboBox(self)
        self.cb.addItems(["+", "-", "*", "/"])

        # 수식 입력을 위한 QHBoxLayout 생성
        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        # 버튼을 담을 QHBoxLayout 생성
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        # 전체 레이아웃 생성
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox_formular)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        # 전체 레이아웃을 윈도우에 설정
        self.setLayout(vbox)

        # 윈도우 타이틀과 아이콘 설정
        self.setWindowTitle("Calculator")
        self.setWindowIcon(QIcon("icon.png"))
        self.resize(256, 256)
        self.show()

    # "Message" 버튼 클릭 시 호출되는 함수
    def activateMessage(self):
        self.te1.appendPlainText("Button clicked!")

    # "Clear" 버튼 클릭 시 호출되는 함수
    def clearMessage(self):
        self.te1.clear()
