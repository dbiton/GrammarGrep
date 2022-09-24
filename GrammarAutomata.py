# import graphviz

import os

import graphviz

os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'


class GrammarAutomata:
    class Group:
        def __init__(self, lineno, col_offset):
            self.lineno_begin = lineno
            self.lineno_end = float('-inf')
            self.col_offset_begin = col_offset
            self.col_offset_end = float('-inf')

    class Node:
        def __init__(self):
            self.edges = []

        def add_edge(self, node_dst, cond):
            self.edges.append((node_dst, cond))

    class Cond:
        # types are str, type_id, type_stmt, type_expr, type_str, type_num, epsilon
        def __init__(self, type, str=""):
            self.type = type
            self.str = str

        # returns if satisfied and index after passing
        def check(self, codelines, labels: dict, lineno, col_offset):
            if self.type == "str":
                return codelines[lineno].startswith(self.str, col_offset), [(lineno, col_offset + len(self.str))]
            elif self.type == "epsilon":
                return True, [(lineno, col_offset)]
            else:
                matchs = []
                if (lineno, col_offset) in labels:
                    list_types = labels[(lineno, col_offset)]
                    for (type, end_lineno, end_col_offset) in list_types:
                        if type == self.type:
                            matchs.append((end_lineno, end_col_offset))
                if len(matchs) > 0:
                    return True, matchs
                else:
                    return False, []

    def __init__(self):
        self.nodes = []
        self.groups = []

    def add_group(self, group_index):
        self.groups.append((group_index, self.nodes[0], self.nodes[-1]))

    def get_groups_begin(self, node):
        return [group_index for (group_index, begin_node, _) in self.groups if begin_node == node]

    def get_groups_end(self, node):
        return [group_index for (group_index, _, end_node) in self.groups if end_node == node]

    @staticmethod
    def get_next_begin(codelines, lineno, col_offset):
        if col_offset < len(codelines[lineno]) - 1:
            return lineno, col_offset + 1
        elif lineno < len(codelines) - 1:
            return lineno + 1, 0
        else:
            return -1, -1

    @staticmethod
    def create_automata_matching(string):
        ga = GrammarAutomata()
        ga.add_node()
        ga.add_node()
        cond = GrammarAutomata.Cond("str", string)
        ga.add_edge(0, 1, cond)
        return ga

    @staticmethod
    def create_automata_meta(meta_type):
        ga = GrammarAutomata()
        ga.add_node()
        ga.add_node()
        cond = GrammarAutomata.Cond(meta_type)
        ga.add_edge(0, 1, cond)
        return ga

    @staticmethod
    def create_automata_or(ga0, ga1):
        ga = GrammarAutomata()
        ga.nodes = [GrammarAutomata.Node()] + ga0.nodes + ga1.nodes + [GrammarAutomata.Node()]
        ga.add_edge(0, 1, GrammarAutomata.Cond("epsilon"))
        ga.add_edge(0, 1+len(ga0.nodes), GrammarAutomata.Cond("epsilon"))
        ga.add_edge(len(ga0.nodes), len(ga.nodes) - 1, GrammarAutomata.Cond("epsilon"))
        ga.add_edge(len(ga.nodes)-2, len(ga.nodes) - 1, GrammarAutomata.Cond("epsilon"))
        ga.groups = ga0.groups + ga1.groups
        return ga

    @staticmethod
    def create_automata_star(ga0):
        ga = GrammarAutomata.create_automata_plus(ga0)
        ga = GrammarAutomata.create_automata_question(ga)
        ga.groups = ga0.groups
        return ga

    @staticmethod
    def create_automata_plus(ga0):
        ga = GrammarAutomata()
        ga.nodes = [GrammarAutomata.Node()] + ga0.nodes + [GrammarAutomata.Node()]
        ga.add_edge(0, 1, GrammarAutomata.Cond("epsilon"))
        ga.add_edge(len(ga.nodes)-2, 1, GrammarAutomata.Cond("epsilon"))
        ga.add_edge(len(ga.nodes)-2, len(ga.nodes)-1, GrammarAutomata.Cond("epsilon"))
        ga.groups = ga0.groups
        return ga

    @staticmethod
    def create_automata_question(ga0):
        ga = GrammarAutomata()
        ga.nodes = [GrammarAutomata.Node()] + ga0.nodes + [GrammarAutomata.Node()]
        ga.add_edge(0, 1, GrammarAutomata.Cond("epsilon"))
        ga.add_edge(len(ga.nodes)-2, len(ga.nodes)-1, GrammarAutomata.Cond("epsilon"))
        ga.add_edge(1, len(ga.nodes)-1, GrammarAutomata.Cond("epsilon"))
        ga.groups = ga0.groups
        return ga

    @staticmethod
    def create_automata_concat(ga0, ga1):
        if ga0 is None:
            return ga1
        ga = GrammarAutomata()
        ga.nodes = ga0.nodes + ga1.nodes
        ga.add_edge(len(ga0.nodes) - 1, len(ga0.nodes), GrammarAutomata.Cond("epsilon"))
        ga.groups = ga0.groups + ga1.groups
        return ga

    def add_node(self):
        self.nodes.append(GrammarAutomata.Node())

    def add_edge(self, id_src, id_dst, cond):
        self.nodes[id_src].add_edge(self.nodes[id_dst], cond)

    def print_graph(self):
        for node in self.nodes:
            print("NODE", hex(id(node)), ":")
            for edge in node.edges:
                print("EDGE TO", hex(id(edge[0])), "WITH COND TYPE:", edge[1].type, "STR:", edge[1].str)

    def display_graph(self):
        dot = graphviz.Digraph(comment='Automata')
        for i, node in enumerate(self.nodes):
            dot.node(hex(id(node)), str(i))
            for edge in node.edges:
                if edge[1].type == "str":
                    dot.edge(hex(id(node)), hex(id(edge[0])), edge[1].type + ":'" + edge[1].str + "'")
                else:
                    dot.edge(hex(id(node)), hex(id(edge[0])), edge[1].type)
        dot.render('doctest-output/automata.gv', view=True)
        pass

    def consolidate_groups(self, groups):
        index_to_range = {}
        for (lineno, col_offset), groups_begin in groups[0].items():
            for group_index in groups_begin:
                if group_index not in index_to_range:
                    index_to_range[group_index] = [(lineno, col_offset), None]
        for (lineno, col_offset), groups_end in groups[1].items():
            for group_index in groups_end:
                if group_index in index_to_range:
                    index_to_range[group_index][1] = (lineno, col_offset)
        # remove uncompleted groups
        index_to_range = {k: l for k, l in index_to_range.items() if l[1] is not None}
        return index_to_range

    def match_generator(self, codelines, labels):
        lineno_begin = 0
        col_offset_begin = 0
        while lineno_begin != -1:
            stack = [(self.nodes[0], lineno_begin, col_offset_begin)]
            group_markers = {}, {}
            last_match_end = None
            while len(stack) > 0:
                node, lineno, col_offset = stack[-1]
                stack.pop()
                groups_begin = self.get_groups_begin(node)
                groups_end = self.get_groups_end(node)
                if len(groups_begin) > 0:
                    group_markers[0][(lineno, col_offset)] = groups_begin
                if len(groups_end) > 0:
                    group_markers[1][(lineno, col_offset)] = groups_end
                for node_dst, cond in node.edges:
                    satisfied, listends = cond.check(codelines, labels, lineno, col_offset)
                    if satisfied:
                        if node_dst == self.nodes[-1]:
                            last_match_end = self.last_listend(listends)
                        for ends in listends:
                            stack.append((node_dst, ends[0], ends[1]))
            if last_match_end is not None:
                yield ((lineno_begin, col_offset_begin), last_match_end), self.consolidate_groups(group_markers)
            lineno_begin, col_offset_begin = self.get_next_begin(codelines, lineno_begin, col_offset_begin)

    def last_listend(self, listends):
        last = listends[0]
        for i in range(1, len(listends)):
            curr = listends[i]
            if curr[0] > last[0] or (curr[0] == last[0] and curr[1] > last[1]):
                last = curr
        return last

    def match_all(self, codelines: list, labels):
        return [m for (m, _) in self.match_generator(codelines, labels)]

    def match_first(self, codelines: list, labels):
        return next(self.match_generator(codelines, labels))[0]

    def get_key(self, val, d):
        for key, value in d.items():
            if val == value:
                return key
        return None

    def replace_helper(self, res, substr, group_position, offset):
        begin = offset[0] + group_position[0][0], offset[1] + group_position[0][1]
        end = offset[0] + group_position[1][0], offset[1] + group_position[1][1]
        res_replaced = res[:begin[0]] + [res[begin[0]][:begin[1]] + substr + res[end[0]][end[1]:]] + res[end[0]+1:]
        offset_new = offset #offset[0], len(substr) - end[1] + begin[1] + offset[1]
        return res_replaced, offset_new

    def replace_all(self, codelines: str, labels, replace_list):
        res = codelines
        offset = (0, 0)
        for match, groups in self.match_generator(codelines, labels):
            for group_index, group_position in groups.items():
                substr = replace_list[group_index]
                res, offset = self.replace_helper(res, substr, group_position, offset)
        return res

    def replace_first(self, codelines, labels, replace_list):
        # match, groups = next(self.match_generator(codelines, labels))[0]
        # print(match, groups)
        return codelines
