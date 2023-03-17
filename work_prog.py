import sqlite3
import sys
import pyglet

from datetime import datetime
from PyQt5 import QtGui, QtCore, QtWidgets, QtMultimedia
from PyQt5.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton, QCheckBox, QTableWidget,
                             QRadioButton, QLineEdit, QVBoxLayout, QWizard, QWizardPage, QTableWidgetItem)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

a = []  # Список полученных баллов


class Installer(QWizard):
    def __init__(self, parent=None):
        super(Installer, self).__init__(parent)
        self.addPage(Page1(self))
        self.addPage(Page2(self))
        self.addPage(Page3(self))
        self.addPage(Page4(self))
        self.addPage(Page5(self))
        self.addPage(Page6(self))
        self.addPage(Page7(self))
        self.addPage(Page8(self))
        self.addPage(Page9(self))
        self.addPage(Page10(self))
        self.addPage(Page11(self))
        self.addPage(Page12(self))
        self.addPage(Page13(self))
        self.addPage(Page14(self))
        self.addPage(Page15(self))
        self.addPage(Page16(self))
        self.addPage(Page17(self))
        self.setWindowTitle('Музыкальная викторина')


class Page1(QWizardPage):
    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)

        self.Title = QLabel("Здравствуйте! Заполните данные о себе.")
        self.error = QLabel()  # Сообщение, если введены неверные данные

        self.nameLabel = QLabel("Фамилия Имя:")
        self.nameLineEdit = QLineEdit()

        self.dateLabel = QLabel("Дата рождения:")
        self.dateLineEdit = QLineEdit()

        self.numberLabel = QLabel("Школа:")
        self.numberLineEdit = QLineEdit()

        self.classLabel = QLabel("Класс обучения:")
        self.classLineEdit = QLineEdit()

        self.teachLabel = QLabel("ФИО преподавателя:")
        self.teachLineEdit = QLineEdit()

        self.foto = QLabel()
        pixmap = QPixmap('f3.png')
        pixmap_r = pixmap.scaled(350, 200, Qt.KeepAspectRatio)
        self.foto.setPixmap(pixmap_r)

        self.GO = QPushButton('Зарегистрироваться')
        self.GO.clicked.connect(self.run_1)  # Вызывает функцию, проверяет корректность введённых данных

        layout = QGridLayout()  # Добавление всех эллементов в сетку
        layout.addWidget(self.Title, 0, 0)
        layout.addWidget(self.error, 7, 0)
        layout.addWidget(self.nameLabel, 2, 0)
        layout.addWidget(self.nameLineEdit, 2, 1)
        layout.addWidget(self.dateLabel, 3, 0)
        layout.addWidget(self.dateLineEdit, 3, 1)
        layout.addWidget(self.numberLabel, 4, 0)
        layout.addWidget(self.numberLineEdit, 4, 1)
        layout.addWidget(self.classLabel, 5, 0)
        layout.addWidget(self.classLineEdit, 5, 1)
        layout.addWidget(self.teachLabel, 6, 0)
        layout.addWidget(self.teachLineEdit, 6, 1)
        layout.addWidget(self.foto, 7, 1)
        layout.addWidget(self.GO, 8, 0)

        self.setLayout(layout)

    def run_1(self):
        f = False
        try:
            datetime.strptime(self.dateLineEdit.text(), '%d.%m.%Y')
            if all(x.isalpha() or x.isspace() for x in self.nameLineEdit.text()) and\
               all(x.isalpha() or x.isspace() for x in self.teachLineEdit.text()) and\
               self.classLineEdit.text().isdigit():
                self.error.setText('Нажмите "Next" и приступите к викторине')
                f = True
                print(f)
                
            else:
                self.error.setText('''Ошибка.
Проверьте корректность введённых данных.''')
        except ValueError:
            self.error.setText('''Ошибка.
Проверьте корректность введённых данных.''')
        if f:
            print('ok')
            self.GO.clicked.connect(self.run)  # Вызывает функцию, заполняет БД


    def run(self):
        print(1)
        con = sqlite3.connect('music.db')
        cur = con.cursor()
        k = cur.execute("SELECT COUNT(*) FROM student")
        l_id = k.fetchone()[0]  # Нахождение последнего id
        z = (l_id + 1, self.nameLineEdit.text(), self.dateLineEdit.text(), self.numberLineEdit.text(),
             self.classLineEdit.text(), self.teachLineEdit.text(), 0)
        print(2)
        cur.execute("""INSERT INTO student(id, Name, Birthday, School, Class, Teacher, point)
VALUES(?, ?, ?, ?, ?, ?, ?)""", z)  # Создание новой записи в БД
        print(3)
        con.commit()
        con.close()


class Page2(QWizardPage):  # Вопрос с 1 вариантом ответа
    def __init__(self, parent=None):
        super(Page2, self).__init__(parent)

        self.lab = QLabel('№1')
        self.question = QLabel('Форма полифонической музыки - ...')

        self.otv1 = QRadioButton("сонатная")
        self.otv2 = QRadioButton("фуга")
        self.otv3 = QRadioButton("рондо")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)  # Вызывает функцию, проверяет ответ

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(self.otv1, 2, 0)
        layout.addWidget(self.otv2, 3,0)
        layout.addWidget(self.otv3, 4, 0)
        layout.addWidget(self.GO1, 5, 0)
        self.setLayout(layout)

    def run_1(self):
        if self.otv2.isChecked():
            a.append(1)


class Page3(QWizardPage):  # Вопрос с 1 вариантом ответа
    def __init__(self, parent=None):
        super(Page3, self).__init__(parent)

        self.lab = QLabel('№2')
        self.question = QLabel('Родоначальник классической симфонии')

        self.otv1 = QRadioButton("Г.Ф.Гендель")
        self.otv2 = QRadioButton("И.С.Бах")
        self.otv3 = QRadioButton("Й.Гайдн")

        self.foto = QLabel()
        pixmap = QPixmap('Gendel.jpg')
        pixmap_r = pixmap.scaled(120, 80, Qt.KeepAspectRatio)
        self.foto.setPixmap(pixmap_r)
        
        self.foto1 = QLabel()
        pixmap1 = QPixmap('Bah.jpg')
        pixmap_r1 = pixmap1.scaled(120, 80, Qt.KeepAspectRatio)
        self.foto1.setPixmap(pixmap_r1)
        
        self.foto2 = QLabel()
        pixmap2 = QPixmap('Gaidn.jpg')
        pixmap_r2 = pixmap2.scaled(120, 80, Qt.KeepAspectRatio)
        self.foto2.setPixmap(pixmap_r2)

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(self.otv1, 2, 0)
        layout.addWidget(self.foto, 2, 1)
        layout.addWidget(self.otv2, 3,0)
        layout.addWidget(self.foto1, 3, 1)
        layout.addWidget(self.otv3, 4, 0)
        layout.addWidget(self.foto2, 4, 1)
        layout.addWidget(self.GO1, 5, 0)
        self.setLayout(layout)

    def run_1(self):
        if self.otv3.isChecked():
            a.append(1)


class Page4(QWizardPage):  # Вопрос с 1 вариантом ответа
    def __init__(self, parent=None):
        super(Page4, self).__init__(parent)

        self.lab = QLabel('№3')
        self.question = QLabel('Франц Шуберт - представитель музыкального направления')

        self.otv1 = QRadioButton("Классицизм")
        self.otv2 = QRadioButton("Романтизм")
        self.otv3 = QRadioButton("Импессионизм")

        self.foto = QLabel()
        pixmap = QPixmap('Shybert.jpg')
        pixmap_r = pixmap.scaled(400, 200, Qt.KeepAspectRatio)
        self.foto.setPixmap(pixmap_r)

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(self.foto, 5, 3)
        layout.addWidget(self.otv1, 2, 0)
        layout.addWidget(self.otv2, 3,0)
        layout.addWidget(self.otv3, 4, 0)
        layout.addWidget(self.GO1, 5, 0)
        self.setLayout(layout)

    def run_1(self):
        if self.otv2.isChecked():
            a.append(1)


class Page5(QWizardPage):  # Вопрос с несколькими вариантами ответа
    def __init__(self, parent=None):
        super(Page5, self).__init__(parent)

        self.lab = QLabel('№4')
        self.question = QLabel('Какие из ниже перечисленных танцев являются польскими?')

        self.otv1 = QCheckBox("Вальс") 
        self.otv2 = QCheckBox("Полонез")
        self.otv3 = QCheckBox("Мазурка")
        self.otv4 = QCheckBox("Лендлер")
        self.otv5 = QCheckBox("Краковяк")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)  # Вызывает функцию, проверяет ответ

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(self.otv1, 2, 0)
        layout.addWidget(self.otv2, 3,0)
        layout.addWidget(self.otv3, 4, 0)
        layout.addWidget(self.otv4, 5, 0)
        layout.addWidget(self.otv5, 6, 0)
        layout.addWidget(self.GO1, 7, 0)
        self.setLayout(layout)

    def run_1(self):
        if self.otv2.isChecked() and self.otv3.isChecked() and self.otv5.isChecked():
            a.append(3)
        elif (self.otv2.isChecked() and self.otv3.isChecked()) or\
             (self.otv3.isChecked() and self.otv5.isChecked()) or\
             (self.otv2.isChecked() and self.otv5.isChecked()):
            a.append(2)
        elif self.otv2.isChecked() or self.otv3.isChecked() or self.otv5.isChecked():
            a.append(1)


class Page6(QWizardPage):  # Вопрос с несколькими вариантами ответа
    def __init__(self, parent=None):
        super(Page6, self).__init__(parent)

        self.lab = QLabel('№5')
        self.question = QLabel('Сергей Сергеевич Прокофьев - автор балетов...')

        self.otv1 = QCheckBox("Ромео и Джульетта")
        self.otv2 = QCheckBox("Спящая красавица")
        self.otv3 = QCheckBox("Лебединое озеро")
        self.otv4 = QCheckBox("Золушка")
        self.otv5 = QCheckBox("Сказ о каменном цветке")

        self.foto = QLabel()
        pixmap = QPixmap('Prokofev.jpg')
        pixmap_r = pixmap.scaled(400, 200, Qt.KeepAspectRatio)
        self.foto.setPixmap(pixmap_r)

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)
        
        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(self.otv1, 2, 0)
        layout.addWidget(self.otv2, 3,0)
        layout.addWidget(self.otv3, 4, 0)
        layout.addWidget(self.otv4, 5, 0)
        layout.addWidget(self.otv5, 6, 0)
        layout.addWidget(self.foto, 7, 1)
        layout.addWidget(self.GO1, 7, 0)
        self.setLayout(layout)

    def run_1(self):
        if self.otv1.isChecked() and self.otv4.isChecked() and self.otv5.isChecked():
            a.append(3)
        elif (self.otv1.isChecked() and self.otv4.isChecked()) or\
             (self.otv5.isChecked() and self.otv4.isChecked()) or\
             (self.otv1.isChecked() and self.otv5.isChecked()):
            a.append(2)
        elif self.otv1.isChecked() and self.otv4.isChecked() and self.otv5.isChecked():
            a.append(1)


class Page7(QWizardPage):  # Вопрос с несколькими вариантами ответа
    def __init__(self, parent=None):
        super(Page7, self).__init__(parent)

        self.lab = QLabel('№6')
        self.question = QLabel('Симфонии, I часть которых написана в сонатной форме')

        self.otv1 = QCheckBox("№103 Гайдна")
        self.otv2 = QCheckBox("№40 Моцарта")
        self.otv3 = QCheckBox("№5 Бетховена")
        self.otv4 = QCheckBox("№8 Шуберта")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(self.otv1, 2, 0)
        layout.addWidget(self.otv2, 3,0)
        layout.addWidget(self.otv3, 4, 0)
        layout.addWidget(self.otv4, 5, 0)
        layout.addWidget(self.GO1, 6, 0)
        self.setLayout(layout)

    def run_1(self):
        if self.otv1.isChecked() and self.otv2.isChecked() and self.otv3.isChecked() and self.otv4.isChecked():
            a.append(4)
        elif (self.otv1.isChecked() and self.otv2.isChecked() and self.otv3.isChecked()) or\
             (self.otv1.isChecked() and self.otv2.isChecked() and self.otv4.isChecked()) or\
             (self.otv1.isChecked() and self.otv3.isChecked() and self.otv4.isChecked()) or\
             (self.otv2.isChecked() and self.otv3.isChecked() and self.otv4.isChecked()):
            a.append(3)
        elif (self.otv1.isChecked() and self.otv2.isChecked()) or\
             (self.otv1.isChecked() and self.otv3.isChecked()) or\
             (self.otv1.isChecked() and self.otv4.isChecked()) or\
             (self.otv2.isChecked() and self.otv3.isChecked()) or\
             (self.otv2.isChecked() and self.otv4.isChecked()) or\
             (self.otv3.isChecked() and self.otv4.isChecked()):
            a.append(2)
        elif self.otv1.isChecked() or self.otv2.isChecked() or self.otv3.isChecked() or self.otv4.isChecked():
             a.append(1)


class Page8(QWizardPage):  # Вопрос по изображению
    def __init__(self, parent=None):
        super(Page8, self).__init__(parent)

        self.lab = QLabel('№7')
        self.question = QLabel('Вспомните программные пьесы русских и зарубежных композиторов')

        self.foto = QLabel()  # Добавление изображения
        pixmap = QPixmap('song1.jpg')
        pixmap_r = pixmap.scaled(600, 200, Qt.KeepAspectRatio)
        self.foto.setPixmap(pixmap_r)
        
        self.otv1 = QRadioButton("П.Чайковский Шарманщик поёт из 'Детского альбома'")
        self.otv2 = QRadioButton("М.Мусоргский Избушка на курьих ножках (Баба-Яга) из цикла 'Картинки с выставки'")
        self.otv3 = QRadioButton("П.Чайковский Песня жаворонка из 'Детского альбома'")
        self.otv4 = QRadioButton("Э.Григ Утро из сюиты 'Пер Гюнт'")
        self.otv5 = QRadioButton("Р.Шуман Дед Мороз из 'Альбома для юношества'")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)  # Вызывает функцию, проверяет ответ

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(self.foto, 2, 0)
        layout.addWidget(self.otv1, 3, 0)
        layout.addWidget(self.otv2, 4,0)
        layout.addWidget(self.otv3, 5, 0)
        layout.addWidget(self.otv4, 6, 0)
        layout.addWidget(self.otv5, 7, 0)
        layout.addWidget(self.GO1, 8, 0)
        self.setLayout(layout)

    def run_1(self):
        if self.otv3.isChecked():
            a.append(3)


class Page9(QWizardPage):  # Вопрос по изображению
    def __init__(self, parent=None):
        super(Page9, self).__init__(parent)

        self.lab = QLabel('№8')
        self.question = QLabel('Вспомните программные пьесы русских и зарубежных композиторов')

        self.foto = QLabel()
        pixmap = QPixmap('song2.jpg')
        pixmap_r = pixmap.scaled(600, 200, Qt.KeepAspectRatio)
        self.foto.setPixmap(pixmap_r)
        
        self.otv1 = QRadioButton("П.Чайковский Шарманщик поёт из 'Детского альбома'")
        self.otv2 = QRadioButton("М.Мусоргский Избушка на курьих ножках (Баба-Яга) из цикла 'Картинки с выставки'")
        self.otv3 = QRadioButton("П.Чайковский Песня жаворонка из 'Детского альбома'")
        self.otv4 = QRadioButton("Э.Григ Утро из сюиты 'Пер Гюнт'")
        self.otv5 = QRadioButton("Р.Шуман Дед Мороз из 'Альбома для юношества'")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)
        
        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(self.foto, 2, 0)
        layout.addWidget(self.otv1, 3, 0)
        layout.addWidget(self.otv2, 4,0)
        layout.addWidget(self.otv3, 5, 0)
        layout.addWidget(self.otv4, 6, 0)
        layout.addWidget(self.otv5, 7, 0)
        layout.addWidget(self.GO1, 8, 0)
        self.setLayout(layout)

    def run_1(self):
        if self.otv1.isChecked():
            a.append(3)


class Page10(QWizardPage):  # Вопрос по изображению
    def __init__(self, parent=None):
        super(Page10, self).__init__(parent)

        self.lab = QLabel('№9')
        self.question = QLabel('Вспомните программные пьесы русских и зарубежных композиторов')

        self.foto = QLabel()
        pixmap = QPixmap('song3.jpg')
        pixmap_r = pixmap.scaled(600, 200, Qt.KeepAspectRatio)
        self.foto.setPixmap(pixmap_r)
        
        self.otv1 = QRadioButton("П.Чайковский Шарманщик поёт из 'Детского альбома'")
        self.otv2 = QRadioButton("М.Мусоргский Избушка на курьих ножках (Баба-Яга) из цикла 'Картинки с выставки'")
        self.otv3 = QRadioButton("П.Чайковский Песня жаворонка из 'Детского альбома'")
        self.otv4 = QRadioButton("Э.Григ Утро из сюиты 'Пер Гюнт'")
        self.otv5 = QRadioButton("Р.Шуман Дед Мороз из 'Альбома для юношества'")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(self.foto, 2, 0)
        layout.addWidget(self.otv1, 3, 0)
        layout.addWidget(self.otv2, 4,0)
        layout.addWidget(self.otv3, 5, 0)
        layout.addWidget(self.otv4, 6, 0)
        layout.addWidget(self.otv5, 7, 0)
        layout.addWidget(self.GO1, 8, 0)
        self.setLayout(layout)

    def run_1(self):
        if self.otv2.isChecked():
            a.append(3)


class Page11(QWizardPage):  # Вопрос по изображению
    def __init__(self, parent=None):
        super(Page11, self).__init__(parent)

        self.lab = QLabel('№10')
        self.question = QLabel('Вспомните программные пьесы русских и зарубежных композиторов')

        self.foto = QLabel()
        pixmap = QPixmap('song4.jpg')
        pixmap_r = pixmap.scaled(600, 200, Qt.KeepAspectRatio)
        self.foto.setPixmap(pixmap_r)
        
        self.otv1 = QRadioButton("П.Чайковский Шарманщик поёт из 'Детского альбома'")
        self.otv2 = QRadioButton("М.Мусоргский Избушка на курьих ножках (Баба-Яга) из цикла 'Картинки с выставки'")
        self.otv3 = QRadioButton("П.Чайковский Песня жаворонка из 'Детского альбома'")
        self.otv4 = QRadioButton("Э.Григ Утро из сюиты 'Пер Гюнт'")
        self.otv5 = QRadioButton("Р.Шуман Дед Мороз из 'Альбома для юношества'")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(self.foto, 2, 0)
        layout.addWidget(self.otv1, 3, 0)
        layout.addWidget(self.otv2, 4,0)
        layout.addWidget(self.otv3, 5, 0)
        layout.addWidget(self.otv4, 6, 0)
        layout.addWidget(self.otv5, 7, 0)
        layout.addWidget(self.GO1, 8, 0)
        self.setLayout(layout)

    def run_1(self):
        if self.otv5.isChecked():
            a.append(3)


class Page12(QWizardPage):  # Вопрос по изображению
    def __init__(self, parent=None):
        super(Page12, self).__init__(parent)

        self.lab = QLabel('№11')
        self.question = QLabel('Вспомните программные пьесы русских и зарубежных композиторов')

        self.foto = QLabel()
        pixmap = QPixmap('song5.jpg')
        pixmap_r = pixmap.scaled(600, 200, Qt.KeepAspectRatio)
        self.foto.setPixmap(pixmap_r)
        
        self.otv1 = QRadioButton("П.Чайковский Шарманщик поёт из 'Детского альбома'")
        self.otv2 = QRadioButton("М.Мусоргский Избушка на курьих ножках (Баба-Яга) из цикла 'Картинки с выставки'")
        self.otv3 = QRadioButton("П.Чайковский Песня жаворонка из 'Детского альбома'")
        self.otv4 = QRadioButton("Э.Григ Утро из сюиты 'Пер Гюнт'")
        self.otv5 = QRadioButton("Р.Шуман Дед Мороз из 'Альбома для юношества'")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(self.foto, 2, 0)
        layout.addWidget(self.otv1, 3, 0)
        layout.addWidget(self.otv2, 4,0)
        layout.addWidget(self.otv3, 5, 0)
        layout.addWidget(self.otv4, 6, 0)
        layout.addWidget(self.otv5, 7, 0)
        layout.addWidget(self.GO1, 8, 0)
        self.setLayout(layout)

    def run_1(self):
        if self.otv4.isChecked():
            a.append(3)


class Page13(QWizardPage):  # Вопрос с использованием MP3 файла
    def __init__(self, parent=None):
        super(Page13, self).__init__(parent)

        self.lab = QLabel('№12')
        self.question = QLabel('Нажмите Play, прослушайте фрагмент музыкального\
произведения и выберете правильный ответ.')
       
        self.player = QtMultimedia.QMediaPlayer()
        play_go = QtWidgets.QPushButton('Play', clicked = self.play)  # Воспроизводит MP3 файл
        play_stop = QtWidgets.QPushButton('Stop', clicked = self.stop)  # Останавливает воспроизведение MP3 файла
        
        self.otv1 = QRadioButton("С.С.Прокофьев балет 'Ромео и Джульетта': Танец рыцарей")
        self.otv2 = QRadioButton("Д.Д.Шостакович 'Ленинградская симфония': тема нашествия")
        self.otv3 = QRadioButton("П.И.Чайковский 'Евгений Онегин': ариозо Ленского 1 картина")
        self.otv4 = QRadioButton("К.Дебюсси 'Девушка с волосами цвета льна' прелюдия")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)  # Вызывает функцию, проверяет ответ

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(play_go, 2, 0)
        layout.addWidget(play_stop, 2, 1)
        layout.addWidget(self.otv1, 4, 0)
        layout.addWidget(self.otv2, 5,0)
        layout.addWidget(self.otv3, 6, 0)
        layout.addWidget(self.otv4, 7, 0)
        layout.addWidget(self.GO1, 8, 0)
        self.setLayout(layout)

    def play(self):
        self.song = 'SONG_1.mp3'
        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(self.song)))
        self.player.play()

    def stop(self):
        self.player.stop()

    def run_1(self):
        self.player.stop()  # Останавливает воспроизведение MP3 файла при ответе
        if self.otv3.isChecked():
            a.append(5)


class Page14(QWizardPage):  # Вопрос с использованием MP3 файла
    def __init__(self, parent=None):
        super(Page14, self).__init__(parent)

        self.lab = QLabel('№13')
        self.question = QLabel('Нажмите Play, прослушайте фрагмент музыкального\
произведения и выберете правильный ответ.')
       
        self.player = QtMultimedia.QMediaPlayer()
        play_go = QtWidgets.QPushButton('Play', clicked = self.play)
        play_stop = QtWidgets.QPushButton('Stop', clicked = self.stop)
        
        self.otv1 = QRadioButton("С.С.Прокофьев балет 'Ромео и Джульетта': Танец рыцарей")
        self.otv2 = QRadioButton("Д.Д.Шостакович 'Ленинградская симфония': тема нашествия")
        self.otv3 = QRadioButton("П.И.Чайковский 'Евгений Онегин': ариозо Ленского 1 картина")
        self.otv4 = QRadioButton("К.Дебюсси 'Девушка с волосами цвета льна' прелюдия")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(play_go, 2, 0)
        layout.addWidget(play_stop, 2, 1)
        layout.addWidget(self.otv1, 4, 0)
        layout.addWidget(self.otv2, 5,0)
        layout.addWidget(self.otv3, 6, 0)
        layout.addWidget(self.otv4, 7, 0)
        layout.addWidget(self.GO1, 8, 0)
        self.setLayout(layout)

    def play(self):
        self.song = 'SONG_2.mp3'
        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(self.song)))
        self.player.play()

    def stop(self):
        self.player.stop()

    def run_1(self):
        self.player.stop()
        if self.otv1.isChecked():
            a.append(5)


class Page15(QWizardPage):  # Вопрос с использованием MP3 файла
    def __init__(self, parent=None):
        super(Page15, self).__init__(parent)

        self.lab = QLabel('№14')
        self.question = QLabel('Нажмите Play, прослушайте фрагмент музыкального\
произведения и выберете правильный ответ.')
       
        self.player = QtMultimedia.QMediaPlayer()
        play_go = QtWidgets.QPushButton('Play', clicked = self.play)
        play_stop = QtWidgets.QPushButton('Stop', clicked = self.stop)
        
        self.otv1 = QRadioButton("С.С.Прокофьев балет 'Ромео и Джульетта': Танец рыцарей")
        self.otv2 = QRadioButton("Д.Д.Шостакович 'Ленинградская симфония': тема нашествия")
        self.otv3 = QRadioButton("П.И.Чайковский 'Евгений Онегин': ариозо Ленского 1 картина")
        self.otv4 = QRadioButton("К.Дебюсси 'Девушка с волосами цвета льна' прелюдия")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)
        
        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(play_go, 2, 0)
        layout.addWidget(play_stop, 2, 1)
        layout.addWidget(self.otv1, 4, 0)
        layout.addWidget(self.otv2, 5,0)
        layout.addWidget(self.otv3, 6, 0)
        layout.addWidget(self.otv4, 7, 0)
        layout.addWidget(self.GO1, 8, 0)
        self.setLayout(layout)

    def play(self):
        self.song = 'SONG_3.mp3'
        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(self.song)))
        self.player.play()

    def stop(self):
        self.player.stop()

    def run_1(self):
        self.player.stop()
        if self.otv2.isChecked():
            a.append(5)


class Page16(QWizardPage):  # Вопрос с использованием MP3 файла
    def __init__(self, parent=None):
        super(Page16, self).__init__(parent)

        self.lab = QLabel('№15')
        self.question = QLabel('Нажмите Play, прослушайте фрагмент музыкального\
произведения и выберете правильный ответ.')
       
        self.player = QtMultimedia.QMediaPlayer()
        play_go = QtWidgets.QPushButton('Play', clicked = self.play)
        play_stop = QtWidgets.QPushButton('Stop', clicked = self.stop)
        
        self.otv1 = QRadioButton("С.С.Прокофьев балет 'Ромео и Джульетта': Танец рыцарей")
        self.otv2 = QRadioButton("Д.Д.Шостакович 'Ленинградская симфония': тема нашествия")
        self.otv3 = QRadioButton("П.И.Чайковский 'Евгений Онегин': ариозо Ленского 1 картина")
        self.otv4 = QRadioButton("К.Дебюсси 'Девушка с волосами цвета льна' прелюдия")

        self.GO1 = QPushButton('Ответить')
        self.GO1.clicked.connect(self.run_1)

        layout = QGridLayout()
        layout.addWidget(self.lab, 0, 0)
        layout.addWidget(self.question, 1, 0)
        layout.addWidget(play_go, 2, 0)
        layout.addWidget(play_stop, 2, 1)
        layout.addWidget(self.otv1, 4, 0)
        layout.addWidget(self.otv2, 5,0)
        layout.addWidget(self.otv3, 6, 0)
        layout.addWidget(self.otv4, 7, 0)
        layout.addWidget(self.GO1, 8, 0)
        self.setLayout(layout)

    def play(self):
        self.song = 'SONG_4.mp3'
        self.player.setMedia(QtMultimedia.QMediaContent(QtCore.QUrl(self.song)))
        self.player.play()

    def stop(self):
        self.player.stop()

    def run_1(self):
        self.player.stop()
        if self.otv4.isChecked():
            a.append(5)


class Page17(QWizardPage):
    def __init__(self, parent=None):
        super(Page17, self).__init__(parent)
        self.GO1 = QPushButton('Подвести итоги')
        self.GO1.clicked.connect(self.run)  # Вызывает функцию run() 

        self.result = QLabel()

        self.RATING = QLabel()  # Заголовок "Рейтинг"
        self.rating = QTableWidget()  # Создаю таблицу рейтинга
        
        layout = QGridLayout()
        layout.addWidget(self.GO1, 0, 0)
        layout.addWidget(self.result, 1, 0)
        layout.addWidget(self.RATING, 2, 0)
        layout.addWidget(self.rating, 3, 0)
        self.setLayout(layout)

    def run(self):
        con = sqlite3.connect('music.db')
        cur = con.cursor()
        k = cur.execute("SELECT COUNT(*) FROM student")
        l_id = str(k.fetchone()[0])  # Нахождение последнего id
        name = cur.execute("SELECT Name FROM student WHERE id == ?", l_id).fetchall()
        for elem in name:
            name1 = elem[0]  # Имя учащегося, проходившего тест

        points = 0  # Набранные баллы
        for i in a:
            points += i
        z = (points, l_id)
        cur.execute("UPDATE student SET point = ? WHERE id == ?", z).fetchall()  # Добавление баллов в БД
        
        allList = cur.execute("""SELECT * FROM student""").fetchall()
        allList_sort = sorted(allList, key=lambda x: x[-1], reverse=True)  # Отсортированный по баллам список учащихся

        self.RATING.setText('Рейтинг')
        self.rating.setColumnCount(7)  # Устанавливаю 7 колонок
        self.rating.setRowCount(10)  # и 10 строк в таблице
        self.rating.setHorizontalHeaderLabels(["id участника", "ФИО", "Дата рождения", "Школа",
                                               "Класс", "Учитель", "Баллы"])  # Устанавливаю заголовки таблицы
        
        for i in range(len(allList_sort[:10])):  # Заполняю рейтинговую таблицу
            for j in range(7):
                self.rating.setItem(i, j, QTableWidgetItem(str(allList_sort[i][j])))
        self.rating.resizeColumnsToContents()

        self.result.setText(f'{name1}      Набранных баллов: {points}')  # Вывожу ФИ учащегося и набранные баллы
        print(f'{name1}      Набранных баллов: {points}')
        con.commit()
        con.close()
        

app = QApplication(sys.argv)
window = Installer()
window.show()
sys.exit(app.exec_())
