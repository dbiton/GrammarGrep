import os
import re

import numpy as np
import pandas as pd
import seaborn as sns
import itertools
import matplotlib.pyplot as plt
from collections import defaultdict
import statistics as st


import GrammarGrep
from GrammarAutomata import GrammarAutomata


def match_regex_regular(regex: str, codelines: list):
    return [m.span() for m in re.finditer(regex, codelines)]


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
    return (end - start) / reps


def benchmark_graph_plot(data):
    # set width of bar
    barWidth = 0.1
    fig = plt.subplots(figsize=(16, 8))

    # set height of bar

    MATCH_REGULAR = [st.mean(v) for (k, v) in data.items() if k[0] == "match regular"]
    MATCH_CONTEXT = [st.mean(v) for (k, v) in data.items() if k[0] == "match context"]
    REPLACE_REGULAR = [st.mean(v) for (k, v) in data.items() if k[0] == "replace regular"]
    REPLACE_CONTEXT = [st.mean(v) for (k, v) in data.items() if k[0] == "replace context"]

    # Set position of bar on X axis
    br1 = np.arange(len(MATCH_REGULAR))
    br2 = [x + barWidth for x in br1]
    br3 = [x + barWidth for x in br2]
    br4 = [x + barWidth for x in br3]

    # Make the plot
    plt.bar(br1, MATCH_REGULAR, color='r', width=barWidth,
            edgecolor='grey', label='Match Grep')
    plt.bar(br2, MATCH_CONTEXT, color='g', width=barWidth,
            edgecolor='grey', label='Match GrammarGrep')
    plt.bar(br3, REPLACE_REGULAR, color='b', width=barWidth,
            edgecolor='grey', label='Replace Grep')
    plt.bar(br4, REPLACE_CONTEXT, color='m', width=barWidth,
            edgecolor='grey', label='Replace GrammarGrep')

    # Adding Xticks
    plt.xlabel('Regular Expression', fontweight='bold', fontsize=15)
    plt.ylabel('Seconds', fontweight='bold', fontsize=15)
    plt.xticks([r + barWidth for r in range(len(MATCH_REGULAR))],
               np.arange(len(MATCH_REGULAR)))

    plt.yscale('log')

    plt.legend()
    plt.show()


if __name__ == '__main__':
    itercount = 16
    regexes_regular = ["test", "str|int|arg(1*)", "[-]?[0-9]+", "def [a-zA-Z0-9]*\([[a-zA-Z0-9]*\):"]
    regexes_context = ["test", "str;|int;|arg;(1*;)", ";num", "def ;id(;id):"]
    res = defaultdict(list)
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
                                                                               len(match_regex_regular(regex_regular,
                                                                                                       codelines)),
                                                                               len(match_regex_context(regex_context,
                                                                                                       codelines))))
                print("match regular:{} match context: {} replace regular:{} replace context: {}".format(
                    t_regular, t_context, t_replace_regular, t_replace_context))
                res[("match regular", regex_context)].append(t_regular)
                res[("match context", regex_context)].append(t_context)
                res[("replace regular", regex_context)].append(t_replace_regular)
                res[("replace context", regex_context)].append(t_replace_context)
    benchmark_graph_plot(res)
