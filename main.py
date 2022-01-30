import tkinter as tk  # old modules
from tkinter import ttk  # new modules


class MainApp(tk.Frame):
    """Главное окно для вызова дочерних"""
    def __init__(self, root):
        super(MainApp, self).__init__(root)
        self.three = ttk.Treeview(self, columns=(
            'id',
            'description',
            'costs',
            'total'
        ), height=15, show='headings')
        self.add_img = tk.PhotoImage(file='add.gif')
        self.installing()

    def installing(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        button = tk.Button(
            toolbar,
            text='Добавить что либо',
            command=self.open_dialogw,
            bg='#d7d8e0',
            bd=0,
            compound=tk.TOP,
            image=self.add_img
        )

        button.pack(side=tk.LEFT)  # Создаёт картинку с кнопкой

        self.three.column('id', width=30, anchor=tk.CENTER)
        self.three.column('description', width=365, anchor=tk.CENTER)
        self.three.column('costs', width=150, anchor=tk.CENTER)
        self.three.column('total', width=110, anchor=tk.CENTER)

        self.three.heading('id', text='#')
        self.three.heading('description', text='Описание')
        self.three.heading('costs', text='Статья дохода/расхода')
        self.three.heading('total', text='Итог')

        self.three.pack()

    def open_dialogw(self):
        ChildWindow()


class ChildWindow(tk.Toplevel):
    """Дочерние окно для вызова доходов/расходов"""
    def __init__(self):
        super(ChildWindow, self).__init__(root)
        self.entry_description = ttk.Entry(self)
        self.entry_money = ttk.Entry(self)
        self.combobox = ttk.Combobox(self, values=[u'Доход', u'Расход'])
        self.installing()

    def installing(self):
        self.title("Добавить доходы/расходы")
        self.geometry("400x220+400+300")
        self.resizable(False, False)

        label_description = tk.Label(self, text="Наименование")
        label_description.place(x=50, y=50)
        label_select = tk.Label(self, text="Статья дохода/расхода")
        label_select.place(x=50, y=80)
        label_amount = tk.Label(self, text="Сумма")
        label_amount.place(x=50, y=110)

        self.entry_description.place(x=200, y=50)
        self.entry_money.place(x=200, y=110)

        self.combobox.current(0)
        self.combobox.place(x=200, y=80)

        btn_cancel = ttk.Button(self, text="Закрыть", command=self.destroy)  # Закрытие окна
        btn_cancel.place(x=300, y=170)

        btn_save = ttk.Button(self, text="Добавить")
        btn_save.place(x=220, y=170)
        btn_save.bind('<Button-1>')

        self.grab_set()
        self.focus_set()


if __name__ == '__main__':
    root = tk.Tk()
    app = MainApp(root=root)
    app.pack()

    root.title("Тестирование")
    root.geometry("650x450+300+200")
    root.resizable(False, False)
    root.mainloop()
