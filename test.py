from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton ,QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from time import sleep

programfile = QApplication([])
window = QWidget()

window.setWindowTitle('Блиц-опрос')
window.resize(700,450)

quest = QLabel('В каком году Украина стала Независимой страной?')

a1 = QRadioButton('В 1992')
a2 = QRadioButton('В 1989')
a3 = QRadioButton('В 1991')
a4 = QRadioButton('В 1994')


q = QVBoxLayout()
q1 = QVBoxLayout()
q2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()


h1.addWidget(quest, alignment = Qt.AlignCenter)
q1.addWidget(a1, alignment = Qt.AlignCenter)
q1.addWidget(a3, alignment = Qt.AlignCenter)
q2.addWidget(a2, alignment = Qt.AlignCenter)
q2.addWidget(a4, alignment = Qt.AlignCenter)
h2.addLayout(q1)
h2.addLayout(q2)
q.addLayout(h1)
q.addLayout(h2)



window.setLayout(q)

#обработка событий
def win():
    quest.setText('Ответ верный!')
    a1.hide()
    a2.hide()
    a3.hide()
    a4.hide()
    

def lose():
    quest.setText('   Ответ неверный.  \nПопробуйте еще раз!')
    a1.hide()
    a2.hide()
    a3.hide()
    a4.hide()
    
    

a3.clicked.connect(win)
a1.clicked.connect(lose)
a2.clicked.connect(lose)
a4.clicked.connect(lose)

# Ответить -> следующий вопрос
# btn.setText('Следущий вопрос')
    
window.show()
programfile.exec_()
