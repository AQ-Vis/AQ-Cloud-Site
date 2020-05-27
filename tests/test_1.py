import unittest

import app

def test_load():
    assert app.root() == "Welcome!"
