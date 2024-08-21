from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QTableWidget, QListWidget, QListWidgetItem, QLineEdit, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QSpinBox)
from app import app

btn_menu = QPushButton('Menu')
btn_sleep = QPushButton('Take a break')
box_minutes = QSpinBox()
box_minutes.setValue(30)
btn_OK = QPushButton('Answer')
lb_Question = QLabel('')

# make a box for the radio buttons 
radio_group_box = QGroupBox('Variants')
radio_group = QButtonGroup()

# make the radio buttons
rbtn_1 = QRadioButton('')
rbtn_2 = QRadioButton('')
rbtn_3 = QRadioButton('')
rbtn_4 = QRadioButton('')

# add the radio buttons
radio_group.addButton(rbtn_1)
radio_group.addButton(rbtn_2)
radio_group.addButton(rbtn_3)
radio_group.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_1)
layout_ans3.addWidget(rbtn_1)
layout_ans3.addWidget(rbtn_2)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

radio_group_box.setLayout(layout_ans1)

# make a panel with the test result
ans_group_box = QGroupBox('Test result')
lb_Result = QLabel('')
lb_Correct = QLabel('')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=(Qt.AlignLeft | Qt.AlignTop), stretch=2)
ans_group_box.setLayout(layout_res)
ans_group_box.hide()