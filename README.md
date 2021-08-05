# Python Unittest Sandbox
This project is used to demonstrate how the Python [unittest](https://docs.python.org/3/library/unittest.html) module may be used.

Tested against Python 3.7 on Ubuntu 20.x

## Environmental Concerns

This project makes use of [Pipenv](https://pipenv.pypa.io/en/latest/) although as it doesn't use any module outside of this project and the python standard library you should be able to make use of it anywhere where python 3.x is found. 

## Invoking tests

There are two modules of interest. One, `module_framework_illustrator`, outputs text to illustrate the order in which different elements of a unittest based module execute. This may be invoked as follows.
```
python -m module_framework_illustrator
```

A more realistic illustration of how tests are structured exists in `module.py` and may be invoked as follows.

```
python -m module
```
