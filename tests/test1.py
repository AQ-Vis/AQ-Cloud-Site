import unittest

import app

def homepage_test_1():
    assert app.root() == "Welcome!"
