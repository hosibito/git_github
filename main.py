import sys
from PyQt5.QtWidgets import QApplication, QWidget

# PyQt5 모듈에서 QApplication, QWidget을 import


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Calculator")  # 창의 제목 설정
        self.resize(256, 256)  # 창의 크기 설정
        self.show()  # 창을 화면에 표시


if __name__ == "__main__":
    app = QApplication(sys.argv)  # QApplication 객체 생성
    view = Calculator()  # Calculator 클래스의 인스턴스 생성
    sys.exit(app.exec_())  # 어플리케이션 실행 및 이벤트 루프 시작
