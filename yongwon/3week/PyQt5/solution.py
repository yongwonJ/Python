from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QSlider
import sys
from PyQt5.QtCore import Qt

# 숙지 필요
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 
        self.setWindowTitle("Robot Arm Controller")
        container = QWidget()
        # 예시코드 주어질 예정
        self.setCentralWidget(container)
        # 숙지 필요
        v_layout = QVBoxLayout()
        # 예시코드 주어질 예정
        container.setLayout(v_layout)
        # 숙지 필요
        self.label = QLabel('0,0,0')
        v_layout.addWidget(self.label)
        self.sliders=[]
        
        for i in range(3):
        # 함수 불러오는 코드 빼고 예시코드 주어질 예정
            self.slider = QSlider()
            self.slider.setRange(0, 180)
            # 숙지 필요
            self.slider.setValue(90)   
            # 예시코드 주어질 예정
            self.slider.setOrientation(Qt.Horizontal)
            self.slider.valueChanged.connect(self.update_label)
		        # 숙지 필요
            v_layout.addWidget(self.slider)
            self.sliders.append(self.slider)

        self.show()

		# 숙지 필요
    def update_label(self):
        # 아래 comprehension 코드와 동일한 코드
        #slider_values=[]
        #for slider in self.sliders:
        #    self.slider_values.append(slider.value())
        slider_values=[slider.value() for slider in self.sliders]
        print(slider_values[0],slider_values[1],slider_values[2])
        self.label.setText(f'slider1 : {slider_values[0]}, slider2 : {slider_values[1]}, slider3 : {slider_values[2]}')

# 숙지 필요
app = QApplication(sys.argv)
win = MainWindow()
app.exec()