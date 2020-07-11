import typing as tp

from python_type_hint_checker.utils import istype


def _func():
    return True


async def _coro_func():
    return True


def test_func():
    assert istype(_func, tp.Callable)


def test_lambda():
    _lambda = lambda o: o  # noqa
    assert istype(_lambda, tp.Callable)

# def test_coroutine():
#     _coro = _coro_func()
#     assert istype(_coro, tp.Coroutine)
