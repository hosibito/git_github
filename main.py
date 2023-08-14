import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn1 = QPushButton("Message", self)  # "Message"라는 텍스트를 가진 버튼 생성
        self.btn1.clicked.connect(
            self.activateMessage
        )  # 버튼 클릭 시 activateMessage 메소드 실행

        vbox = QVBoxLayout()  # 수직 박스 레이아웃 생성
        vbox.addStretch(1)  # 레이아웃에 공백 추가
        vbox.addWidget(self.btn1)  # 레이아웃에 버튼 추가
        vbox.addStretch(1)  # 레이아웃에 공백 추가

        self.setLayout(vbox)  # 위젯의 레이아웃을 vbox로 설정

        self.setWindowTitle("Calculator")  # 창의 제목 설정
        self.setWindowIcon(QIcon("icon.png"))  # 창의 아이콘 설정
        self.resize(256, 256)  # 창의 크기 설정
        self.show()  # 창을 화면에 표시

    def activateMessage(self):
        QMessageBox.information(
            self, "information", "Button clicked!"
        )  # 메시지 박스를 표시하는 메소드


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 어플리케이션 객체 생성
    view = Calculator()  # Calculator 클래스의 인스턴스 생성
    sys.exit(app.exec_())  # 어플리케이션 실행 및 이벤트 루프 시작
