import ast
import RegExParser


class GrammarGrep:
    def __init__(self, code: str = None):
        self.code = None
        self.labels = None
        if code is not None:
            self.load_code(code)

    'note that match is greedy - so it does not get every match, but instead the longest one from each initial position'
    def match(self, regex):
        nfa = RegExParser.regex_to_nfa(regex)
        'nfa.display_graph()'
        return nfa.match_all(self.code, self.labels)

    def replace(self, regex, replace_list):
        nfa = RegExParser.regex_to_nfa(regex)
        return nfa.replace_all(self.code, self.labels, replace_list)

    def load_code(self, code: str):
        labels = {}

        class LabelVisitor(ast.NodeVisitor):
            def generic_visit(self, node: ast.AST):
                if isinstance(node, ast.expr):
                    key = (node.lineno - 1, node.col_offset)
                    value = ("expr_type", node.end_lineno - 1, node.end_col_offset)
                    labels.setdefault(key, [])
                    labels[key].append(value)
                if isinstance(node, ast.stmt):
                    key = (node.lineno - 1, node.col_offset)
                    value = ("stmt_type", node.end_lineno - 1, node.end_col_offset)
                    labels.setdefault(key, [])
                    labels[key].append(value)
                if isinstance(node, ast.Name):
                    key = (node.lineno - 1, node.col_offset)
                    value = ("id_type", node.end_lineno - 1, node.end_col_offset)
                    labels.setdefault(key, [])
                    labels[key].append(value)
                if isinstance(node, ast.Num):
                    key = (node.lineno - 1, node.col_offset)
                    value = ("num_type", node.end_lineno - 1, node.end_col_offset)
                    labels.setdefault(key, [])
                    labels[key].append(value)
                if isinstance(node, ast.Str):
                    key = (node.lineno - 1, node.col_offset)
                    value = ("str_type", node.end_lineno - 1, node.end_col_offset)
                    labels.setdefault(key, [])
                    labels[key].append(value)
                ast.NodeVisitor.generic_visit(self, node)
        parsed_code = ast.parse(code)
        self.code = code.splitlines()
        LabelVisitor().visit(parsed_code)
        self.labels = labels
