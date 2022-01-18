import tkinter as tk


class MainApp(tk.Frame):
    def __init__(self, root):
        super(MainApp, self).__init__(root)
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

        button.pack(side=tk.LEFT)

    def open_dialogw(self):
        ChildWindow()


class ChildWindow(tk.Toplevel):
    def __init__(self):
        super(ChildWindow, self).__init__(root)
        self.installing()

    def installing(self):
        self.title("Добавить доходы/расходы")
        self.geometry("400x220+400+300")
        self.resizable(False, False)

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
