#!/usr/bin/python3
import ast, inspect, __builtin__
from python_agent import AgentString, StringTransformer

filename = "sample_file.py"
file_two = "test.py"
with open(filename) as f:
    code_one = f.read()

with open(file_two) as f_two:
    code_two = f_two.read()

tree = ast.parse(code_one)
tree = StringTransformer().visit(tree)
tree_two = ast.parse(code_two)
tree_two = StringTransformer().visit(tree_two)

for x in tree.body:
    if isinstance(x, ast.Assign):
        print(x)


# Add lineno & col_offset to the nodes we created
ast.fix_missing_locations(tree)
ast.fix_missing_locations(tree_two)
# co_two = compile(tree_two, "<ast>", "exec")
co = compile(tree, "<ast>", "exec")

exec co
print(AgentString.COUNT)
