from PyQt5.QtWidgets import (QApplication,
                              QMainWindow, 
                              QWidget, QVBoxLayout,QHBoxLayout, QLabel, QSlider)
import sys
from PyQt5.QtCore import Qt # 이벤트 처리할 떄 쓴다
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() # 여기는 왜 괄호를 치는가?

        container = QWidget() # 바탕에 컨테이너를 깔고 
        self.setCentralWidget(container)
        self.label = QLabel("0")
        
        layout = QVBoxLayout()
        container.setLayout(layout)

        self.sliders = []

        for i in range(3):
            self.slider = QSlider()
            self.slider.setRange(0, 180)
            self.slider.setValue(90)   
            self.slider.setOrientation(Qt.Horizontal)
            self.slider.valueChanged.connect(self.update_label) # 값이 바뀌면 함수 호출? 함수 연결?
            layout.addWidget(self.slider)
            self.sliders.append(self.slider)
       
        layout.addWidget(self.label)
         # 윗 부분에 위젯을 만들고, 마지막에 addWidget으로 합쳐준다!

        self.show()
    
    def update_label(self):
        # print(slider.value()) 그냥 이렇게 적으면 값을 못받앙오니까 self.slider로 값을 받아와야함
        slider_values = []
        for slider in self.sliders:
            slider_values.append(slider.value()) # [ ] 
        print(slider_values)    

        slider_values1 = [slider.value() for slider in self.sliders]
        #print(f"compre{slider_values1}")
        self.label.setText(f"{slider_values[0], slider_values[1], slider_values[2]}")

        

app = QApplication(sys.argv)
win = MainWindow()

app.exec()

