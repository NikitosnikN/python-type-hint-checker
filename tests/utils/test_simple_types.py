import typing as tp

from python_type_hint_checker.utils import istype


def test_str():
    _str = "a"
    assert istype(_str, str) is True


def test_int():
    _int = 1
    assert istype(_int, int) is True


def test_bool():
    _bool = True
    assert istype(_bool, bool) is True


def test_bytes():
    _bytes = b"bytes"
    assert istype(_bytes, bytes) is True
    assert istype(_bytes, tp.ByteString) is True


def test_hashable():
    for i in (1, "str", b"bytes", True, None):
        assert istype(i, tp.Hashable) is True
    for i in (list(), dict()):
        assert istype(i, tp.Hashable) is False


def test_none():
    _none = None
    assert istype(_none, None) is True
