from rply import *

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):

        # Add Comments
        self.lexer.add('COMMENT', r'//[^\n]*')
        self.lexer.ignore(r'//[^\n]*')

        # Print
        self.lexer.add('PRINT', r'print')
        self.lexer.add('QSOL', r'qsolve')


        # Parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # Semi Colon
        self.lexer.add('SEMI_COLON', r'\;')

        # Operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MUL', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('MOD', r'\%')
        self.lexer.add('EXP', r'\^')
        self.lexer.add('SIN', r'sin')
        self.lexer.add('COS', r'cos')

        # Punc
        self.lexer.add('DOT', r'\.')
        self.lexer.add('COM', r'\,')

        # Number
        self.lexer.add('NUMBER', r'\d+')

        # Assignment
        self.lexer.add('ASSIGN', r'\=')

        # Identifier
        self.lexer.add('IDENTIFIER', r'[a-zA-Z_][a-zA-Z_0-9]*')
        self.lexer.add('BAR', r'\|')

        # Ignore spaces
        self.lexer.ignore('\s+')


    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
