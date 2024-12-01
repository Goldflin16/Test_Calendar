from PyQt5.QtWidgets import(
    QApplication, QMainWindow, QWidget, QPushButton, QCheckBox, QCalendarWidget, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import Qt

app = QApplication([])
window = QWidget()
window.setFixedSize(450, 550)

calendar = QCalendarWidget()
calendar.setGridVisible(True)
calendar.setVerticalHeaderFormat(calendar.VerticalHeaderFormat.NoVerticalHeader)
calendar.setHorizontalHeaderFormat(calendar.HorizontalHeaderFormat.SingleLetterDayNames)
calendar.setNavigationBarVisible(False)
start = QPushButton("Старт")
stop = QPushButton("Стоп")
auto_start = QCheckBox("Автостарт")

video = QVideoWidget()

v_layout = QVBoxLayout()
v_layout.addWidget(start, alignment= Qt.AlignTop)
v_layout.addWidget(stop, alignment= Qt.AlignTop)
v_layout.addWidget(auto_start, alignment= Qt.AlignTop)

h_layout = QHBoxLayout()
h_layout.addWidget(calendar, stretch= 5)
h_layout.addLayout(v_layout, stretch= 2)

main_layout = QVBoxLayout()
main_layout.addLayout(h_layout, stretch= 40)
main_layout.addWidget(video, stretch= 60)



window.setLayout(main_layout)

window.show()
app.exec_()

