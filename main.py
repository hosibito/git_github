import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QPlainTextEdit,
    QHBoxLayout,
)
from PyQt5.QtGui import QIcon


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()  # QPlainTextEdit 위젯 생성
        self.te1.setReadOnly(True)  # 편집 불가능하도록 설정

        self.btn1 = QPushButton(
            "Message", self
        )  # "Message"라는 텍스트를 가진 QPushButton 위젯 생성
        self.btn1.clicked.connect(
            self.activateMessage
        )  # 버튼 클릭 시 activateMessage 메서드 호출

        self.btn2 = QPushButton("Clear", self)  # "Clear"라는 텍스트를 가진 QPushButton 위젯 생성
        self.btn2.clicked.connect(self.clearMessage)  # 버튼 클릭 시 clearMessage 메서드 호출

        hbox = QHBoxLayout()  # 수평 박스 레이아웃 생성
        hbox.addStretch(1)  # 공간을 늘려서 버튼을 오른쪽으로 밀어냄
        hbox.addWidget(self.btn1)  # 버튼1을 수평 박스에 추가
        hbox.addWidget(self.btn2)  # 버튼2를 수평 박스에 추가

        vbox = QVBoxLayout()  # 수직 박스 레이아웃 생성
        vbox.addWidget(self.te1)  # QPlainTextEdit 위젯을 수직 박스에 추가
        vbox.addLayout(hbox)  # 수평 박스 레이아웃을 수직 박스에 추가
        vbox.addStretch(1)  # 공간을 늘려서 수직 박스의 아래쪽으로 밀어냄

        self.setLayout(vbox)  # 수직 박스 레이아웃을 윈도우의 레이아웃으로 설정

        self.setWindowTitle("Calculator")  # 윈도우 타이틀 설정
        self.setWindowIcon(QIcon("icon.png"))  # 윈도우 아이콘 설정
        self.resize(256, 256)  # 윈도우 크기 설정
        self.show()  # 윈도우를 화면에 표시

    def activateMessage(self):
        # QMessageBox.information(self, "information", "Button clicked!")
        self.te1.appendPlainText(
            "Button clicked!"
        )  # QPlainTextEdit에 "Button clicked!" 텍스트 추가

    def clearMessage(self):
        self.te1.clear()  # QPlainTextEdit의 텍스트 모두 삭제


if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    view = Calculator()  # Calculator 객체 생성
    sys.exit(app.exec_())  # 어플리케이션 실행 및 이벤트 루프 시작
