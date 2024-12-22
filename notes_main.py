from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout
 

import json


app = QApplication([])


notes_win = QWidget()
notes_win.setWindowTitle('Умные заметки')
notes_win.resize(900, 600)


list_notes = QListWidget()
lisr_notes_label = QLabel('Список заметок')


addzam = QPushButton("Создать заметку")# кнопка "создать заметку"
delzam = QPushButton("Удалить заметку")#кнопка""удалить заметку"
savezam = QPushButton('Сохранить заметку')# Кнопка сохранить заметку


field_tag = QLineEdit('')
teg.setPlaceholderText('Введите тег...')
field_text = QTextEdit()
addkzam = QPushButton('Добавить к заметке')
otkzam = QPushButton('Открепить от заметки')
foundzam = QPushButton('Найти заметку по тегу')
list_tags = QListWidget()
tegt= QLabel('Список тегов')

layout_notes = QHBoxLayout()
col_1 = QVBoxLayout()
col_1.addWidget(field_text)


col_2 = QVBoxLayout()
col 2. addWidget(list notes label)
col_2. addWidget(list_notes)
row_1 = QHBoxLayout
row 1. addWidget (button note create) 
row_1. addWidget (button_note_del)
row 2 = QHBoxLayout()
row_2. addWidget(button_note_save)
col_2. addLayout (row_1) 
col_2. addlayout (row 2)


col_2. addWidget(list_tags_label)
col_2. addWidget (list_tags)
col 2. addWidget (field tag)
row_3 = QHBoxLayout()
row 3.addWidget(button tag add)
row_3.addWidget(button_tag_del)
row_4 = QHBoxLayout
row 4. addWidget (button tag search)

col_2.addLayout(row_3)
col_2.addLayout(row_4)


ayout notes.addlayout (col_1, stretch = 2)
layout_notes.addLayout (col_2, stretch - 1)
notes_win.setLayout(layout_notes)


def add_note():
    note_name,result = QInputDialog.getText(main_win,'Добавить заметку', 'Название заметки:')
    notes[note_name] ={'текст':'','теги':[]}
    list_notes.addItem(note_name)
    list_tags.addItems(notes[note_name]['теги'])
    print(notes)


def show_note():
    key = list_notes.selectedItems()[0].text()
    field_text.setText(notes[name]['текст'])
    list_tags.clear()
    list_tags.addItems(notes[name]['теги'])


def save_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        notes[key]['текст'] = field_text.toPlainText()
        with open('notes.json','w')as file:
            json.dump(notes,file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print('Заметка для сохранения не выбрана!')


def del note():
    if list_notes.selectedItems ():
        key = list notes.selectedItems)[0].text()
     del notes[key] list_notes.clear ()
        list tags.clear())
        field_text.clear()
        list notes.addItems(notes)
        with open ("notes _data.json", "w") as file:
        json.dump (notes, file, sort_keys=True,)
    print(notes)
else:
    print('Заметка для сохранения не выбрана!')


button_note_create.clicked.connect(add_note)
list_notes.itemClicked.connect(show_note)
button. note_save.clicked.connect(save _note) 
button_note_del.clicked.connect(del_note)button_tag_add.clicked.connect(add_tag)
button_tar. del.clicked.connect(del_tag)
button_tag_search.clicked.connect(search_tag)




notes_win.show()


with open ("notes _data. json", "r") as file:
notes = json. load(file)
list notes. addItems (notes)


app.exec_()