from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QMessageBox, QGroupBox, QButtonGroup, QRadioButton#создай приложение для запоминания информации
from random import shuffle, randint

class Question():
    def __init__(self, question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions_list = []
questions_list.append(Question('Государственный язык Бразилии','Португальский','Бразильский','Испанский','Итальянский'))
questions_list.append(Question('Какая марка автомобили Италии?','Феррари','Порше','Мерседес','Форд'))
questions_list.append(Question('Какой праздник отмечают в России 4 ноября?','День Народного Единства','Рождество','Новый год','День рождения Пушкина'))
questions_list.append(Question('Сколько дней в високосном году?','366','364','365','367'))
questions_list.append(Question('Кто провёл больше всех времени на орбите из российских космонавтов?','Падалка','Гагарин','Авдеев','Леонов'))
questions_list.append(Question('Выбери перевод слова ‘переменная’','variable','variation','variant','changing'))
questions_list.append(Question('В каком году была основана Москва?','1147','1242','1861','1943'))
questions_list.append(Question('Какого цвета нет на флаге России','Зелёного','Синего','Красного','Белого'))
'''questions_list.append(Question('','','','',''))'''

app = QApplication([])

window = QWidget()
window.setWindowTitle('Memory Card')
window.resize(700,500)

btn_button = QPushButton('Ответить')
lb_Question = QLabel('В каком году была основана Москва?')

RadioGroupBox = QGroupBox('Варианты ответов')

btn_answer1 = QRadioButton('1147')#расположение виджетов по лэйаутам
btn_answer2 = QRadioButton('1242')
btn_answer3 = QRadioButton('1861')
btn_answer4 = QRadioButton('1943')

RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

layoutH1 = QHBoxLayout()
layoutV2 = QVBoxLayout()
layoutV3 = QVBoxLayout()

layoutV2.addWidget(btn_answer1, alignment = Qt.AlignCenter)
layoutV2.addWidget(btn_answer2, alignment = Qt.AlignCenter)
layoutV3.addWidget(btn_answer3, alignment = Qt.AlignCenter)
layoutV3.addWidget(btn_answer4, alignment = Qt.AlignCenter)

layoutH1.addLayout(layoutV2)
layoutH1.addLayout(layoutV3)

RadioGroupBox.setLayout(layoutH1)

RadioGroupBox2 = QGroupBox('Результаты теста')

lb_Result = QLabel('прав ты или нет')
lb_Correct = QLabel('ответ будет тут')

layoutV2 = QVBoxLayout()

layoutV2.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layoutV2.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch=2)

RadioGroupBox2.setLayout(layoutV2)

layoutH11 = QHBoxLayout()
layoutH22 = QHBoxLayout()
layoutH33 = QHBoxLayout()

layoutH11.addWidget(lb_Question, alignment= (Qt.AlignHCenter | Qt.AlignVCenter))
layoutH22.addWidget(RadioGroupBox)
layoutH22.addWidget(RadioGroupBox2)
RadioGroupBox2.hide()
layoutH33.addStretch(1)
layoutH33.addWidget(btn_button, stretch=2)
layoutH33.addStretch(1)

layout_card = QVBoxLayout()
layout_card.addLayout(layoutH11,stretch=2)
layout_card.addLayout(layoutH22,stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layoutH33,stretch=1)
layout_card.addStretch(1)
layout_card.addStretch(5)

def show_result():
    RadioGroupBox.hide()
    RadioGroupBox2.show()
    btn_button.setText('Следующий вопрос')

def show_question():
    RadioGroupBox2.hide()
    RadioGroupBox.show()
    btn_button.setText('Ответить')

    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
def ask(q: Question):
    '''функция записывает значения вопроса и ответов в соответствующие виджеты, 
    при этом варианты ответов распределяются случайным образом'''
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()

def check_answer():
    '''если выбран какой-то вариант ответа, то надо проверить и показать панель ответов'''
    if answers[0].isChecked():
        show_correct('Правильно!')
        window.score += 1
        print('Статистика\n Всего вопросов:',window.total,'\n Правильных ответов:',window.score)
        print('Рейтинг:',window.score/window.total*100,'%')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно!')
            print('Рейтинг:',window.score/window.total*100,'%')

def next_question():
    window.total += 1
    print('Статистика\n Всего вопросов:',window.total,'\n Правильных ответов:',window.score)
    cur_question = randint(0, len(questions_list) - 1) #переходим к следующему вопросу
    q = questions_list[cur_question] #взяли вопрос
    ask(q) # спросили

def show_correct(res):
    '''показать результат - установим переданный текст в надпись 'результат' и покажем нужную панель'''
    lb_Result.setText(res)
    show_result()


def start_test():
    if btn_button.text() == 'Ответить':
        check_answer()
    else:
        next_question()

window.setLayout(layout_card)

btn_button.clicked.connect(start_test)
window.score = 0
window.total = 0
next_question()

window.show()
app.exec()