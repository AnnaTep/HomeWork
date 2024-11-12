import tkinter
import os
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialfile="/", title='Выберите файл', filetypes=(('Текстовый файл', '.txt'),
                                                                                             ('Все файлы', '*')))
    text['text'] = text['text'] + '' + filename
    os.startfile(filename)

window = tkinter.Tk()
window.title('Проводник')  # изменеие заголовка
window.geometry('450x150')  # установка размеров окна
window.configure(bg='yellow')
window.resizable(False, False)  # запрет на изменение окна
text = tkinter.Label(window, text='Файл:', height=5, width=65, background='silver',
                     foreground='blue')  # текстовое поле
text.grid(column=1, row=1)
button_select = tkinter.Button(window, width=20, height=3, text='Выберите файл',background='silver',
                               foreground='blue', command=file_select)  # кнопка
button_select.grid(column=1, row=2, pady=5)
window.mainloop()  # обновление окна
