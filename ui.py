from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QPlainTextEdit,
    QHBoxLayout,
    QLabel,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate, Qt


class View(QWidget):
    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        # 현재 날짜를 표시하는 라벨 생성
        self.lbl1 = QLabel(self.date.toString(Qt.DefaultLocaleLongDate), self)

        # 텍스트를 편집할 수 있는 플레인 텍스트 에디터 생성
        self.te1 = QPlainTextEdit()
        self.te1.setReadOnly(True)

        # 메시지 버튼 생성
        self.btn1 = QPushButton("Message", self)
        # 클리어 버튼 생성
        self.btn2 = QPushButton("Clear", self)

        # 메시지 버튼과 클리어 버튼을 수평으로 정렬하는 레이아웃 생성
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(self.btn1)
        hbox.addWidget(self.btn2)

        # 플레인 텍스트 에디터와 버튼 레이아웃, 날짜 라벨을 수직으로 정렬하는 레이아웃 생성
        vbox = QVBoxLayout()
        vbox.addWidget(self.te1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.lbl1)

        # 수직 레이아웃을 위젯의 레이아웃으로 설정
        self.setLayout(vbox)

        # 창의 제목 설정
        self.setWindowTitle("Calculator")
        # 창의 아이콘 설정
        self.setWindowIcon(QIcon("icon.png"))
        # 창의 크기 설정
        self.resize(256, 256)
        # 창을 화면에 표시
        self.show()

    def activateMessage(self):
        # 버튼이 클릭되었을 때 메시지를 플레인 텍스트 에디터에 추가
        self.te1.appendPlainText("Button clicked!")

    def clearMessage(self):
        # 플레인 텍스트 에디터의 내용을 지움
        self.te1.clear()
