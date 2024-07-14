import json
import tkinter as tk
from tkinter import filedialog

words = ['int', 'double', 'float', 'void', 'static', 'if', 'else if', 'else', 'return', 'for', 'in', 'using',
         'namespace', 'class', 'Write', 'WriteLine', 'Console', 'Main', 'break', 'byte', 'case', 'catch', 'switch',
         'try', 'while', 'finally']
operations = ['+', '*', '-', '/', '<', '>', '=', '!=', '%', '**', '++', '+=', '--', '-=', '<=', '==', '>=', '&&', '||']
separators = [' ', ',', ';', '(', ')', '[', ']', '{', '}', '.', '\n']

def check_token(tokens, token_class, token_value):
    if not (token_value in tokens[token_class]):
        token_code = str(len(tokens[token_class]) + 1)
        tokens[token_class][token_value] = token_class + token_code

def get_operation(input_sequence, i):
    for k in range(3, 0, -1):
        if i + k < len(input_sequence):
            buffer = input_sequence[i:i + k]
            if buffer in operations:
                return buffer
    return ''

def get_separator(input_sequence, i):
    buffer = input_sequence[i]
    if buffer in separators:
        return buffer
    return ''

def prog(text):
    #Лексемы
    tokens = {'W': {}, 'I': {}, 'O': {}, 'R': {}, 'N': {}, 'C': {}}
    for service_word in words:
        check_token(tokens, 'W', service_word)
    for operation in operations:
        check_token(tokens, 'O', operation)
    for separator in separators:
        check_token(tokens, 'R', separator)

    #f = open('test.txt', 'r')
    input_sequence = text
    #f.close()

    i = 0
    state = 'S'
    output_sequence = buffer = ''
    while i < len(input_sequence):
        symbol = input_sequence[i]
        operation = get_operation(input_sequence, i)
        separator = get_separator(input_sequence, i)
        if state == 'S':
            buffer = ''
            if symbol.isalpha():
                state = 'p1'
            elif symbol.isdigit():
                state = 'p3'
            elif symbol == "'":
                state = 'p9'
            elif symbol == '/':
                state = 'p10'
            elif symbol == '"':
                state = 'p14'
            elif operation:
                check_token(tokens, 'O', operation)
                output_sequence += tokens['O'][operation] + ' '
                i += len(operation) - 1
            elif separator:
                if separator != ' ':
                    check_token(tokens, 'R', separator)
                    output_sequence += tokens['R'][separator]
                    if separator == '\n':
                        output_sequence += '\n'
                    else:
                        output_sequence += ' '
            elif i == len(input_sequence) - 1:
                state = 'Z'
        if state == 'p1':
            if symbol.isalpha():
                buffer += symbol
            elif symbol.isdigit():
                state = 'p2'
                buffer += symbol
            else:
                if operation or separator:
                    if buffer in words:
                        output_sequence += tokens['W'][buffer] + ' '
                    elif buffer in operations:
                        output_sequence += tokens['O'][buffer] + ' '
                    else:
                        check_token(tokens, 'I', buffer)
                        output_sequence += tokens['I'][buffer] + ' '
                    if operation:
                        check_token(tokens, 'O', operation)
                        output_sequence += tokens['O'][operation] + ' '
                        i += len(operation) - 1
                    if separator:
                        if separator != ' ':
                            check_token(tokens, 'R', separator)
                            output_sequence += tokens['R'][separator]
                            if separator == '\n':
                                output_sequence += '\n'
                            else:
                                output_sequence += ' '
                state = 'S'
        elif state == 'p2':
            if symbol.isalnum():
                buffer += symbol
            else:
                if operation or separator:
                    check_token(tokens, 'I', buffer)
                    output_sequence += tokens['I'][buffer] + ' '
                    if operation:
                        check_token(tokens, 'O', operation)
                        output_sequence += tokens['O'][operation] + ' '
                        i += len(operation) - 1
                    if separator:
                        if separator != ' ':
                            check_token(tokens, 'R', separator)
                            output_sequence += tokens['R'][separator]
                            if separator == '\n':
                                output_sequence += '\n'
                            else:
                                output_sequence += ' '
                    state = 'S'
        elif state == 'p3':
            if symbol.isdigit():
                buffer += symbol
            elif symbol == '.':
                state = 'p4'
                buffer += symbol
            elif symbol == 'e' or symbol == 'E':
                state = 'p6'
                buffer += symbol
            else:
                if operation or separator:
                    check_token(tokens, 'N', buffer)
                    output_sequence += tokens['N'][buffer] + ' '
                    if operation:
                        check_token(tokens, 'O', operation)
                        output_sequence += tokens['O'][operation] + ' '
                        i += len(operation) - 1
                    if separator:
                        if separator != ' ':
                            check_token(tokens, 'R', separator)
                            output_sequence += tokens['R'][separator]
                            if separator == '\n':
                                output_sequence += '\n'
                            else:
                                output_sequence += ' '
                    state = 'S'
        elif state == 'p4':
            if symbol.isdigit():
                state = 'p5'
                buffer += symbol
        elif state == 'p5':
            if symbol.isdigit():
                buffer += symbol
            elif symbol == 'e' or symbol == 'E':
                state = 'p6'
                buffer += symbol
            else:
                if operation or separator:
                    check_token(tokens, 'N', buffer)
                    output_sequence += tokens['N'][buffer] + ' '
                    if operation:
                        check_token(tokens, 'O', operation)
                        output_sequence += tokens['O'][operation] + ' '
                        i += len(operation) - 1
                    if separator:
                        if separator != ' ':
                            check_token(tokens, 'R', separator)
                            output_sequence += tokens['R'][separator]
                            if separator == '\n':
                                output_sequence += '\n'
                            else:
                                output_sequence += ' '
                    state = 'S'
        elif state == 'p6':
            if symbol == '-' or symbol == '+':
                state = 'p7'
                buffer += symbol
            elif symbol.isdigit():
                state = 'p8'
                buffer += symbol
        elif state == 'p7':
            if symbol.isdigit():
                state = 'p8'
                buffer += symbol
        elif state == 'p8':
            if symbol.isdigit():
                buffer += symbol
            else:
                if operation or separator:
                    check_token(tokens, 'N', buffer)
                    output_sequence += tokens['N'][buffer] + ' '
                    if operation:
                        check_token(tokens, 'O', operation)
                        output_sequence += tokens['O'][operation] + ' '
                        i += len(operation) - 1
                    if separator:
                        if separator != ' ':
                            check_token(tokens, 'R', separator)
                            output_sequence += tokens['R'][separator]
                            if separator == '\n':
                                output_sequence += '\n'
                            else:
                                output_sequence += ' '
                state = 'S'
        elif state == 'p9':
            buffer += symbol
            state = 'p12'
        elif state == 'p10':
            if symbol == '/':
                state = 'p11'
        elif state == 'p11':
            if symbol == '\n':
                state = 'S'
            elif i == len(input_sequence) - 1:
                state = 'Z'
        elif state == 'p12':
            if symbol == "'":
                buffer += symbol
                check_token(tokens, 'C', buffer)
                output_sequence += tokens['C'][buffer] + ' '
                state = 'S'
            else:
                buffer += symbol
                state = 'p12'
        elif state == 'p13':
            if symbol == '\n':
                state = 'S'
            elif i == len(input_sequence) - 1:
                state = 'Z'
        elif state == 'p14':
            buffer += symbol
            state = 'p15'
        elif state == 'p15':
            if symbol == '"':
                buffer += symbol
                check_token(tokens, 'C', buffer)
                output_sequence += tokens['C'][buffer] + ' '
                state = 'S'
            else:
                buffer += symbol
                state = 'p15'
        i += 1

    f = open('tokens.txt', 'w')
    f.write(output_sequence)
    f.close()

    for token_class in tokens.keys():
        with open('%s.json' % token_class, 'w') as file:
            json.dump({}, file)

    #файлы, содержащие все таблицы лексем
    for token_class in tokens.keys():
        with open('%s.json' % token_class, 'w', encoding='utf-8') as write_file:
            data = {val: key for key, val in tokens[token_class].items()}
            json.dump(data, write_file, indent=4, ensure_ascii=False)

def file():
    file_path = filedialog.askopenfilename(filetypes=[('Text files', '*.txt')])
    if file_path:
        code_text.delete(1.0, tk.END)
        with open(file_path, 'r') as file:
            content = file.read()
        code_text.insert("1.0", content)
def button_click():
    token_text.configure(state="normal")
    W_text.configure(state="normal")
    R_text.configure(state="normal")
    O_text.configure(state="normal")
    N_text.configure(state="normal")
    I_text.configure(state="normal")
    C_text.configure(state="normal")
    token_text.delete(1.0, tk.END)
    W_text.delete(1.0, tk.END)
    R_text.delete(1.0, tk.END)
    O_text.delete(1.0, tk.END)
    N_text.delete(1.0, tk.END)
    I_text.delete(1.0, tk.END)
    C_text.delete(1.0, tk.END)
    entry = code_text.get("1.0", "end-1c")

    if entry == '':
        pass
    else:
        prog(entry)
        f4 = open('tokens.txt', 'r')
        text = f4.read()
        token_text.insert("1.0", text)
        token_text.configure(state='disabled')
        f4.close()

        fW = open('W.json', 'r')
        text = fW.read()
        text = text.replace("    ", "")
        text = text.replace('"', "")
        text = text.replace(',', "")
        text = text.replace("\\", "")
        text = text[2:-1]
        W_text.insert("1.0", text)
        W_text.configure(state='disabled')
        fW.close()

        fR = open('R.json', 'r')
        text = fR.read()
        text = text.replace("    ", "")
        text = text.replace('"', "")
        text = text.replace(',', "")
        text = text.replace("\\", "")
        text = text[2:-1]
        R_text.insert("1.0", text)
        R_text.configure(state='disabled')
        fR.close()

        fO = open('O.json', 'r')
        text = fO.read()
        text = text.replace("    ", "")
        text = text.replace('"', "")
        text = text.replace(',', "")
        text = text.replace("\\", "")
        text = text[2:-1]
        O_text.insert("1.0", text)
        O_text.configure(state='disabled')
        fO.close()

        fN = open('N.json', 'r')
        text = fN.read()
        text = text.replace("    ", "")
        text = text.replace('"', "")
        text = text.replace(',', "")
        text = text.replace("\\", "")
        text = text[2:-1]
        N_text.insert("1.0", text)
        N_text.configure(state='disabled')
        fN.close()

        fI = open('I.json', 'r')
        text = fI.read()
        text = text.replace("    ", "")
        text = text.replace('"', "")
        text = text.replace(',', "")
        text = text.replace("\\", "")
        text = text[2:-1]
        I_text.insert("1.0", text)
        I_text.configure(state='disabled')
        fI.close()

        fC = open('C.json', 'r')
        text = fC.read()
        text = text.replace("    ", "")
        text = text.replace('"', "")
        text = text.replace(',', "")
        text = text.replace("\\", "")
        text = text[2:-1]
        C_text.insert("1.0", text)
        C_text.configure(state='disabled')
        fC.close()

root = tk.Tk()
root.title("LR1")

code_label = tk.Label(root, text="Код на C#", font=("Arial", 16))
code_label.grid(column=1, row=1)
code_text = tk.Text(root, height=15, width=42)
code_text.grid(column=1,row=2)

token_label = tk.Label(root, text="Итог", font=("Arial", 16))
token_label.grid(column=3, row=1)
token_text = tk.Text(root, height=15, width=42)
token_text.grid(column=3,row=2)

tru_button = tk.Button(root, text="Выполнить", command=button_click)
tru_button.grid(column=2, row=1, rowspan=2)

tru_button1 = tk.Button(root, text="Файл", command=file)
tru_button1.grid(column=2, row=2, rowspan=3)

W_label = tk.Label(root, text="Лексемы служебных слов", font=("Arial", 16))
W_label.grid(column=1, row=4)
W_text = tk.Text(root, height=10, width=30)
W_text.grid(column=1,row=5)

R_label = tk.Label(root, text="Лексемы разделителей", font=("Arial", 16))
R_label.grid(column=2, row=4)
R_text = tk.Text(root, height=10, width=30)
R_text.grid(column=2,row=5)

O_label = tk.Label(root, text="Лексемы операций", font=("Arial", 16))
O_label.grid(column=3, row=4)
O_text = tk.Text(root, height=10, width=30)
O_text.grid(column=3,row=5)

N_label = tk.Label(root, text="Лексемы числовых констант", font=("Arial", 16))
N_label.grid(column=1, row=6)
N_text = tk.Text(root, height=10, width=30)
N_text.grid(column=1,row=7)

I_label = tk.Label(root, text="Лексемы идентификаторов", font=("Arial", 16))
I_label.grid(column=2, row=6)
I_text = tk.Text(root, height=10, width=30)
I_text.grid(column=2,row=7)

C_label = tk.Label(root, text="Лексемы символьных констант", font=("Arial", 16))
C_label.grid(column=3, row=6)
C_text = tk.Text(root, height=10, width=30)
C_text.grid(column=3,row=7)

root.mainloop()