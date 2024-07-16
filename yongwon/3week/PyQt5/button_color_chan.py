import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# QApplication 앱을 만들고 실행시키는 역할

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.button_state = False

        self.show()
        button = QPushButton("누름") # 버튼 생성
        button.clicked.connect(self.button_is_clicked)# 함수를 넣어
        self.setCentralWidget(button)

    def button_is_clicked(self):
        self.button_state = not self.button_state


        if self.button_state :
            self.setStyleSheet("background-color : lightblue")
            print("버튼이 눌렸습니다.")
        else:
            self.setStyleSheet("background-color : yellow")

app = QApplication(sys.argv)# 어플리케이션을 계속 돌린다.
win = MainWindow()
app.exec()
