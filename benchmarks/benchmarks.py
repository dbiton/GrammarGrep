regex_1 = 'if len(;id) > 0:;|;(return ;id;)'
regex_2 = 'if len(;id) > 0:;|;(return ;id;)|;(return ;num;)'
regex_3 = 'if len(;id) > 0:;|;(return ;id;)'

code = '''def f(z: set):
    x = []
    y = "hello world"
    for i in range(32):
        if len(x) > 0:
            return 0
        if len(y) > 0:
            x += 1
            return x
'''

regex_1 = 'if len(;id) > 0:;|;(return ;id;)'
regex_2 = 'if len(;id) > 0:;|;(return ;id;)|;(return ;num;)'
regex_3 = 'if len(;id) > 0:;|;(return ;id;)'

code = '''def f(z: set):
    x = []
    y = "hello world"
    for i in range(32):
        if len(x) > 0:
            return 0
        if len(y) > 0:
            x += 1
            for i in range(32):
                if len(x) > 0:
                    return 0
                if len(y) > 0:
                    x += 1
                    for i in range(32):
                        if len(x) > 0:
                            return 0
                        if len(y) > 0:
                            x += 1
                            for i in range(32):
                                if len(x) > 0:
                                    return 0
                                if len(y) > 0:
                                    x += 1
                                    for i in range(32):
                                        if len(x) > 0:
                                            return 0
                                        if len(y) > 0:
                                            x += 1
                                        for i in range(32):
                                            if len(x) > 0:
                                                return 0
                                            if len(y) > 0:
                                                x += 1
                                            for i in range(32):
                                                if len(x) > 0:
                                                    return 0
                                                if len(y) > 0:
                                                    x += 1
                                                    for i in range(32):
                                                        if len(x) > 0:
                                                            return 0
                                                        if len(y) > 0:
                                                            x += 1
                                                            for i in range(32):
                                                                if len(x) > 0:
                                                                    return 0
                                                                if len(y) > 0:
                                                                    x += 1
                                                                    for i in range(32):
                                                                        if len(x) > 0:
                                                                            return 0
                                                                        if len(y) > 0:
                                                                            x += 1
                                                                        for i in range(32):
                                                                            if len(x) > 0:
                                                                                return 0
                                                                            if len(y) > 0:
                                                                                x += 1
                                                                            for i in range(32):
                                                                                if len(x) > 0:
                                                                                    return 0
                                                                                if len(y) > 0:
                                                                                    x += 1
                                                                                    for i in range(32):
                                                                                        if len(x) > 0:
                                                                                            return 0
                                                                                        if len(y) > 0:
                                                                                            x += 1
                                                                                            for i in range(32):
                                                                                                if len(x) > 0:
                                                                                                    return 0
                                                                                                if len(y) > 0:
                                                                                                    x += 1
                                                                                                    for i in range(32):
                                                                                                        if len(x) > 0:
                                                                                                            return 0
                                                                                                        if len(y) > 0:
                                                                                                            x += 1
                                                                                                        for i in range(32):
                                                                                                            if len(x) > 0:
                                                                                                                return 0
                                                                                                            if len(y) > 0:
                                                                                                                x += 1
                                                                                                            for i in range(32):
                                                                                                                if len(x) > 0:
                                                                                                                    return 0
                                                                                                                if len(y) > 0:
                                                                                                                    x += 1
                                                                                                                    for i in range(32):
                                                                                                                        if len(x) > 0:
                                                                                                                            return 0
                                                                                                                        if len(y) > 0:
                                                                                                                            x += 1
                                                                                                                            for i in range(32):
                                                                                                                                if len(x) > 0:
                                                                                                                                    return 0
                                                                                                                                if len(y) > 0:
                                                                                                                                    x += 1
                                                                                                                                    for i in range(32):
                                                                                                                                        if len(x) > 0:
                                                                                                                                            return 0
                                                                                                                                        if len(y) > 0:
                                                                                                                                            x += 1
                                                                                                                                        for i in range(32):
                                                                                                                                            if len(x) > 0:
                                                                                                                                                return 0
                                                                                                                                            if len(y) > 0:
                                                                                                                                                x += 1
                                                                                                                                                return x        
'''

code = '''
    regex=''
    groups=[]
    i_begin, i_end = 0. 0
    nfa = None
    i_curr = i_begin
    while i_curr < i_end: 
        meta_idx = regex.find(";", i_curr)
        if meta_idx == -1:
            nfa_step = GrammarAutomata.create_automata_matching(regex[i_curr:])
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_step)
            return nfa

        if meta_idx > i_curr:
            nfa_step = GrammarAutomata.create_automata_matching(regex[i_curr:meta_idx])
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_step)

        if regex[meta_idx + 1] == "(":
            idx_close, idx_group = groups[meta_idx]
            nfa_step = regex_to_nfa_aux(regex, groups, meta_idx + 2, idx_close)
            nfa_step.add_group(idx_group)
            i_curr = idx_close + 2
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_step)
        elif regex[meta_idx + 1] == "|":
            nfa_l = nfa
            nfa_r = regex_to_nfa_aux(regex, groups, meta_idx + 2, i_end)
            nfa = GrammarAutomata.create_automata_or(nfa_l, nfa_r)
            return nfa
        elif regex[meta_idx + 1] == "*":
            nfa_inner = regex_to_nfa_aux(regex, groups, i_curr, meta_idx)
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_inner)
            nfa = GrammarAutomata.create_automata_star(nfa)
            i_curr = meta_idx + 2
        elif regex[meta_idx + 1] == "+":
            nfa_inner = regex_to_nfa_aux(regex, groups, i_curr, meta_idx)
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_inner)
            nfa = GrammarAutomata.create_automata_plus(nfa)
            i_curr = meta_idx + 2
        elif regex[meta_idx + 1] == "?":
            nfa_inner = regex_to_nfa_aux(regex, groups, i_curr, meta_idx)
            nfa = GrammarAutomata.create_automata_concat(nfa, nfa_inner)
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
            print("Error!")
            return None
    return nfa
    '''