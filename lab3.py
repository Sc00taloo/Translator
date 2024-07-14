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

    print(content)
    (Language.get_python_code(content))
    with open('py_code.py', 'r') as file:
        py_code = file.read()
        python_text.delete(1.0, tk.END)
        python_text.insert("1.0", py_code)

def file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if file_path:
        code_text.delete(1.0, tk.END)
        with open(file_path, 'r') as file:
            content = file.read()
        code_text.insert("1.0", content)

root = tk.Tk()
root.title("LR3")

tru_button1 = tk.Button(root, text="Файл", command=file)
tru_button1.grid(column=1, row=0, columnspan=2)

tru_button = tk.Button(root, text="Выполнить", command=opz_function)
tru_button.grid(column=1, row=1, columnspan=2)

code_label = tk.Label(root, text="Код на C#", font=("Arial", 16))
code_label.grid(column=1, row=2)
code_text = tk.Text(root, height=40, width=40)
code_text.grid(column=1,row=3)

python_label = tk.Label(root, text="Код на Python", font=("Arial", 16))
python_label.grid(column=2, row=2)
python_text = tk.Text(root, height=40, width=40)
python_text.grid(column=2,row=3)

root.mainloop()
