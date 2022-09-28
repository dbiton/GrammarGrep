import os
import re
import GrammarGrep
from GrammarAutomata import GrammarAutomata


def match_regex_python(regex: str, codelines: list):
    return [m.span() for m in re.finditer(regex, codelines)]


def match_regex_grammar(regex: str, codelines: list):
    gg = GrammarGrep.GrammarGrep(codelines)
    codelines_length = [len(s) for s in codelines]
    return [GrammarAutomata.flattened_range(r, codelines_length) for r in gg.match(regex)]


def timereps(reps, func):
    from time import time
    start = time()
    for i in range(0, reps):
        func()
    end = time()
    return (end - start) / reps


if __name__ == '__main__':
    regexes_python = ["test", "str|int|arg(1*)"]
    regexes_grep = ["test", "str;|int;|arg;(1*;)"]
    for regex_python, regex_grep in zip(regexes_python, regexes_grep):
        for benchmark_name in os.listdir("benchmarks"):
            with open(os.path.join("benchmarks", benchmark_name)) as f:
                codelines = "".join(f.readlines())
                t_python = timereps(10, lambda: match_regex_python(regex_python, codelines))
                t_grammar = timereps(10, lambda: match_regex_grammar(regex_grep, codelines))
                print(benchmark_name, regex_python, t_python, regex_grep, t_grammar)
