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
        self.te1 = QPlainTextEdit()  # QPlainTextEdit 위젯 생성
        self.te1.setReadOnly(True)  # 편집 불가능하도록 설정

        self.btn1 = QPushButton("Calc", self)  # "Calc"라는 텍스트를 가진 QPushButton 위젯 생성
        self.btn2 = QPushButton("Clear", self)  # "Clear"라는 텍스트를 가진 QPushButton 위젯 생성

        self.le1 = QLineEdit("0", self)  # "0"이라는 텍스트를 가진 QLineEdit 위젯 생성
        self.le1.setAlignment(QtCore.Qt.AlignRight)  # 오른쪽 정렬 설정
        self.le1.setFocus(True)  # 포커스 설정
        self.le1.selectAll()  # 텍스트 전체 선택

        self.le2 = QLineEdit("0", self)  # "0"이라는 텍스트를 가진 QLineEdit 위젯 생성
        self.le2.setAlignment(QtCore.Qt.AlignRight)  # 오른쪽 정렬 설정

        self.cb = QComboBox(self)  # QComboBox 위젯 생성
        self.cb.addItems(["+", "-", "*", "/"])  # "+", "-", "*", "/" 아이템 추가

        hbox_formular = QHBoxLayout()  # 수평 박스 레이아웃 생성
        hbox_formular.addWidget(self.le1)  # le1 위젯 추가
        hbox_formular.addWidget(self.cb)  # cb 위젯 추가
        hbox_formular.addWidget(self.le2)  # le2 위젯 추가

        hbox = QHBoxLayout()  # 수평 박스 레이아웃 생성
        hbox.addStretch(1)  # 공간 추가
        hbox.addWidget(self.btn1)  # btn1 위젯 추가
        hbox.addWidget(self.btn2)  # btn2 위젯 추가

        vbox = QVBoxLayout()  # 수직 박스 레이아웃 생성
        vbox.addWidget(self.te1)  # te1 위젯 추가
        vbox.addLayout(hbox_formular)  # hbox_formular 레이아웃 추가
        vbox.addLayout(hbox)  # hbox 레이아웃 추가
        vbox.addStretch(1)  # 공간 추가

        self.setLayout(vbox)  # 레이아웃 설정

        self.setWindowTitle("Calculator")  # 창 제목 설정
        self.setWindowIcon(QIcon("icon.png"))  # 아이콘 설정
        self.resize(256, 256)  # 창 크기 설정
        self.show()  # 창 보이기

    def setDisplay(self):
        self.te1.appendPlainText("Button clicked!")  # te1에 "Button clicked!" 텍스트 추가

    def clearMessage(self):
        self.te1.clear()  # te1의 텍스트 모두 지우기
