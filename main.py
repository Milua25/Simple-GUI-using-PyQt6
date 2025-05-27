import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox, QMainWindow, \
    QMessageBox


class SpeedCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        self.drop_down_value = "Metric (km)"

        grid = QGridLayout()

        # Create Widgets
        distance_label = QLabel("Distance:")
        self.distance_label_edit = QLineEdit()

        time_label = QLabel("Time(hours):")
        self.time_label_edit = QLineEdit()

        drop_down = QComboBox()
        drop_down.addItems(["Metric (km)", "Imperial (miles)"])

        # Sends the current index (position) of the selected item.
        drop_down.currentIndexChanged.connect(self.index_changed)

        # There is an alternate signal to send the text.
        drop_down.currentTextChanged.connect(self.text_changed)

        # Button
        calculate_button = QPushButton("Calculate")
        calculate_button.setCheckable(True)
        calculate_button.clicked.connect(self.calculate_speed)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_label_edit, 0, 1)
        grid.addWidget(drop_down, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_label_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 3)
        grid.addWidget(self.output_label, 3, 0, 1, 3)

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

    def index_changed(self, i):  # i is an int
        return i

    def text_changed(self, s):
        self.drop_down_value = s  # s is a str

    def calculate_speed(self):
        unit = self.drop_down_value
        try:
            distance = int(self.distance_label_edit.text())
            time = int(self.time_label_edit.text())
            avr_speed = distance / time
            if unit == "Metric (km)":
                avr_speed = round(avr_speed, 2)
                unit_ab = "km/h"
            else:
                avr_speed = round(avr_speed * 0.621371, 2)
                unit_ab = "mph"
        except ValueError:
            QMessageBox.warning(self, "Warning", "Please enter a number.")
        except ZeroDivisionError:
            QMessageBox.warning(self, "Warning", "Distance cannot be divided by zero.")
        else:
            self.output_label.setText(f"Average Speed: {avr_speed}{unit_ab}")


# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works to
app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
