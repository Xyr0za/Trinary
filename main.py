from lexer import *
from parser import *

lines = [i for i in open("main.tia")]

lexer = Lexer().get_lexer()
pg = Parser()
pg.parse()
parser = pg.get_parser()

context = {}

for instrucion in lines:
    tokens = lexer.lex(instrucion)
    parser.parse(tokens).eval(context)