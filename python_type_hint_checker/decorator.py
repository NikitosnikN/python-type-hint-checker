from typing import get_type_hints
from functools import wraps

from .utils import istype

__all__ = ["validate_typing"]


def validate_typing(raise_exception: bool = True):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # TODO
            return func(*args, **kwargs)
        return wrapper
    return decorator
