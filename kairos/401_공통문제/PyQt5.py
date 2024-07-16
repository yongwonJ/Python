from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSlider
import sys
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        container = QWidget()
        self.setCentralWidget(container)
        v_layout = QVBoxLayout()
        container.setLayout(v_layout)
        self.label = QLabel("0,0,0")
        v_layout.addWidget(self.label)

        self.sliders = []
        for i in range(3):
            self.slider = QSlider()
            self.slider.setRange(0, 180)
            self.slider.value(90)                  
            self.slider.setOrientation(Qt.Horizontal)
            self.slider.valueChanged.connect(self.update_label)
            v_layout.addWidget(self.slider)
            self.sliders.append(self.slider.value)

    def update_label(self):
        for slider in self.sliders :
            slider_values = [slider for slider in self.sliders] 

            # slider_values = []
            # for slider in self.slider :
            #     slider_values.append(slider)

            self.label.setText(f"{slider_values[0]}, {slider_values[1]}, {slider_values[2]}") 

app = QApplication()
win = MainWindow
app.exec()


        

