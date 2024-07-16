from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QPushButton, QWidget
import sys

class MainWindow(QMainWindow):
    def __init__(self):  
        super().__init__()

        self.setWindowTitle("Kairos")

        container = QWidget()
        self.setCentralWidget(container)

        h_layout = QHBoxLayout()  
        container.setLayout(h_layout)      
        self.buttons = ["A", "B", "C", "D"]
        self.button_colors = {"A": "red", "B": "green", "C": "blue", "D": "yellow"}
        self.button_list = []

        for button_text in self.buttons:
            button = QPushButton(button_text)
            button.clicked.connect(self.button_is_clicked)
            self.button_list.append(button)
            h_layout.addWidget(button)
        
        self.show()

    def button_is_clicked(self):
        clicked_button = self.sender()
        button_text = clicked_button.text()
        color = self.button_colors[button_text]
        clicked_button.setStyleSheet(f"background-color: {color};")

app = QApplication(sys.argv)
win = MainWindow() 
app.exec()