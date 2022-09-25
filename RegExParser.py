from GrammarAutomata import GrammarAutomata

'''
Production Rules:
    s;|t;|v;+

    r = ;(s;) NOTE: denotes groups + order of ops
    r = st
    r = s;|t
    r = s;*
    r = s;+
    r = s;?
    r = ;id
    r = ;stmt
    r = ;expr
    r = ;str
    r = ;num

Examples:
    1. if len(;id) > ;num and ;expr:
    2. \(assertEquals(;expr, ;expr)\) | \(assert(;expr)\)
    3. ;id = ;str\?
    4. ;id = ;id ** ;num
    5. ;id = 1\(0\)\*
'''


def get_closing_paren(regex: str, paren_open_idx):
    i = regex.find(";", paren_open_idx)
    counter = 1
    while True:
        if regex[i + 1] == "(":
            counter += 1
        elif regex[i + 1] == ")":
            counter -= 1
        if counter == 0:
            return i + 2
        i = regex.find(";", i + 1)
        if i == -1:
            raise RuntimeError("Regular expression's parentheses are unbalanced")

def get_groups(regex: str):
    groups = {}
    i_begin = regex.find(";(", 0)
    while i_begin != -1:
        i_end = get_closing_paren(regex, i_begin+1)
        groups[i_begin] = (i_end, len(groups))
        i_begin = regex.find(";(", i_begin + 2)
    return groups


def regex_to_nfa_aux(regex: str, groups, i_begin, i_end):
    nfa = None
    i_curr = i_begin
    while i_curr < i_end:
        meta_idx = regex.find(";", i_curr, i_end)
        if meta_idx == -1:
            nfa_step = GrammarAutomata.create_automata_matching(regex[i_curr:i_end])
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_step)
            return nfa

        if meta_idx > i_curr:
            nfa_step = GrammarAutomata.create_automata_matching(regex[i_curr:meta_idx])
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_step)

        if regex[meta_idx + 1] == "(":
            idx_close, idx_group = groups[meta_idx]
            nfa_step = regex_to_nfa_aux(regex, groups, meta_idx + 2, idx_close - 2)
            nfa_step.add_group(idx_group)
            i_curr = idx_close
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_step)
        elif regex[meta_idx + 1] == "|":
            nfa_l = nfa
            nfa_r = regex_to_nfa_aux(regex, groups, meta_idx + 2, i_end)
            nfa = GrammarAutomata.create_automata_or(nfa_l, nfa_r)
            return nfa
        elif regex[meta_idx + 1] == "*":
            nfa = GrammarAutomata.create_automata_star(nfa)
            i_curr = meta_idx + 2
        elif regex[meta_idx + 1] == "+":
            nfa = GrammarAutomata.create_automata_plus(nfa)
            i_curr = meta_idx + 2
        elif regex[meta_idx + 1] == "?":
            nfa = GrammarAutomata.create_automata_question(nfa)
            i_curr = meta_idx + 2
        elif regex[meta_idx + 1:].startswith("id"):
            nfa_step = GrammarAutomata.create_automata_meta("id_type")
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_step)
            i_curr = meta_idx + 1 + 2
        elif regex[meta_idx + 1:].startswith("stmt"):
            nfa_step = GrammarAutomata.create_automata_meta("stmt_type")
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_step)
            i_curr = meta_idx + 1 + 4
        elif regex[meta_idx + 1:].startswith("expr"):
            nfa_step = GrammarAutomata.create_automata_meta("expr_type")
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_step)
            i_curr = meta_idx + 1 + 4
        elif regex[meta_idx + 1:].startswith("str"):
            nfa_step = GrammarAutomata.create_automata_meta("str_type")
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_step)
            i_curr = meta_idx + 1 + 3
        elif regex[meta_idx + 1:].startswith("num"):
            nfa_step = GrammarAutomata.create_automata_meta("num_type")
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_step)
            i_curr = meta_idx + 1 + 3
        else:
            raise RuntimeError("Could not compile regular expression")
    return nfa


def regex_to_nfa(regex: str):
    groups = get_groups(regex)
    return regex_to_nfa_aux(regex, groups, 0, len(regex))
