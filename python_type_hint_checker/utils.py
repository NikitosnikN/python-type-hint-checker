import typing as tp

__all__ = ["istype"]


def _istype_iterator_itarable(__obj, __obj_type, __typing):
    if issubclass(__obj_type, tp.Generator):
        return _istype_generator(__obj, __typing)

    args = tp.get_args(__typing)

    if args:
        if isinstance(__obj_type, tp.Dict):
            return all([*[istype(k, args[0]) for k in __obj.keys()], *[istype(v, args[1]) for v in __obj.values()]])
        else:
            return all([istype(i, args[0]) for i in __obj])

    return isinstance(__obj, __typing)


def _istype_callable(__obj, __typing):
    # TODO is coroutine ?
    return isinstance(__obj, __typing)


def _istype_generator(__obj, __typing):
    return isinstance(__obj, __typing)


def _istype_special(__obj, __typing):
    pass


def istype(__obj: tp.Any, __typing):
    """

    :param __obj:
    :param __typing:
    :return:
    """
    __obj_type = type(__obj)

    if isinstance(__typing, type):
        return isinstance(__obj, __typing)  # or __obj_type is __typing
    elif issubclass(__obj_type, tp.Callable):
        return _istype_callable(__obj, __typing)
    elif issubclass(__obj_type, (tp.Iterator, tp.Iterable)):
        return _istype_iterator_itarable(__obj, __obj_type, __typing)
    elif issubclass(type(__typing), tp._SpecialForm):  # noqa
        return _istype_special(__obj, __typing)
    elif __typing is None:
        return __obj is None

    return isinstance(__obj, __typing)
