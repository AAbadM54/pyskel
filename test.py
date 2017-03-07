import os
from parse.parser import Parser

parser = Parser()
parser.export_arguments()
os.system('python3 -m unittest discover -s test -p "test_*.py" -v')
