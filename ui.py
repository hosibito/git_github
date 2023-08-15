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
        # 텍스트 편집기 생성
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        # 메시지 버튼 생성
        self.btn1 = QPushButton("Message", self)
        # 클리어 버튼 생성
        self.btn2 = QPushButton("Clear", self)

        # 첫 번째 입력 상자 생성
        self.le1 = QLineEdit("0", self)
        self.le1.setAlignment(QtCore.Qt.AlignRight)

        # 두 번째 입력 상자 생성
        self.le2 = QLineEdit("0", self)
        self.le2.setAlignment(QtCore.Qt.AlignRight)

        # 연산자 선택 상자 생성
        self.cb = QComboBox(self)
        self.cb.addItems(["+", "-", "*", "/"])

        # 수식 입력 상자를 가로로 정렬하는 레이아웃 생성
        hbox_formular = QHBoxLayout()
        hbox_formular.addWidget(self.le1)
        hbox_formular.addWidget(self.cb)
        hbox_formular.addWidget(self.le2)

        # 버튼을 가로로 정렬하는 레이아웃 생성
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

        # 윈도우 타이틀 설정
        self.setWindowTitle("Calculator")
        # 아이콘 설정
        self.setWindowIcon(QIcon("icon.png"))
        # 윈도우 크기 설정
        self.resize(256, 256)
        # 윈도우를 화면에 표시
        self.show()

    # 메시지 활성화 함수
    def activateMessage(self, text):
        self.te1.appendPlainText(text)

    # 메시지 클리어 함수
    def clearMessage(self):
        self.te1.clear()
