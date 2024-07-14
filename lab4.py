import tkinter as tk
from tkinter import filedialog, messagebox
import main
from Runtime.Language_.language import Language

file_path=""

def is_file_empty(file_path):
    try:
        with open(file_path, 'r') as file:
            return not bool(file.read())
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл не найден")
        return True
    except IOError:
        messagebox.showerror("Ошибка", "Ошибка ввода-вывода при чтении файла")
        return True

def syntax_function():
    global file_path
    if file_path:
        with open(file_path, "r") as file:
            main.prog(file_path)
            content = file.read()
            code_text.delete(1.0, tk.END)
            code_text.insert("1.0", content)

    with open('error_logs.txt', 'w') as file_er:
        file_er.write("")
    file_er.close()
    try:
        (Language.check_syntax(content))
        file_path = 'error_logs.txt'  # Путь к файлу с ошибками
        if is_file_empty(file_path):
            error_text.delete(1.0, tk.END)
            messagebox.showinfo("Информация", "Нет ошибок")
        else:
            try:
                with open(file_path, 'r') as file_er:
                    err_inf = file_er.read()
                    error_text.delete(1.0, tk.END)
                    error_text.insert("1.0", err_inf)
            except FileNotFoundError:
                messagebox.showerror("Ошибка", "Файл с ошибками не найден")
            except IOError:
                messagebox.showerror("Ошибка", "Ошибка ввода-вывода при чтении файла с ошибками")
    except:
        with open('error_logs.txt', 'r') as file_er:
            err_inf = file_er.read()
            error_text.delete(1.0, tk.END)
            error_text.insert("1.0", err_inf)



def file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if file_path:
        code_text.delete(1.0, tk.END)
        with open(file_path, 'r') as file:
            content = file.read()
        code_text.insert("1.0", content)

root = tk.Tk()
root.title("LR4")

tru_button1 = tk.Button(root, text="Файл", command=file)
tru_button1.grid(column=1, row=0, columnspan=2)

tru_button = tk.Button(root, text="Выполнить", command=syntax_function)
tru_button.grid(column=1, row=1, columnspan=2)

code_label = tk.Label(root, text="Код на C#", font=("Arial", 16))
code_label.grid(column=1, row=2)
code_text = tk.Text(root, height=40, width=40)
code_text.grid(column=1,row=3)

error_label = tk.Label(root, text="Ошибки", font=("Arial", 16))
error_label.grid(column=2, row=2)
error_text = tk.Text(root, height=40, width=40)
error_text.grid(column=2,row=3)

root.mainloop()