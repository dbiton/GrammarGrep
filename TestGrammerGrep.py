import unittest

from GrammarGrep import GrammarGrep

code_simple_function = \
    "def f(x, y):\n" \
    "   z = x + y\n" \
    "   s = 's'\n" \
    "   return z*z"

code_simple_statement = "x = y + 5 * 3"

code_number = "21211"

code_asserts = \
    "def f(x, y):\n" \
    "   z = x + y\n" \
    "   s = 's'\n" \
    "   return z*z"

class TestGrammerGrep(unittest.TestCase):

    def test_match_plaintext_char(self):
        grep = GrammarGrep(code_simple_function)
        self.assertEqual(grep.match("s"), [((2, 3), (2, 4)), ((2, 8), (2, 9))])

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
        self.assertEqual(grep.match(";expr"), [((0, 0), (0, 1)), ((0, 4), (0, 13)),
                                               ((0, 8), (0, 13)), ((0, 12), (0, 13))])

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
        self.assertEqual(grep.match("2;(1;*;)"), [((0, 0), (0, 1)), ((0, 0), (0, 2)),
                                                  ((0, 2), (0, 3)), ((0, 2), (0, 5))])

    def test_match_meta_question(self):
        grep = GrammarGrep(code_number)
        self.assertEqual(grep.match("2;(1;?;)"), [((0, 0), (0, 1)), ((0, 0), (0, 2)),
                                                  ((0, 2), (0, 3))])

    def test_match_comprehensive_regex(self):
        grep = GrammarGrep(code_asserts)
        self.assertEqual(grep.match("assert(;(2;?1;*;) == len(;str));|assertEqual(2;(1;+;), ;(;id;|num;))"), [])

if __name__ == '__main__':
    unittest.main()
