import sys
from ui import View
from ctrl import Control
from PyQt5.QtWidgets import QApplication


def main():
    # QApplication 객체 생성
    calc = QApplication(sys.argv)
    app = QApplication(sys.argv)

    # View 객체 생성
    view = View()

    # Control 객체 생성하면서 View 객체 전달
    Control(view=view)

    # 어플리케이션 실행
    sys.exit(app.exec_())


if __name__ == "__main__":
    # main 함수 호출
    main()
