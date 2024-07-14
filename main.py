import json

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

    # файл, содержащий последовательность кодов лексем входной программы
    f = open('tokens.txt', 'w')
    f.write(output_sequence)
    f.close()

    for token_class in tokens.keys():
        with open('%s.json' % token_class, 'w') as file:
            json.dump({}, file)

    # файлы, содержащие все таблицы лексем
    for token_class in tokens.keys():
        with open('%s.json' % token_class, 'w') as write_file:
            data = {val: key for key, val in tokens[token_class].items()}
            json.dump(data, write_file, indent=4)
