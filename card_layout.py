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

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QHBoxLayout()

layout_line1.addWidget(btn_menu)
layout_line1.addStretch(1)
layout_line1.addWidget(btn_sleep)
layout_line1.addWidget(box_minutes)
layout_line1.addWidget(QLabel('min'))

layout_line2.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line3.addWidget(radio_group_box)
layout_line3.addWidget(ans_group_box)

layout_line4.addStretch(1)
layout_line4.addWidget(btn_OK, stretch=2)
layout_line4.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layout_line1, stretch=1)
layout_card.addLayout(layout_line2, stretch=2)
layout_card.addLayout(layout_line3, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line4, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)

def show_result():
    radio_group_box.hide()
    ans_group_box.show()
    btn_OK.setText('Next question')

def show_result():
    radio_group_box.show()
    ans_group_box.hide()
    btn_OK.setText('Answer')
    radio_group.setExclusive(False)
    rbtn_2.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    radio_group.setExclusive(True)