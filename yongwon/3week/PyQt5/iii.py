from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QWidget,QVBoxLayout
import sys
import random

candidates = ["김무현", "김동희", "조권희", "심승환","김민우"]

class MainWindow(QMainWindow):
    def __init__(self):  
        super().__init__()
        self.button1_state = False
        self.button2_state = False

        self.setWindowTitle("Kairos")

        container = QWidget()
        self.setCentralWidget(container)

        h_layout = QHBoxLayout()

        v_layout = QVBoxLayout()    
        container.setLayout(h_layout)      

        
        button1 = QPushButton("반장")
        button1.clicked.connect(self.button1_is_clicked)

        button2 = QPushButton("부반장")
        button2.clicked.connect(self.button2_is_clicked)

        h_layout.addWidget(button1)
        h_layout.addWidget(button2)
        

        self.show()

    def button1_is_clicked(self):
        x= random.choice(candidates)
        print(f"반장은 {x}입니다! 축하해요!")  


    def button2_is_clicked(self):
        x= random.choice(candidates)
        print(f"부반장은 {x}입니다! 축하해요!")  

app = QApplication(sys.argv)
win = MainWindow() 
app.exec()
