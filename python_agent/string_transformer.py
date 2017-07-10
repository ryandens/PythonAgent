import ast


class StringTransformer(ast.NodeTransformer):
    """Wraps all integers in a call to Integer()"""

    def visit_Str(self, node):
        # if isinstance(node.s, str):
        #     print("Node replaced")
        #     return ast.Call(func=ast.Name(id='AgentString', ctx=ast.Load()),
        #                     args=[node], keywords=[])
        # print("node not replaced")
        # return node
        return ast.Call(func=ast.Name(id='AgentString', ctx=ast.Load()),
                        args=[node], keywords=[])
