from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget
from app import app

# consts
MAIN_WIDTH, MAIN_HEIGHT = 1000, 450
CARD_WIFTH, CARD_HEIGHT = 600, 500
TIME_UNIT = 1000

# globals
questions_listmodel = QuestionListModel() # type: ignore
frm_edit = QuestionEdit(0, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3) # type: ignore
frm_card = 0
timer = QTimer()
win_card = QWidget()
win_main = QWidget()

# test data

def testlist():
    frm = Question("a", "b", "c", "d")
    questions_listmodel.form_list.append(frm)
    frm = Question("a", "b", "c", "d")
    questions_listmodel.form_list.append(frm)
    frm = Question("a", "b", "c", "d")
    questions_listmodel.form_list.append(frm)
    frm = Question("a", "b", "c", "d")
    questions_listmodel.form_list.append(frm)