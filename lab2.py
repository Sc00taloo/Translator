import tkinter as tk
from tkinter import filedialog
import main
from Runtime.Language_.language import Language

file_path=""
def opz_function():
    global file_path
    if file_path:
        with open(file_path, "r") as file:
            main.prog(file_path)
            content = file.read()
            code_text.delete(1.0, tk.END)
            code_text.insert("1.0", content)

    entry = code_text.get("1.0", "end-1c")
    main.prog(entry)
    with open("tokens.txt", "r") as file:
        tokens = file.read()
        lex_text.delete(1.0, tk.END)
        lex_text.insert("1.0", tokens)

    print(content)
    (Language.using_rpn(content))
    with open('opz.txt', 'r') as file:
        opz = file.read()
        opz_text.delete(1.0, tk.END)
        opz_text.insert("1.0", opz)

def file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if file_path:
        code_text.delete(1.0, tk.END)
        with open(file_path, 'r') as file:
            content = file.read()
        code_text.insert("1.0", content)

root = tk.Tk()
root.title("LR2")

tru_button1 = tk.Button(root, text="Файл", command=file)
tru_button1.grid(column=2, row=0)

tru_button = tk.Button(root, text="Выполнить", command=opz_function)
tru_button.grid(column=2, row=1)

code_label = tk.Label(root, text="Код на C#", font=("Arial", 16))
code_label.grid(column=1, row=2)
code_text = tk.Text(root, height=40, width=40)
code_text.grid(column=1,row=3)

lex_label = tk.Label(root, text="Лексемы", font=("Arial", 16))
lex_label.grid(column=2, row=2)
lex_text = tk.Text(root, height=40, width=40)
lex_text.grid(column=2,row=3)

opz_label = tk.Label(root, text="ОПЗ", font=("Arial", 16))
opz_label.grid(column=3, row=2)
opz_text = tk.Text(root, height=40, width=40)
opz_text.grid(column=3,row=3)

root.mainloop()