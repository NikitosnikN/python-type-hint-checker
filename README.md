# Python Type Hint Checker

Python Type Hint Checker is a Python library for parsing type hinting (PEP 484) 

### Motivation

It is research / home project

## Installation

TBD

## Usage


Use function to manually check PEP 484 type hints

```python
import typing
from python_type_hint_checker.utils import istype

istype([1, 2, 3], typing.List[int])             # returns True
istype({"foo": "bar"}, typing.Dict[str, int])   # returns False
``` 

Or use decorator to validate function type hints

```python
from python_type_hint_checker.decorator import validate_typing 

@validate_typing()
def some_func(a: str, b: int):
    ...

some_func("foo", 0)     # Normal execution
some_func(1, "bar")     # Exception will be raised
```

## Tests

To run tests `pytest` should be installed

```bash
pip install pytest
```

Then execute pytest command

```bash
pytest
```

## Roadmap

[ ] complete most common types

[ ] complete decorator

[ ] cover code with tests (100%)

[ ] release to PyPi
...

## Contributing

Feel free to contribute

## License
[MIT](https://choosealicense.com/licenses/mit/)