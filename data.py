from PyQt5.QtCore import QAbstractListModel, QModelIndex, Qt
from random import randint, shuffle

new_quest_templ = 'New Question'
new_answer_templ = 'New answer'

text_wrong = 'Wrong'
text_correct = 'Correct'

class Question():
    def __init__(self, question = new_quest_templ, answer = new_answer_templ, wrong_answer1 = '', wrong_answer2 = '', wrong_answer3 = ''):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
        self.is_active = True
        self.attempts = 0
        self.correct = 0

    def got_right(self):
        self.attempts += 1
        self.correct += 1
    
    def got_wrong(self):
        self.attempts += 1

class QuestionView():
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.frm_model = frm_model
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

    def change(self, frm_model):
        self.frm_model = frm_model
    
    def show(self):
        self.question.setText(self.frm_model.question)
        self.answer.setText(self.frm_model.answer)
        self.wrong_answer1.setText(self.frm_model.wrong_answer1)
        self.wrong_answer2.setText(self.frm_model.wrong_answer2)
        self.wrong_answer3.setText(self.frm_model.wrong_answer3)

class QuestionEdit(QuestionView):
    def save_question(self):
        self.frm_model.question = self.question.text()
    
    def save_answer(self):
        self.frm_model.answer = self.answer.text()
    
    def save_wrong(self):
        self.frm_model.wrong_answer1 = self.wrong_answer1.text()
        self.frm_model.wrong_answer2 = self.wrong_answer2.text()
        self.frm_model.wrong_answer3 = self.wrong_answer3.text()
    
    def set_connects(self):
        self.question.editing_finished.connect(self.save_question)
        self.answer.editing_finished.connect(self.save_answer)
        self.wrong_answer1.editing_finished.connect(self.save_wrong)
        self.wrong_answer2.editing_finished.connect(self.save_wrong)
        self.wrong_answer3.editing_finished.connect(self.save_wrong)

    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.set_connects()

class AnswerCheck(QuestionView):
    def __init__(self, frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3, showed_answer, result):
        super().__init__(frm_model, question, answer, wrong_answer1, wrong_answer2, wrong_answer3)
        self.showed_answer = showed_answer
        self.result = result

    def check(self):
        if self.answer.isChecked():
            self.result.setText(text_correct)
            self.showed_answer.setText(self.frm_model.answer)
            self.frm_model.got_right()
        else:
            self.result.setText(text_wrong)
            self.showed_answer.setText(self.frm_model.answer)
            self.frm_model.got_wrong()

class QuestionListModel(QAbstractListModel):
    ''' в данных находится список объектов типа Question, 
    а также список активных вопросов, чтобы показывать его на экране '''
    def init(self, parent=None):
        super().init(parent)
        self.form_list = []
    def rowCount(self, index):
        ''' число элементов для показа: обязательный метод для модели, с которой будет связан виджет "список"'''
        return len(self.form_list)
    def data(self, index, role):
        ''' обязательный метод для модели: какие данные она дает по запросу от интерфейса'''
        if role == Qt.DisplayRole:
            # интерфейс хочет нарисовать эту строку, дадим ему текст вопроса для отображения
            form = self.form_list[index.row()]
            return form.question
    def insertRows(self, parent=QModelIndex()):
        ''' этот метод вызывается, чтобы вставить в список объектов новые данные;
        генерируется и вставляется один пустой вопрос.'''
        position = len(self.form_list) # мы вставляем в конец, это нужно сообщить следующей строкой:
        self.beginInsertRows(parent, position, position) # вставка данных должна быть после этого указания и перед endInsertRows()
        self.form_list.append(Question()) # добавили новый вопрос в список данных
        self.endInsertRows() # закончили вставку (теперь можно продолжать работать с моделью)
        QModelIndex()
        return True # сообщаем, что все прошло хорошо
    def removeRows(self, position, parent=QModelIndex()):
        ''' стандартный метод для удаления строк - после удаления из модели строка автоматически удаляется с экрана'''
        self.beginRemoveRows(parent, position, position) # сообщаем, что мы собираемся удалять строку - от position до position 
            # (вообще говоря, стандарт метода removeRows предлагает убирать несколько строк, но мы напишем одну)
        self.form_list.pop(position) # удаляем из списка элемент с номером position
            # в правильной реализации программы удалять вопросы со статистикой нельзя, можно их деактивировать, 
            # но это заметно усложняет модель (надо поддерживать список всех вопросов для статистики 
            # и список активных для отображения в списке редактирования)
        self.endRemoveRows() # закончили удаление (дальше библиотека сама обновляет список на экране)
        return True # все в порядке 
            # (по-хорошему нам может прийти несуществующий position,
            #  правильнее было бы писать try except и возвращать True только в действительно сработавшем случае)
    def random_question(self):
        ''' Выдаёт случайный вопрос '''
        # тут стоит проверять, что вопрос активный...
        total = len(self.form_list)
        current = randint(0, total - 1)
        return self.form_list[current]
    
def random_answerCheck(list_model, w_question, widgets_list, w_showed_answer, w_result):
    frm = list_model.random_question()
    shuffle(widgets_list)
    frm_card = AnswerCheck(frm, w_question, widgets_list[0:3], w_showed_answer, w_result)
    return frm_card