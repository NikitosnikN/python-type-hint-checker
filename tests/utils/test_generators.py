import typing as tp

from python_type_hint_checker.utils import istype


def _gen_func():
    yield True


_gen_1 = _gen_func()
_gen_2 = (i for i in range(1))


def test_generators_true():
    assert istype(_gen_1, tp.Generator) is True
    assert istype(_gen_2, tp.Generator) is True


def test_generators_false():
    assert istype(_gen_1, tp.Callable) is False
    assert istype(_gen_2, tp.Callable) is False
