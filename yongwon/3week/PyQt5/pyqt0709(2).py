from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,QHBoxLayout, QLabel, QSlider
import sys
from PyQt5.QtCore import Qt # 이벤트 처리할 떄 쓴다
# 하지만 여기선 슬라이더를 회전시키는 용도

#윈도우 클래스
class MainWindow(QMainwindow):
    def __init__(self):
        super().__init()
        #윈도우에 직접 슬라이더를 만들게 아니니까 위젯을 담을 컨테이너를 만든다
        container = QWidget()
        self.setCentralWidget(container)
        self.label = QLabel("0")
        layout = QVBoxLayout()
        container.setLayout(layout)

        self.sliders = []
        for i in range(3):
            self.slider = QSlider()
            self.slider.setRange(0,180)
            self.slider.setValue(90)
            self.slider.setOrientation(Qt.Horizontal)
            self.slider.valueChanged.connect(self.update_label)
            layout.addWidget(self.slider)
            self.sliders.append(self.slider)
        
        layout.addWidget(self.label)
        self.show()

    def update_label(self):
        slider_value = []
        for slider in self.sliders:
            slider_values.append(slider.value())
        print(slider_values)

        self.label.setText(f"~~~~")
        


