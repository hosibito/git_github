class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()

    def connectSignals(self):
        self.view.btn1.clicked.connect(
            self.view.activateMessage
        )  # btn1 클릭 시 activateMessage 메소드 호출
        self.view.btn2.clicked.connect(
            self.view.clearMessage
        )  # btn2 클릭 시 clearMessage 메소드 호출
