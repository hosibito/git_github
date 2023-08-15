class Control:
    def __init__(self, view):
        self.view = view
        self.connectSignals()  # view와의 신호 연결을 수행하는 메서드 호출

    def calculate(self):
        pass  # 계산을 수행하는 메서드

    def connectSignals(self):
        self.view.btn1.clicked.connect(self.calculate)  # btn1 버튼 클릭 시 calculate 메서드와 연결
        self.view.btn2.clicked.connect(
            self.view.clearMessage
        )  # btn2 버튼 클릭 시 view의 clearMessage 메서드와 연결
