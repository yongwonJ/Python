import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QCheckBox, QComboBox, QDateEdit, QDateTimeEdit, QDial, QDoubleSpinBox, QSlider, QLineEdit

class WidgetDemo(QWidget):
    def __init__(self):
        super().__init__()

        # Create layout
        layout = QVBoxLayout()

        # Add QCheckBox
        checkbox = QCheckBox("Check me")
        checkbox.setChecked(True)  # Set checkbox to checked
        checked = checkbox.isChecked()  # Check if checkbox is checked
        checkbox.toggle()  # Toggle the checkbox state
        layout.addWidget(checkbox)

        # Add QComboBox
        combo_box1 = QComboBox()
        layout.addWidget(combo_box1)

        # Add QDateEdit
        date_edit = QDateEdit()
        layout.addWidget(date_edit)

        # Add QDateTimeEdit
        datetime_edit = QDateTimeEdit()
        layout.addWidget(datetime_edit)

        # Add QDial
        dial = QDial()
        layout.addWidget(dial)

        # Add QDoubleSpinBox
        double_spin_box = QDoubleSpinBox()
        layout.addWidget(double_spin_box)

        # Add another QComboBox
        combo_box2 = QComboBox()
        combo_box2.addItem("Option 1")
        combo_box2.addItem("Option 2")
        layout.addWidget(combo_box2)

        # Add a QSlider
        slider = QSlider()
        layout.addWidget(slider)

        # Add two QLineEdit
        line_edit1 = QLineEdit()
        layout.addWidget(line_edit1)

        line_edit2 = QLineEdit()
        layout.addWidget(line_edit2)

        # Add a final QSlider
        final_slider = QSlider()
        layout.addWidget(final_slider)

        # Add a QDoubleSpinBox at the bottom
        double_spin_box_bottom = QDoubleSpinBox()
        layout.addWidget(double_spin_box_bottom)

        # Set layout
        self.setLayout(layout)
        self.setWindowTitle("Widgets Demo")

        def checkbox_state_changed(self, state):
            if state == 2:  # Checked state
                print(1)
                
                
# Main function
if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = WidgetDemo()
    demo.show()
    sys.exit(app.exec_())
