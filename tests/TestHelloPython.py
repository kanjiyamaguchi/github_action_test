# coding: utf-8
import unittest
from HelloPython import HelloPython


class TestHelloPython(unittest.TestCase):

    def test_hello(self):

        message = "(\^v^);"
        self.assertTrue(HelloPython(message=message).hello())

        message = 1111
        self.assertTrue(HelloPython(message=message).hello())

        message = "ああぁぁああ!!!"
        self.assertTrue(HelloPython(message=message).hello())
