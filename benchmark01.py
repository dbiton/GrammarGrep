#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#

import argparse
import inspect
import typing
import unittest
from io import StringIO

from nubia.internal.typing import argument, command
from nubia.internal.typing.argparse import add_command, find_command
from nubia.internal.typing.builder import build_value


class ParseError(Exception):
    pass


class ContainedParser(argparse.ArgumentParser):
    """
    Parser that gives options that avoid using sys.stdout, sys.stderr and
    raising SystemExit
    """

    def help(self):
        return self._print_to_buffer(self.print_help)

    def usage(self):
        return self._print_to_buffer(self.print_usage)

    def _print_to_buffer(self, print_function):
        s = StringIO()
        print_function(s)
        return s.getvalue()

    def error(self, message):
        raise ParseError(message)


class SimpleValuesBuilderTest(unittest.TestCase):
    def test_build_string(self):
        value = build_value("some string", str, False)
        self.assertEqual(value, "some string")

        value = build_value('"some string"', str, True)
        self.assertEqual(value, "some string")

    def test_build_int(self):
        value = build_value("1", int, False)
        self.assertEqual(value, 1)

        value = build_value("1", int, True)
        self.assertEqual(value, 1)

    def test_build_custom_type(self):
        def parser(string):
            return string.split("#")

        value = build_value("special#string", parser, False)
        self.assertEqual(value, ["special", "string"])

        value = build_value('"special#string"', parser, True)
        self.assertEqual(value, ["special", "string"])

    def test_build_tuple(self):
        value = build_value("foo bar,1,0.5", typing.Tuple[str, int, float], False)
        self.assertEqual(value, ("foo bar", 1, 0.5))

        value = build_value('("foo bar",1,0.5)', typing.Tuple[str, int, float], True)
        self.assertEqual(value, ("foo bar", 1, 0.5))

    def test_build_tuple_partially_typed(self):
        value = build_value(
            "foo bar,1,0.5", typing.Tuple[str, typing.Any, float], False
        )
        self.assertEqual(value, ("foo bar", "1", 0.5))

        value = build_value(
            '("foo bar",1,0.5)', typing.Tuple[str, typing.Any, float], True
        )
        self.assertEqual(value, (str("foo bar"), 1, 0.5))

    def test_build_tuple_untyped(self):
        value = build_value("foo bar,1,0.5", typing.Tuple, False)
        self.assertEqual(value, ("foo bar", "1", "0.5"))

        value = build_value('("foo bar",1,0.5)', typing.Tuple, True)
        self.assertEqual(value, (str("foo bar"), 1, 0.5))

    def test_build_tuple_single_element(self):
        value = build_value("foo bar", typing.Tuple[str], False)
        self.assertEqual(value, ("foo bar",))

        value = build_value('("foo bar",)', typing.Tuple[str], True)
        self.assertEqual(value, (str("foo bar"),))

    def test_build_typed_dict(self):
        value = build_value("a:1;b:2", typing.Mapping[str, int], False)
        self.assertEqual(value, {"a": 1, "b": 2})

        value = build_value(
            '{"a": "1", "b": 2, "c": 3.2}', typing.Mapping[str, int], True
        )
        self.assertEqual(value, {"a": 1, "b": 2, "c": 3})

    def test_build_typed_dict_mixed(self):
        value = build_value("a=1;b=2", typing.Mapping[str, int], False)
        self.assertEqual(value, {"a": 1, "b": 2})

        value = build_value("a:1;b=2", typing.Mapping[str, int], False)
        self.assertEqual(value, {"a": 1, "b": 2})

    def test_build_typed_dict_with_list(self):
        value = build_value("a=1,2,3;b=2", typing.Mapping[str, str], False)
        self.assertEqual(value, {"a": "1,2,3", "b": "2"})

        value = build_value("a=1,2,3;b=2", typing.Mapping[str, typing.List[int]], False)
        self.assertEqual(value, {"a": [1, 2, 3], "b": [2]})

    def test_build_partially_typed_dict(self):
        value = build_value("a:1;b:2", typing.Mapping[typing.Any, int], False)
        self.assertEqual(value, {"a": 1, "b": 2})

        value = build_value(
            '{"a": "1", "b": 2, 0: 3}', typing.Mapping[typing.Any, int], True
        )
        self.assertEqual(value, {"a": 1, "b": 2, 0: 3})

    def test_build_untyped_dict(self):
        value = build_value("a:1;b:2", typing.Mapping, False)
        self.assertEqual(value, {"a": "1", "b": "2"})

        value = build_value('{"a": 1, "b": 2.5}', typing.Mapping, True)
        self.assertEqual(value, {"a": 1, "b": 2.5})

    def test_build_typed_list(self):
        value = build_value("1,2,3", typing.List[int], False)
        self.assertEqual(value, [1, 2, 3])

        value = build_value("hello,world,test", typing.List[str], False)
        self.assertEqual(value, ["hello", "world", "test"])

        value = build_value("hello", typing.List[str], False)
        self.assertEqual(value, ["hello"])

        value = build_value('["1",2,3.2]', typing.List[int], True)
        self.assertEqual(value, [1, 2, 3])

    def test_build_untyped_list(self):
        value = build_value("1,2,3", typing.List, False)
        self.assertEqual(value, ["1", "2", "3"])

        value = build_value('["1",2,3.5]', typing.List, True)
        self.assertEqual(value, ["1", 2, 3.5])

    def test_build_any_typed_list(self):
        value = build_value("1,2,3", typing.List[typing.Any], False)
        self.assertEqual(value, ["1", "2", "3"])

        value = build_value('["1",2,3.5]', typing.List[typing.Any], True)
        self.assertEqual(value, ["1", 2, 3.5])

    def test_build_whitespaces(self):
        value = build_value(" a : 1 ; b : 2 ", typing.Mapping[str, int], False)
        self.assertEqual(value, {"a": 1, "b": 2})

        value = build_value('{ "a" : 1 , "b" : 2 }', typing.Mapping[str, int], True)
        self.assertEqual(value, {"a": 1, "b": 2})

        value = build_value(" 1 , 2 , 3 ", typing.List[int], False)
        self.assertEqual(value, [1, 2, 3])

        value = build_value("[ 1 , 2 , 3 ]", typing.List[int], True)
        self.assertEqual(value, [1, 2, 3])

        value = build_value(" 1 , 2 , 3 ", typing.Tuple[int, int, int], False)
        self.assertEqual(value, (1, 2, 3))

        value = build_value("( 1 , 2 , 3 )", typing.Tuple[int, int, int], True)
        self.assertEqual(value, (1, 2, 3))

    def test_build_with_casting(self):
        value = build_value("a:1;b:2;c:3", typing.Mapping[str, float])
        self.assertEqual(value, {"a": 1.0, "b": 2.0, "c": 3.0})

        value = build_value("a:1;b:2;c:3", typing.Mapping[str, str])
        self.assertEqual(value, {"a": "1", "b": "2", "c": "3"})

        self.assertRaises(
            ValueError, build_value, "a:1;b:2;c:3", typing.Mapping[int, int]
        )

    def test_build_nested_structures(self):
        inpt = """{
            "a": 1,
            "b": {
                "c": [2, 3, 4, [5, 6]]
            }
        }"""
        expected = {"a": 1, "b": {"c": [2, 3, 4, [5, 6]]}}
        expected_type = typing.Any
        self.assertEqual(build_value(inpt, expected_type, True), expected)

        inpt = """{
            "a": [ [1, 2], [3, 4] ],
            "b": [ [10, 20, 30], [40] ]
        }"""
        expected = {"a": [[1, 2], [3, 4]], "b": [[10, 20, 30], [40]]}
        # dict of str => list of list of ints
        expected_type = typing.Mapping[str, typing.List[typing.List[int]]]
        self.assertEqual(build_value(inpt, expected_type, True), expected)

    def test_build_tuple_error(self):
        # too many arguments
        self.assertRaises(
            ValueError,
            build_value,
            "foo bar,1,0.5,extra!",
            typing.Tuple[str, int, float],
            False,
        )

        self.assertRaises(
            ValueError,
            build_value,
            '("foo bar", 1, 0.5, "extra!")',
            typing.Tuple[str, int, float],
            True,
        )

        # too few arguments
        self.assertRaises(
            ValueError, build_value, "foo bar", typing.Tuple[str, int, float], False
        )

        self.assertRaises(
            ValueError, build_value, '("foo bar",)', typing.Tuple[str, int, float], True
        )


class ArgparseExtensionTest(unittest.TestCase):
    def test_no_decorator_simple(self):
        def foo():
            return "bar"

        def foo2(arg1, arg2):
            return (arg1, arg2)

        self._test(foo, "foo".split(), "bar")
        self._test(
            foo,
            "foo --invalid arg".split(),
            ParseError("unrecognized arguments: --invalid arg"),
        )

        self._test(foo2, "foo2 --arg1=abc --arg2=123".split(), ("abc", "123"))
        self._test(foo2, "foo2 --arg1 abc --arg2 123".split(), ("abc", "123"))

    def test_no_decorator_defaults(self):
        def foo(arg1="bar"):
            return arg1

        def foo2(arg1=True):
            return arg1

        def foo3(arg1=False):
            return arg1

        self._test(foo, "foo".split(), "bar")
        self._test(foo, "foo --arg1 lol".split(), "lol")

        # boolean args are exposed as flags that works as on/off switches
        # if the argument default is True, the flag works as an "off" switch
        self._test(foo2, "foo2".split(), True)
        self._test(foo2, "foo2 --arg1".split(), False)
        # if the argument default is False, the flag works as an "on" switch
        self._test(foo3, "foo3".split(), False)
        self._test(foo3, "foo3 --arg1".split(), True)

    def test_argument_decorated_simple(self):
        @argument("arg1")
        @argument("arg2")
        def foo(arg1, arg2):
            return "{} {}".format(arg1, arg2)

        self._test(foo, "foo --arg1 Hello --arg2 World".split(), "Hello World")

    def test_argument_decorated_different_name(self):
        @argument("arg1", name="banana")
        @argument("arg2", name="apple")
        def foo(arg1, arg2):
            return "{} {}".format(arg1, arg2)

        # arg2 is not decorated
        @argument("arg1", name="banana")
        def foo2(arg1, arg2):
            return "{} {}".format(arg1, arg2)

        # arg2 is decorated but pretty much useless in this form
        @argument("arg1", name="banana")
        @argument("arg2")
        def foo3(arg1, arg2):
            return "{} {}".format(arg1, arg2)

        self._test(foo, "foo --banana Hello --apple World".split(), "Hello World")
        self._test(foo2, "foo2 --banana Hello --arg2 World".split(), "Hello World")
        self._test(foo3, "foo3 --banana Hello --arg2 World".split(), "Hello World")

        self._test(foo, "foo --arg1 Hello --apple World".split(), ParseError)

    def test_argument_decorated_aliases(self):
        @argument("arg", aliases=["banana", "apple", "b", "a"])
        def foo(arg):
            return arg

        self._test(foo, "foo --arg bar".split(), "bar")
        self._test(foo, "foo --banana bar".split(), "bar")
        self._test(foo, "foo --apple bar".split(), "bar")
        self._test(foo, "foo -b bar".split(), "bar")
        self._test(foo, "foo -a bar".split(), "bar")

    def test_argument_decorated_kwargs(self):
        @argument("arg", type=int, description="arg help")
        @argument("extra_arg", type=int, description="extra")
        def foo(arg, **kwargs):
            return (arg, kwargs)

        self._test(foo, "foo --arg 6".split(), (6, {"extra_arg": None}))
        self._test(foo, "foo --extra-arg 15".split(), ParseError)
        self._test(foo, "foo --arg 14 --another-extra-arg 15".split(), ParseError)
        self._test(foo, "foo --arg 3 --extra-arg 15".split(), (3, {"extra_arg": 15}))

    def test_argument_decorated_naming_conventions(self):
        @argument("arg_1", aliases=["_argument__1"])
        @argument("arg_2", name="_argument___2")
        def __foo__bar__(arg_1, arg_2):
            return "{} {}".format(arg_1, arg_2)

        self._test(__foo__bar__, "foo-bar --arg-1 x --argument-2 y".split(), "x y")
        self._test(__foo__bar__, "foo-bar --argument-1 x --argument-2 y".split(), "x y")

    def test_argument_dict_list_type_lifting(self):
        @argument("arg_1", type=typing.Mapping[str, int])
        @argument("arg_2", type=typing.List[int])
        def __foo__bar__(arg_1, arg_2):
            return (arg_1, arg_2)

        self._test(__foo__bar__, "foo-bar --arg-1 x --arg-2 y".split(), ParseError)

        self._test(__foo__bar__, "foo-bar --arg-1 1 --arg-2 2".split(), ParseError)
        self._test(
            __foo__bar__,
            "foo-bar --arg-1 allData=1 --arg-2 2".split(),
            ({"allData": 1}, [2]),
        )
        self._test(
            __foo__bar__,
            "foo-bar --arg-1 all=1;nothing-data:2 --arg-2 2".split(),
            ({"all": 1, "nothing-data": 2}, [2]),
        )
        self._test(
            __foo__bar__,
            "foo-bar --arg-1 all=1;nothing-data=2 --arg-2 2".split(),
            ({"all": 1, "nothing-data": 2}, [2]),
        )
        self._test(
            __foo__bar__,
            "foo-bar --arg-1 all=1;nothing-data=2 --arg-2 2 3".split(),
            ({"all": 1, "nothing-data": 2}, [2, 3]),
        )
        self._test(
            __foo__bar__,
            "foo-bar --arg-1 all=1;nothing-data=2 --arg-2 2 3".split(),
            ({"all": 1, "nothing-data": 2}, [2, 3]),
        )

    def test_argument_list_in_dict_type_lifting(self):
        @argument("arg_1", type=typing.Mapping[str, typing.List[int]])
        def __foo__bar__(arg_1):
            return arg_1

        self._test(__foo__bar__, "foo-bar --arg-1 x".split(), ParseError)

        self._test(__foo__bar__, "foo-bar --arg-1 allData=1".split(), {"allData": [1]})
        self._test(
            __foo__bar__,
            "foo-bar --arg-1 all=1;nothing-data:2".split(),
            {"all": [1], "nothing-data": [2]},
        )
        self._test(
            __foo__bar__,
            "foo-bar --arg-1 all=1,2,3;nothing-data=2".split(),
            {"all": [1, 2, 3], "nothing-data": [2]},
        )
        self._test(
            __foo__bar__,
            "foo-bar --arg-1 all=1;nothing-data=2,2,3".split(),
            {"all": [1], "nothing-data": [2, 2, 3]},
        )

    def test_argument_decorated_unknown_arg(self):
        with self.assertRaises(NameError):

            @argument("arg1", description="arg1 description")
            @argument("bar", description="this arg doesnt exist!")
            def foo(arg1, arg2):
                pass

    def test_kwargs(self):
        try:

            @argument("arg1", description="this exists!")
            def foo(arg1, **kwargs):
                pass

        except Exception as e:
            self.fail("Should not have thrown: {}".format(e))

    def test_kwargs_with_arguments(self):
        try:

            @argument("arg1", description="this exists!")
            @argument("arg2", description="this is in kwargs!")
            def foo(arg1, **kwargs):
                pass

        except Exception as e:
            self.fail("Should not have thrown: {}".format(e))

    def test_command_decorator_presence(self):
        def foo():
            return "bar"

        self._test(foo, ["foo"], "bar")
        self._test(command(foo), ["foo"], "bar")
        self._test(command()(foo), ["foo"], "bar")

    def test_command_exclusive_args_simple(self):
        @command(exclusive_arguments=["arg1", "arg2"])
        def foo(arg1="", arg2="", arg3=""):
            return ",".join(str(arg) for arg in (arg1, arg2, arg3))

        self._test(foo, "foo --arg1=bar".split(), "bar,,")
        self._test(foo, "foo --arg2=bar".split(), ",bar,")
        self._test(foo, "foo --arg3=bar".split(), ",,bar")
        self._test(foo, "foo --arg1=bar --arg3=bar".split(), "bar,,bar")
        self._test(foo, "foo --arg2=bar --arg3=bar".split(), ",bar,bar")

        self._test(foo, "foo --arg1=bar --arg2=bar".split(), ParseError)
        self._test(foo, "foo --arg1=bar --arg2=bar --arg3=bar".split(), ParseError)

    def test_command_exclusive_args_array(self):
        @command(exclusive_arguments=[["arg1", "arg2"], ["arg3", "arg4"]])
        def foo(arg1="", arg2="", arg3="", arg4=""):
            return ",".join(str(arg) for arg in (arg1, arg2, arg3, arg4))

        self._test(foo, "foo --arg1=bar".split(), "bar,,,")
        self._test(foo, "foo --arg2=bar".split(), ",bar,,")
        self._test(foo, "foo --arg3=bar".split(), ",,bar,")
        self._test(foo, "foo --arg4=bar".split(), ",,,bar")
        self._test(foo, "foo --arg1=bar --arg3=bar".split(), "bar,,bar,")
        self._test(foo, "foo --arg1=bar --arg4=bar".split(), "bar,,,bar")
        self._test(foo, "foo --arg2=bar --arg3=bar".split(), ",bar,bar,")
        self._test(foo, "foo --arg2=bar --arg4=bar".split(), ",bar,,bar")

        self._test(foo, "foo --arg1=bar --arg2=bar".split(), ParseError)
        self._test(foo, "foo --arg3=bar --arg4=bar".split(), ParseError)
        self._test(
            foo, "foo --arg1=bar --arg2=bar --arg3=bar --arg4=bar".split(), ParseError
        )

    def test_command_repeated_exclusive_args(self):
        with self.assertRaises(ValueError):
            # arg1 is present in two exclusive groups
            @command(exclusive_arguments=[["arg1", "arg2"], ["arg1", "arg3"]])
            def foo(arg1="", arg2="", arg3=""):
                pass

    def test_command_unknown_exclusive_args(self):
        with self.assertRaises(NameError):
            # arg bar doesnt exist
            @command(exclusive_arguments=[["arg1", "bar"]])
            def foo(arg1="", arg2="", arg3=""):
                pass

    def test_duplicate_argument_decorator(self):
        with self.assertRaises(ValueError):
            # two refs to the same arg
            @command
            @argument("arg", name="arg1")
            @argument("arg", name="arg2")
            def foo(arg=1):
                pass

    def test_positional_arg(self):
        @argument("arg", positional=True)
        def foo(arg):
            return arg

        self._test(foo, "foo lalala", "lalala")

    def test_positional_arg_with_default(self):
        @argument("arg1", positional=True)
        @argument("arg2")
        def foo(arg1, arg2="default_arg1"):
            return "{},{}".format(arg1, arg2)

        self._test(foo, "foo lalala", "lalala,default_arg1")
        self._test(foo, "foo lalala --arg2 bububu", "lalala,bububu")
        self._test(foo, "foo --arg2 bububu lalala", "lalala,bububu")

    def test_only_single_value_allowed_for_positional(self):
        @argument("arg1", positional=True)
        def foo(arg1):
            pass

        self._test(foo, "foo lalala bububu", ParseError)

    def test_missing_positional(self):
        @argument("arg", positional=True)
        def foo(arg):
            pass

        self._test(foo, "foo", ParseError)

    def test_multiple_positionals(self):
        @argument("arg1", positional=True)
        @argument("arg2", positional=True)
        @argument("arg3")
        def foo(arg1, arg2, arg3="default"):
            return ",".join([arg1, arg2, arg3])

        self._test(foo, "foo arg1v arg2v", "arg1v,arg2v,default")
        self._test(foo, "foo arg1v arg2v --arg3 arg3v", "arg1v,arg2v,arg3v")
        self._test(foo, "foo arg1v --arg3 arg3v arg2v", "arg1v,arg2v,arg3v")
        self._test(foo, "foo --arg3 arg3v arg1v arg2v", "arg1v,arg2v,arg3v")

    def test_multiple_positionals_not_relates_to_decorator(self):
        # just all permutations of three decorators

        @argument("arg1", positional=True)
        @argument("arg2", positional=True)
        @argument("arg3", positional=True)
        def foo(arg1, arg2, arg3):
            return ",".join([arg1, arg2, arg3])

        self._test(foo, "foo arg1v arg2v arg3v", "arg1v,arg2v,arg3v")

        @argument("arg1", positional=True)
        @argument("arg3", positional=True)
        @argument("arg2", positional=True)
        def foo(arg1, arg2, arg3):
            return ",".join([arg1, arg2, arg3])

        self._test(foo, "foo arg1v arg2v arg3v", "arg1v,arg2v,arg3v")

        @argument("arg2", positional=True)
        @argument("arg1", positional=True)
        @argument("arg3", positional=True)
        def foo(arg1, arg2, arg3):
            return ",".join([arg1, arg2, arg3])

        self._test(foo, "foo arg1v arg2v arg3v", "arg1v,arg2v,arg3v")

        @argument("arg2", positional=True)
        @argument("arg3", positional=True)
        @argument("arg1", positional=True)
        def foo(arg1, arg2, arg3):
            return ",".join([arg1, arg2, arg3])

        self._test(foo, "foo arg1v arg2v arg3v", "arg1v,arg2v,arg3v")

        @argument("arg3", positional=True)
        @argument("arg1", positional=True)
        @argument("arg2", positional=True)
        def foo(arg1, arg2, arg3):
            return ",".join([arg1, arg2, arg3])

        self._test(foo, "foo arg1v arg2v arg3v", "arg1v,arg2v,arg3v")

        @argument("arg3", positional=True)
        @argument("arg2", positional=True)
        @argument("arg1", positional=True)
        def foo(arg1, arg2, arg3):
            return ",".join([arg1, arg2, arg3])

        self._test(foo, "foo arg1v arg2v arg3v", "arg1v,arg2v,arg3v")

    def test_positional_with_default(self):
        msg = (
            "We explicitly do not support positional "
            "with default because it is confusing"
        )
        with self.assertRaises(ValueError, msg=msg):

            @command
            @argument("arg", positional=True)
            def foo(arg="default"):
                return arg

            # validation happens on building parser time so let's build one
            parser = ContainedParser()
            add_command(parser, foo)

    def test_positional_with_aliases(self):
        msg = "Aliases for positional not yet supported"
        with self.assertRaises(ValueError, msg=msg):

            @command
            @argument("arg", positional=True, aliases=["a"])
            def foo(arg="default"):
                return arg

            # validation happens on building parser time so let's build one
            parser = ContainedParser()
            add_command(parser, foo)

    def _test(self, command_function, arguments, expected_result):
        if isinstance(arguments, str):
            arguments = arguments.split()

        parser = ContainedParser()
        add_command(parser, command_function)
        try:
            parsed = parser.parse_args(args=arguments)
        except Exception as e:
            if inspect.isclass(expected_result):
                self.assertIsInstance(e, expected_result)
            elif isinstance(expected_result, ParseError):
                self.assertEqual(str(e), str(expected_result))
            else:
                raise
        else:
            command_function = find_command(parser, parsed, True)
            self.assertEqual(command_function(), expected_result)

#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#

from typing import List, Optional

from later.unittest import TestCase
from termcolor import cprint

from nubia import argument, command, deprecated
from tests.util import TestShell


class CommandSpecTest(TestCase):
    async def test_command_sync(self):
        @command
        def test_command() -> int:
            """
            Sample Docstring
            """
            return 22

        shell = TestShell(commands=[test_command])
        self.assertEqual(22, await shell.run_cli_line("test_shell test-command "))

    async def test_command_name_spec1(self):
        @command
        @argument("arg", description="argument help", aliases=["i"])
        async def test_command(arg: List[str]) -> int:
            """
            Sample Docstring
            """
            self.assertEqual(["a", "b"], arg)
            cprint(arg, "green")
            return 22

        shell = TestShell(commands=[test_command])
        self.assertEqual(
            22, await shell.run_cli_line("test_shell test-command --arg a b")
        )

        self.assertEqual(
            22, await shell.run_interactive_line('test-command arg=["a","b"]')
        )
        self.assertEqual(
            22, await shell.run_interactive_line("test-command arg=[a, b]")
        )

    async def test_command_name_spec2(self):
        """
        Explicitly setting the command name with underscore, we should respect
        the supplied name and not auto-transform it
        """

        @command("bleh_command")
        @argument("arg", description="argument help", aliases=["i"])
        async def test_command(arg: List[str]) -> int:
            """
            Sample Docstring
            """
            self.assertEqual(["a", "b"], arg)
            cprint(arg, "green")
            return 22

        shell = TestShell(commands=[test_command])
        self.assertEqual(
            22, await shell.run_cli_line("test_shell bleh_command --arg a b")
        )
        self.assertEqual(
            22, await shell.run_interactive_line('bleh_command arg=["a","b"]')
        )
        self.assertEqual(
            22, await shell.run_interactive_line("bleh_command arg=[a, b]")
        )

    async def test_command_async(self):
        @command
        @argument("arg", description="argument help", aliases=["i"])
        async def test_command(arg: List[str]) -> int:
            """
            Sample Docstring
            """
            self.assertEqual(["a", "b"], arg)
            cprint(arg, "green")
            return 22

        shell = TestShell(commands=[test_command])
        self.assertEqual(
            22, await shell.run_cli_line("test_shell test-command --arg a b")
        )
        self.assertEqual(
            22, await shell.run_interactive_line('test-command arg=["a","b"]')
        )

    async def test_command_aliases_spec(self):
        """
        Testing aliases
        """

        @command("bleh_command", aliases=["bleh"])
        @argument("arg", description="argument help", aliases=["i"])
        async def test_command(arg: List[str]) -> int:
            """
            Sample Docstring
            """
            self.assertEqual(["a", "b"], arg)
            cprint(arg, "green")
            return 22

        shell = TestShell(commands=[test_command])
        self.assertEqual(22, await shell.run_cli_line("test_shell bleh -i a b"))

    async def test_command_find_approx_spec(self):
        """
        Testing approximate command / subcommand typing
        """

        @command("command_first", aliases=["first"])
        @argument("arg", description="argument help", aliases=["i"])
        async def test_command_1(arg: int = 22) -> int:
            """
            Sample Docstring
            """
            cprint(arg, "green")
            return arg

        @command("command_second", aliases=["second"])
        @argument("arg", description="argument help", aliases=["i"])
        async def test_command_2(arg: int = 23) -> int:
            """
            Sample Docstring
            """
            cprint(arg, "green")
            return arg

        shell = TestShell(commands=[test_command_1, test_command_2])

        # correct command name
        self.assertEqual(22, await shell.run_interactive_line("first"))
        # unique prefix command name
        self.assertEqual(22, await shell.run_interactive_line("f"))
        # unique levenshtein command name
        self.assertEqual(22, await shell.run_interactive_line("firts"))
        # unique prefix + levenshtein command name
        self.assertEqual(22, await shell.run_interactive_line("firs"))
        # non-unique prefix command name
        self.assertEqual(None, await shell.run_interactive_line("command"))

        # approximate matching only works for interactive mode, not CLI
        self.assertEqual(22, await shell.run_cli_line("test_shell first"))
        with self.assertRaises(SystemExit):
            await shell.run_cli_line("test_shell f")
        with self.assertRaises(SystemExit):
            await shell.run_cli_line("test_shell firts")
        with self.assertRaises(SystemExit):
            await shell.run_cli_line("test_shell firs")
        with self.assertRaises(SystemExit):
            await shell.run_cli_line("test_shell command")

    async def test_no_type_works_the_same(self):
        @command
        @argument("arg", positional=True)
        async def test_command(arg: str) -> int:
            """
            Sample Docstring
            """
            self.assertIsInstance(arg, str)
            self.assertEqual("1", arg)
            return 64 + int(arg)

        shell = TestShell(commands=[test_command])
        self.assertEqual(65, await shell.run_cli_line("test_shell test-command 1"))
        self.assertEqual(65, await shell.run_interactive_line("test-command 1"))
        self.assertEqual(65, await shell.run_interactive_line('test-command "1"'))

        @command
        @argument("arg")
        async def test_command(arg: str) -> int:
            """
            Sample Docstring
            """
            self.assertIsInstance(arg, str)
            self.assertEqual("1", arg)
            return 64 + int(arg)

        shell = TestShell(commands=[test_command])
        self.assertEqual(
            65, await shell.run_cli_line("test_shell test-command --arg 1")
        )
        self.assertEqual(
            65,
            await shell.run_interactive_line("test-command arg=1"),
        )
        self.assertEqual(
            65,
            await shell.run_interactive_line('test-command arg="1"'),
        )

    async def test_command_with_postional(self):
        @command
        @argument("arg1", positional=True)
        @argument("arg2", positional=True)
        @argument("arg3", positional=True)
        async def test_command(arg1: str, arg2: str, arg3: str) -> int:
            """
            Sample Docstring
            """
            cprint([arg1, arg2])
            self.assertEqual("1", arg1)
            self.assertIsInstance(arg1, str)
            self.assertEqual("2", arg2)
            self.assertIsInstance(arg2, str)
            self.assertEqual("nubia", arg3)
            return 64 * int(arg1) + int(arg2)

        shell = TestShell(commands=[test_command])
        self.assertEqual(
            66, await shell.run_cli_line("test_shell test-command 1 2 nubia")
        )
        self.assertEqual(66, await shell.run_interactive_line("test-command 1 2 nubia"))

    async def test_command_with_extra_spaces(self):
        @command
        @argument("arg1", positional=True)
        async def test_command(arg1: str) -> None:
            """
            Sample Docstring
            """
            self.assertEqual("1", arg1)
            self.assertIsInstance(arg1, str)
            return True

        shell = TestShell(commands=[test_command])
        self.assertTrue(await shell.run_interactive_line("test-command 1"))
        self.assertTrue(await shell.run_interactive_line("test-command  1"))
        self.assertTrue(await shell.run_interactive_line("test-command   1"))
        self.assertTrue(await shell.run_interactive_line(" test-command 1"))
        self.assertTrue(await shell.run_interactive_line("  test-command 1"))
        self.assertTrue(await shell.run_interactive_line("test-command 1 "))
        self.assertTrue(await shell.run_interactive_line("test-command 1  "))
        self.assertTrue(await shell.run_interactive_line("  test-command  1  "))

    async def test_command_with_postional_and_named_arguments(self):
        @command
        @argument("arg2", positional=True)
        @argument("arg3", positional=True)
        async def test_command(arg1: str, arg2: str, arg3: str) -> int:
            """
            Sample Docstring
            """
            cprint([arg1, arg2])
            self.assertEqual("1", arg1)
            self.assertIsInstance(arg1, str)
            self.assertEqual("2", arg2)
            self.assertIsInstance(arg2, str)
            self.assertEqual("nubia", arg3)
            return 64 * int(arg1) + int(arg2)

        shell = TestShell(commands=[test_command])
        self.assertEqual(
            66, await shell.run_cli_line("test_shell test-command --arg1=1 2 nubia")
        )
        self.assertEqual(
            66, await shell.run_interactive_line("test-command arg1=1 2 nubia")
        )
        self.assertEqual(
            66, await shell.run_interactive_line("test-command arg1=1 arg2=2 nubia")
        )
        # Fails parsing because positionals have to be at the end
        self.assertEqual(
            1, await shell.run_interactive_line("test-command 2 nubia arg1=1")
        )

    async def test_command_with_mutex_groups(self):
        @command(exclusive_arguments=["arg1", "arg2"])
        @argument("arg1")
        @argument("arg2")
        async def test_command(arg1: str = "0", arg2: str = "0") -> int:
            """
            Sample Docstring
            """
            return 64 * int(arg1) + int(arg2)

        shell = TestShell(commands=[test_command])
        self.assertEqual(
            64, await shell.run_cli_line("test_shell test-command --arg1 1")
        )
        self.assertEqual(
            64,
            await shell.run_interactive_line("test-command arg1=1"),
        )

        self.assertEqual(
            2, await shell.run_cli_line("test_shell test-command --arg2 2")
        )
        self.assertEqual(
            2,
            await shell.run_interactive_line("test-command arg2=2"),
        )

        with self.assertRaises(SystemExit):
            await shell.run_cli_line("test_shell test-command --arg1 1 --arg2 2")

        self.assertEqual(
            66,
            await shell.run_interactive_line("test-command arg1=1 arg2=2"),
            "We are not enforsing mutex groups on interactive",
        )

    async def test_command_with_mutex_groups_two_positionals(self):
        msg = "We don't supporting mutex group with required arguments"
        with self.assertRaises(ValueError, msg=msg):

            @command(exclusive_arguments=["arg1", "arg2"])
            @argument("arg1", positional=True)
            @argument("arg2")
            async def test_command(arg1: str, arg2: str = "lalala") -> int:
                """
                Sample Docstring
                """
                return -1

            await TestShell(commands=[test_command]).run_async()

    async def test_command_default_argument(self):
        """
        Tests that calling a command from the CLI without all arguments
        specified will fall back to the default arguments set in the command
        definition.
        """

        @command
        @argument("arg", description="argument help", aliases=["i"])
        async def test_command(arg: int = 22) -> int:
            """
            Sample Docstring
            """
            cprint(arg, "green")
            return arg

        shell = TestShell(commands=[test_command])
        self.assertEqual(22, await shell.run_cli_line("test_shell test-command"))
        self.assertEqual(22, await shell.run_interactive_line("test-command"))

    async def test_command_optional_argument(self):
        """
        Same as above but check for make the argument optional in Python sense.
        """

        @command
        @argument("arg", description="argument help", aliases=["i"])
        async def test_command(arg: Optional[List[str]] = None) -> int:
            """
            Sample Docstring
            """
            arg = arg or ["42"]
            cprint(arg, "green")
            return sum(int(x) for x in arg)

        shell = TestShell(commands=[test_command])
        self.assertEqual(42, await shell.run_cli_line("test_shell test-command"))
        self.assertEqual(42, await shell.run_interactive_line("test-command"))
        self.assertEqual(0, await shell.run_cli_line("test_shell test-command --arg 0"))
        self.assertEqual(
            0,
            await shell.run_interactive_line("test-command arg=[0]"),
        )

    async def test_command_one_required_one_default_argument(self):
        """
        Tests that calling a command from the CLI without all arguments
        specified will fall back to the default arguments set in the command
        definition.
        """

        @command("bleh_command")
        @argument("arg1", description="argument help", aliases=["i1"])
        @argument("arg2", description="argument 2 help", aliases=["i2"])
        async def test_command(arg1: int, arg2: int = 1) -> int:
            """
            Sample Docstring
            """
            cprint(arg1, "green")
            return arg1 + arg2

        shell = TestShell(commands=[test_command])
        self.assertEqual(
            22, await shell.run_cli_line("test_shell bleh_command --arg1=21")
        )
        self.assertEqual(
            22,
            await shell.run_interactive_line("bleh_command arg1=21"),
        )

    async def test_command_for_blacklist_plugin_allowed(self):
        @command("allowed")
        async def test_command():
            """
            Sample Docstring
            """
            cprint("Command Executed as required", "green")
            return 42

        shell = TestShell(commands=[test_command])
        self.assertEqual(42, await shell.run_cli_line("test_shell allowed"))
        self.assertEqual(42, await shell.run_interactive_line("allowed"))

    async def test_command_for_blacklist_plugin_blacklisted(self):
        @command("blocked")
        async def test_command():
            """
            Sample Docstring
            """
            cprint("Command executed, but should be blocked", "red")
            return 3

        shell = TestShell(commands=[test_command])
        self.assertEqual(1, await shell.run_cli_line("test_shell blocked"))
        self.assertEqual(1, await shell.run_interactive_line("blocked"))

    async def test_command_with_negative_ints(self):
        @command("minus_command")
        @argument("arg1", type=int)
        async def test_command(arg1):
            """
            Sample Docstring
            """
            self.assertEqual(type(5), type(arg1))
            return 42 if arg1 == -1 else -1

        shell = TestShell(commands=[test_command])
        # Cli run
        self.assertEqual(
            42, await shell.run_cli_line("test_shell minus_command --arg1=-1")
        )
        # Interactive
        self.assertEqual(42, await shell.run_interactive_line("minus_command arg1=-1"))

    async def test_command_with_negative_floats(self):
        @command("minus_command")
        @argument("arg1", type=float)
        async def test_command(arg1):
            """
            Sample Docstring
            """
            self.assertEqual(type(5.0), type(arg1))
            return 42 if arg1 == -1.0 else 55

        shell = TestShell(commands=[test_command])
        # Cli run
        self.assertEqual(
            42, await shell.run_cli_line("test_shell minus_command --arg1=-1")
        )
        self.assertEqual(
            42, await shell.run_cli_line("test_shell minus_command --arg1=-1.0")
        )
        # Interactive
        self.assertEqual(42, await shell.run_interactive_line("minus_command arg1=-1"))
        self.assertEqual(
            42, await shell.run_interactive_line("minus_command arg1=-1.0")
        )

    async def test_command_deprecation(self):
        @deprecated(superseded_by="new-command")
        @command
        def old_command() -> int:
            """
            Sample Docstring
            """
            cprint("This command is deprecated", "yellow")
            return new_command()

        @command
        def new_command() -> int:
            """
            Sample Docstring
            """
            cprint("This is the future", "green")
            return 42

        shell = TestShell(commands=[old_command, new_command])
        self.assertEqual(42, await shell.run_cli_line("test_shell old-command"))
        self.assertEqual(42, await shell.run_interactive_line("old-command"))
        self.assertEqual(42, await shell.run_cli_line("test_shell new-command"))
        self.assertEqual(42, await shell.run_interactive_line("new-command"))

    async def test_type_lifting(self):
        @command
        @argument("args")
        async def test_command(args: List[str]) -> str:
            """
            Sample Docstring
            """
            return "|".join(args)

        shell = TestShell(commands=[test_command])
        # CLI
        self.assertEqual(
            "a", await shell.run_cli_line("test_shell test-command --args a")
        )
        self.assertEqual(
            "a|b", await shell.run_cli_line("test_shell test-command --args a b")
        )
        # Interactive
        self.assertEqual("a", await shell.run_interactive_line('test-command args="a"'))
        self.assertEqual(
            "a", await shell.run_interactive_line('test-command args=["a"]')
        )
        self.assertEqual(
            "a|b", await shell.run_interactive_line('test-command args=["a", "b"]')
        )