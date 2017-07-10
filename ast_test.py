#!/usr/bin/python3
import ast, inspect, __builtin__, marshal, py_compile, time
from python_agent import AgentString, StringTransformer

filename = "sample_file.py"
with open(filename) as f:
    code_one = f.read()


tree = ast.parse(code_one)
tree = StringTransformer().visit(tree)


# for x in tree.body:
#     if isinstance(x, ast.Assign):
#         print(x)


# Add lineno & col_offset to the nodes we created
ast.fix_missing_locations(tree)
co = compile(tree, "<ast>", "exec")

# print(dir(code))
print(co)
print(type(co))
# exec co
# print(AgentString.COUNT)

with open('../output.pyc', 'wb') as fc:
    fc.write('\0\0\0\0')
    py_compile.wr_long(fc, long(time.time()))
    marshal.dump(co, fc)
    fc.flush()
    fc.seek(0, 0)
    fc.write(py_compile.MAGIC)