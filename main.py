from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget
from app import app

# consts
MAIN_WIDTH, MAIN_HEIGHT = 1000, 450
CARD_WIDTH, CARD_HEIGHT = 600, 500
TIME_UNIT = 1000

# globals
# questions_listmodel = QuestionListModel()
frm_edit = QuestionEdit(0, txt_Question, txt_Answer, txt_Wrong1, txt_Wrong2, txt_Wrong3)
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

def set_card():
    win_card.resize(CARD_WIDTH, CARD_HEIGHT)
    win_card.move(300, 300)
    win_card.setWindowTitle('supa dupa test')
    win_card.setLayout(layout_card)

def sleep_card():
    win_card.hide()
    timer.setInterval(TIME_UNIT * box_Minutes.value())
    timer.start()

def show_card():
    win_card.show()
    timer.stop()

def show_random():
    global frm_card
    frm_card = random_answerCheck(questions_listmodel, lb_question, radio_list, lb_correct, lb_result)
    frm_card.show()
    show_question()

def click_OK():
    if btn_OK.text() != 'Next question':
        frm_card.check()
        show_result()
    else:
        show_random()