from Token.token_type import TokenType


class ErrorHandler:
    def __init__(self):
        self.hadError = False
        self.hadRuntimeError = False

    def runtime_error(self, error):
        print(f"[line {error.token.line}]: {error.message}")
        with open('error_logs.txt', 'a') as file:
            #error.token.line = error.token.line - 1
            err_log = f"[line {error.token.line}] :  {error.message} \n"
            file.write(err_log)
        self.hadRuntimeError = True

    def error(self, line, message):
        self.report(line, "")

    def report(self, line, where):
        print(f"[line {line}] Error{where}.")
        with open('error_logs.txt', 'a') as file:
            #line = line - 1
            err_log = f"[line {line}] Error{where}.\n"
            file.write(err_log)
        self.hadError = True

    def error_token(self, token, message):
        #token.line = token.line - 1
        if token.type == TokenType.EOF:
            self.report(token.line, " at end")
        else:
            self.report(token.line, f" at '{token.lexeme}'")
