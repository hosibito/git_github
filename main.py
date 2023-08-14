import sys
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QPushButton,
    QVBoxLayout,
    QMessageBox,
    QPlainTextEdit,
)
from PyQt5.QtGui import QIcon


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.te1 = QPlainTextEdit()  # QPlainTextEdit 위젯 생성
        self.te1.setReadOnly(True)  # 편집 불가능하도록 설정

        self.btn1 = QPushButton("Message", self)  # QPushButton 위젯 생성
        self.btn1.clicked.connect(
            self.activateMessage
        )  # 버튼 클릭 시 activateMessage 메소드 호출

        vbox = QVBoxLayout()  # 수직 박스 레이아웃 생성
        vbox.addWidget(self.te1)  # QPlainTextEdit 위젯을 수직 박스 레이아웃에 추가
        vbox.addWidget(self.btn1)  # QPushButton 위젯을 수직 박스 레이아웃에 추가
        vbox.addStretch(1)  # 수직 박스 레이아웃에 공간 추가

        self.setLayout(vbox)  # 수직 박스 레이아웃을 현재 위젯의 레이아웃으로 설정

        self.setWindowTitle("Calculator")  # 창의 제목 설정
        self.setWindowIcon(QIcon("icon.png"))  # 창의 아이콘 설정
        self.resize(256, 256)  # 창의 크기 설정
        self.show()  # 창을 화면에 표시

    def activateMessage(self):
        # QMessageBox.information(self, "information", "Button clicked!")
        self.te1.appendPlainText(
            "Button clicked!"
        )  # QPlainTextEdit에 "Button clicked!" 텍스트 추가


if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    view = Calculator()  # Calculator 객체 생성
    sys.exit(app.exec_())  # 어플리케이션 실행 및 이벤트 루프 시작
