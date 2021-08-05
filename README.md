# Python Unittest Sandbox
This project is used to demonstrate how the Python [unittest](https://docs.python.org/3/library/unittest.html) module may be used.

Tested against Python 3.7 on Ubuntu 20.x

## Environmental Concerns

This project makes use of [Pipenv](https://pipenv.pypa.io/en/latest/) although as it doesn't use any module outside of this project and the python standard library you should be able to make use of it anywhere where python 3.x is found. 

## Invoking tests

There are two modules of interest. 

### module_framework_illustrator

`module_framework_illustrator`, outputs text to illustrate the order in which different elements of a unittest based module execute. This may be invoked as follows.
```
python -m module_framework_illustrator
```

The expected output is 

```
(python-unittest-sandbox) rshea@foobar:~/src/python-unittest-sandbox/pyunsa$ python -m  module_framework_illustration
setUpModule: __main__ set up A

    setUpClass: TestCase1 set up B

        setUp: __main__.TestCase1.test_one set up C

            __main__.TestCase1.test_one running

        tearDown: __main__.TestCase1.test_one tear down C

.        setUp: __main__.TestCase1.test_two set up C

            __main__.TestCase1.test_two running

        tearDown: __main__.TestCase1.test_two tear down C

.    tearDownClass: TestCase1 tear down B

setUpModule: __main__ tear down A


----------------------------------------------------------------------
Ran 2 tests in 0.013s

OK

A more realistic illustration of how tests are structured exists in `module.py` and may be invoked as follows.

```
python -m module
```
