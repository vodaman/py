from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])

def calc():
    x = int(in_.text())
    y = int(in_2.text())
    result = x + y
    message = QMessageBox()
    message.setText("The result is " + str(result))
    message.exec_()


win = QWidget()
win.setWindowTitle("My App")
win.resize(400, 300)

in_ = QLineEdit()
in_.setPlaceholderText("Enter X")
in_2 = QLineEdit()
in_2.setPlaceholderText("Enter y")

btn = QPushButton("Calculate X + Y")

btn.clicked.connect(calc)

layout = QVBoxLayout()
layout.addWidget(in_)
layout.addWidget(in_2)
layout.addWidget(btn)

win.setLayout(layout)

win.show()
app.exec_()


