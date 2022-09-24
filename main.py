import os
import argparse
from termcolor import colored

from GrammarGrep import *

os.system('color')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Use regular expressions for finding and replacing code segments.')

    parser.add_argument('-f', '--filename', type=str, required=True, help='path to file queried')
    parser.add_argument('-m', '--match', type=str, required=True, help='regex used for matchin')
    parser.add_argument('-r', '--replace', nargs="*", required=False,
                        help='list of strings, ith group in matched string will be replaced with ith string in list')
    args = parser.parse_args()

    f = open(args.filename, "r")
    code = f.read()

    grammerGrep = GrammarGrep()
    grammerGrep.load_code(code)

    code = code.splitlines()
    if args.replace is not None and len(args.replace) > 0:
        result = grammerGrep.replace(args.match, args.replace)
        print('\n'.join(result))
    else:
        match_ranges = grammerGrep.match(args.match)
        for (lineno_beg, col_beg), (lineno_end, col_end) in match_ranges:
            print("line", lineno_beg)
            print(code[lineno_beg][:col_beg] + colored(code[lineno_beg][col_beg:col_end], 'red') +
                  code[lineno_beg][col_end:], '\n')
