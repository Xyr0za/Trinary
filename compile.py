from sys import argv, exit
from print_color import print

from lexer import *
from parser import *

version: str = "1.1.2"

print(
f"""
========================================
=                                      =
={f'Trinary V{version}'.center(38)}=
=                                      =
========================================\n
""", color = "v"
)

try:
    file_location = argv[1]
    if argv[1].split('.')[1] != "tia":
        raise FileNotFoundError
    lines = [i.strip() for i in open(file_location)]
except FileNotFoundError:
    print("That is not a valid .TIA file", tag="ERROR", tag_color="red", color="white")
    print("Process ending\n", tag="ERROR", tag_color="red", color="white")
    exit()

lexer = Lexer().get_lexer()
pg = Parser()
pg.parse()
parser = pg.get_parser()

context = {}

for instruction in lines:
    if instruction == '' or instruction[0:2] == "//":
        continue

    tokens = lexer.lex(instruction)
    parser.parse(tokens).eval(context)
