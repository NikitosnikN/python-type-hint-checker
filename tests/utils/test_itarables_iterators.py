import typing as tp
from python_type_hint_checker.utils import istype


def test_list():
    _list = list()
    _list_of_str = ["str", "str"]
    _list_of_int = [0, 1]
    _list_of_bools = [True, False]
    _list_of_none = [None, None]
    _list_of_lists = [list(), list()]
    _list_recursive = [[1, 2], [3, 4]]
    _list_of_multiple_types = [1, "str", True]

    assert istype(_list, list) is True
    assert istype(_list, tp.List) is True
    assert istype(_list_of_str, tp.List[str]) is True
    assert istype(_list_of_int, tp.List[int]) is True
    assert istype(_list_of_bools, tp.List[bool]) is True
    assert istype(_list_of_none, tp.List[None]) is True
    assert istype(_list_of_lists, tp.List[list]) is True
    assert istype(_list_recursive, tp.List[tp.List[int]]) is True
    assert istype(_list_of_multiple_types, tp.List[int]) is False


def test_dict():
    _dict = dict()
    _dict_str_int = {"a": 1, "b": 2}
    _dict_int_bool = {0: False, 1: True}
    assert istype(_dict, dict) is True
    assert istype(_dict, tp.Dict) is True
    assert istype(_dict_str_int, tp.Dict[str, int]) is True
    assert istype(_dict_int_bool, tp.Dict[int, bool]) is True


def test_tuple():
    _tuple = tuple()
    assert istype(_tuple, tuple) is True
    assert istype(_tuple, tp.Tuple) is True


def test_set():
    _set = set()
    assert istype(_set, set) is True
    assert istype(_set, tp.Set) is True


def test_frozenset():
    _frozenset = frozenset()
    assert istype(_frozenset, frozenset) is True
    assert istype(_frozenset, tp.FrozenSet) is True
