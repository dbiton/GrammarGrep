import unittest

from GrammarGrep import GrammarGrep

code_simple_function = \
    "def f(x, y):\n" \
    "   z = x + y\n" \
    "   s = 's'\n" \
    "   return z*z"

code_simple_statement = "x = y + 5 * 3"

code_number = "212112"

code_asserts = \
    "def f():\n" \
    "   assert(11 == len('s'))\n" \
    "   assertEqual(21, 21)\n" \
    "   name = 'dvir'\n" \
    "   assert(2 == len(name))\n" \
    "   assert(22 == len(name))\n" \
    "   assertEqual(2111, name)\n" \
    "   assertEqual(2, 2)"


# note: match does not return all matches, but instead the longest ones starting at each initial position

class TestGrammerGrep(unittest.TestCase):

    def test_match_plaintext_char(self):
        grep = GrammarGrep(code_simple_function)
        self.assertEqual(grep.match("s"), [((2, 3), (2, 4)), ((2, 8), (2, 9))])

    def test_match_adjacent(self):
        grep = GrammarGrep("123123123")
        self.assertEqual(grep.match("123"), [((0, 0), (0, 3)), ((0, 3), (0, 6)), ((0, 6), (0, 9))])

    def test_match_multiline_plaintext(self):
        grep = GrammarGrep(code_simple_function)
        self.assertEqual(grep.match("def f(x, y):\n   z ="), [((0, 0), (1, 6))])

    def test_match_plaintext_string(self):
        grep = GrammarGrep(code_simple_function)
        self.assertEqual(grep.match("z*z"), [((3, 10), (3, 13))])

    def test_match_meta_or(self):
        grep = GrammarGrep(code_simple_function)
        self.assertEqual(grep.match("z*z;|s"), [((2, 3), (2, 4)), ((2, 8), (2, 9)), ((3, 10), (3, 13))])

    def test_match_concat(self):
        grep = GrammarGrep(code_simple_statement)
        self.assertEqual(grep.match(";id + 5 * ;num"), [((0, 4), (0, 13))])

    def test_match_num(self):
        grep = GrammarGrep(code_simple_statement)
        self.assertEqual(grep.match(";num"), [((0, 8), (0, 9)), ((0, 12), (0, 13))])

    def test_match_str(self):
        grep = GrammarGrep(code_simple_function)
        self.assertEqual(grep.match(";str"), [((2, 7), (2, 10))])

    def test_match_expr(self):
        grep = GrammarGrep(code_simple_statement)
        self.assertEqual(grep.match(";expr"), [((0, 0), (0, 1)), ((0, 4), (0, 13))])

    def test_match_stmt(self):
        grep = GrammarGrep(code_simple_statement)
        self.assertEqual(grep.match(";stmt"), [((0, 0), (0, 13))])

    def test_match_id(self):
        grep = GrammarGrep(code_simple_statement)
        self.assertEqual(grep.match(";id"), [((0, 0), (0, 1)), ((0, 4), (0, 5))])

    def test_match_meta_plus(self):
        grep = GrammarGrep(code_number)
        self.assertEqual(grep.match("2;(1;+;)"), [((0, 0), (0, 2)), ((0, 2), (0, 5))])

    def test_match_meta_star(self):
        grep = GrammarGrep(code_number)
        self.assertEqual(grep.match("2;(1;*;)"), [((0, 0), (0, 2)),
                                                  ((0, 2), (0, 5)),
                                                  ((0, 5), (0, 6))])

    def test_match_meta_question(self):
        grep = GrammarGrep(code_number)
        self.assertEqual(grep.match("2;(1;?;)"), [((0, 0), (0, 2)),
                                                  ((0, 2), (0, 4)),
                                                  ((0, 5), (0, 6))])

    def test_unbalanced_parentheses(self):
        grep = GrammarGrep(code_asserts)
        self.assertRaises(RuntimeError, grep.match, ";(;(;x))")

    def test_match_comprehensive_regex(self):
        grep = GrammarGrep(code_asserts)
        self.assertEqual(grep.match("assert(;(2;?1;*;) == len(;str));|assertEqual(2;(1;+;), ;(;id;|;num;))"), [
            ((1, 3), (1, 25)),
            ((2, 3), (2, 22)),
            ((6, 3), (6, 26))
        ])

    def test_match_single_plaintext_char_in_group(self):
        grep = GrammarGrep(code_simple_statement)
        self.assertEqual(grep.match(";(+;)"), [((0, 6), (0, 7))])

    def test_replace_single_plaintext_char(self):
        grep = GrammarGrep(code_simple_statement)
        self.assertEqual(grep.replace(";(+;)", ['-']), ["x = y - 5 * 3"])

    def test_replace_multiple_in_single_line(self):
        grep = GrammarGrep(code_simple_statement)
        self.assertEqual(grep.replace(";(;id;) ;(+;) ;num * ;(;num;)", ['x', '-', 'z']), ["x = x - 5 * z"])

    def test_replace_multiple_in_multiple_lines(self):
        grep = GrammarGrep(code_asserts)

        self.assertEqual(grep.replace("assert(;(;num;) == len(;(;str;|;id;))", ['5', "'hello'"]), [
            "def f():",
            "   assert(5 == len('hello'))",
            "   assertEqual(21, 21)",
            "   name = 'dvir'",
            "   assert(5 == len('hello'))",
            "   assert(5 == len('hello'))",
            "   assertEqual(2111, name)",
            "   assertEqual(2, 2)"
        ])

    def test_replace_adjacent_matches(self):
        grep = GrammarGrep("123123123")
        self.assertEqual(grep.replace(";(123;)", ['321']), ["321321321"])

    def test_replace_multiple_occurrences_of_single_group_in_match(self):
        grep = GrammarGrep("123123123")
        self.assertEqual(grep.replace(";(123;);*", ['321']), ["321321321"])

    def test_replace_longest_match(self):
        grep = GrammarGrep("AAAAAAAAAAA")
        self.assertEqual(grep.replace(";(A;*;)", ['B']), ["B"])

if __name__ == '__main__':
    unittest.main()
