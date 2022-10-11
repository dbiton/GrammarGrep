import os
import re
import GrammarGrep
from GrammarAutomata import GrammarAutomata


def match_regex_regular(regex: str, codelines: list):
    return [m.span() for m in re.finditer(regex, " ".join(codelines))]


def match_regex_context(regex: str, codelines: list):
    gg = GrammarGrep.GrammarGrep(codelines)
    codelines_length = [len(s) for s in codelines]
    return [GrammarAutomata.flattened_range(r, codelines_length) for r in gg.match(regex)]


def replace_regex_regular(regex: str, codelines: list, s: str):
    return re.sub(regex, s, " ".join(codelines))


def replace_regex_context(regex: str, codelines: list, s: str):
    gg = GrammarGrep.GrammarGrep(codelines)
    return gg.replace(regex, codelines)


def timereps(reps, func):
    from time import time
    start = time()
    for i in range(0, reps):
        func()
    end = time()
    return (end - start)


if __name__ == '__main__':
    itercount = 16
    regexes_regular = ["test", "str|int|arg(1*)", "[-]?[0-9]+", "def [a-zA-Z0-9]*\([[a-zA-Z0-9]*\):"]
    regexes_context = ["test", "str;|int;|arg;(1*;)", ";num", "def ;id(;id):"]
    for regex_context, regex_regular in zip(regexes_context, regexes_regular):
        for benchmark_name in os.listdir("benchmarks"):
            with open(os.path.join("benchmarks", benchmark_name)) as f:
                codelines = "".join(f.readlines())
                t_regular = timereps(itercount, lambda: match_regex_regular(regex_regular, codelines))
                t_context = timereps(itercount, lambda: match_regex_context(regex_context, codelines))
                t_replace_regular = timereps(itercount,
                                             lambda: replace_regex_regular(regex_context, codelines, "dummy"))
                t_replace_context = timereps(itercount,
                                             lambda: replace_regex_context(regex_context, codelines, "dummy"))
                print("benchmark: {}, regexes: {}, {}, matches: {}, {}".format(benchmark_name, regex_regular,
                                                                               regex_context,
                                                                               len(match_regex_regular(regex_regular, codelines)),
                                                                               len(match_regex_context(regex_regular, codelines))))
                print("match regular:{} match context: {} replace regular:{} replace context: {}".format(
                      t_regular, t_context, t_replace_regular, t_replace_context))
