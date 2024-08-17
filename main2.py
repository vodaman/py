from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

def clothes():
    if int(in_.text()) < 10:
        message = QMessageBox()
        message.setText("Wear something warm")
    elif int(in_.text()) < 20:
        message = QMessageBox()
        message.setText("Wear something light")
    else:
        message = QMessageBox()
        message.setText("Wear something comfortable")
    message.exec_()

def food():
    if int(in_.text()) < 10:
        message = QMessageBox()
        message.setText("Eat mashed potatoes and drink some hot tea")
    elif int(in_.text()) < 20:
        message = QMessageBox()
        message.setText("Eat a salad and drink some juice")
    else:
        message = QMessageBox()
        message.setText("Eat an ice cream and drink some coke")
    message.exec_()

win = QWidget()
win.setWindowTitle("My App")
win.resize(400, 300)

in_ = QLineEdit()
in_.setPlaceholderText("Enter the weather")
btn1 = QPushButton("Get clothes recommendation")
btn2 = QPushButton("Get food recommendation")

btn1.clicked.connect(clothes)
btn2.clicked.connect(food)

layout = QVBoxLayout()
layout.addWidget(in_)
layout.addWidget(btn1)
layout.addWidget(btn2)

win.setLayout(layout)

win.show()
app.exec_()
