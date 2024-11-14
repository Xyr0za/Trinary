from rply import ParserGenerator
from abstree import *

class Parser():
    def __init__(self):
        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            ['NUMBER',
             'PRINT',
             'OPEN_PAREN', 'CLOSE_PAREN',
             'SEMI_COLON',
             'SUM', 'SUB', 'MUL', 'DIV', 'MOD', 'EXP',
             'ASSIGN', 'IDENTIFIER', 'BAR'],
            precedence=[
                ('left', ['SUM', 'SUB']),
                ('left', ['MUL', 'DIV', 'MOD']),
                ('right', ['EXP'])
            ]
        )
        self.symbolTable = {}

    def parse(self):
        @self.pg.production('program : PRINT OPEN_PAREN expression CLOSE_PAREN SEMI_COLON')
        def print_program(p):
            return Print(p[2])

        @self.pg.production('program : BAR IDENTIFIER ASSIGN expression SEMI_COLON')
        def assignment(p):
            var_name = p[1].getstr()
            value = p[3]
            return Assignment(var_name, value)


        @self.pg.production('expression : expression SUM expression')
        @self.pg.production('expression : expression SUB expression')
        @self.pg.production('expression : expression MUL expression')
        @self.pg.production('expression : expression DIV expression')
        @self.pg.production('expression : expression MOD expression')
        @self.pg.production('expression : expression EXP expression')
        def expression(p):

            left = p[0]
            right = p[2]
            operator = p[1]

            if operator.gettokentype() == 'SUM':
                return Sum(left, right)
            elif operator.gettokentype() == 'SUB':
                return Sub(left, right)
            elif operator.gettokentype() == 'MUL':
                return Mul(left, right)
            elif operator.gettokentype() == 'DIV':
                return Div(left, right)
            elif operator.gettokentype() == 'MOD':
                return Mod(left, right)
            elif operator.gettokentype() == "EXP":
                return Exp(left, right)

        @self.pg.production('expression : IDENTIFIER')
        def variable_reference(p):
            var_name = p[0].getstr()
            return Variable(var_name)

        @self.pg.production('expression : OPEN_PAREN expression CLOSE_PAREN')
        def paren_expression(p):
            return p[1]

        @self.pg.production('expression : NUMBER')
        def number(p):
            return Number(p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()