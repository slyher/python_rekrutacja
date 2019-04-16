"""
implement python split functionality
split(text, separator)
separator may be multi character
function should return array of items between separator
"""
import unittest


class StringSplit:
    def split(self, text, separator):
        pass


class SimpleTestCase(unittest.TestCase):
    def setUp(self):
        self.string_split = StringSplit()

    def testForSimpleSplit(self):
        text ="111/123/231"
        separator = "/"
        assert self.string_split.split(text, separator) == text.split(separator)

    def testForComplexSplit(self):
        text = "Ala ma kota"
        separator = "ma"
        assert self.string_split.split(text, separator) == text.split(separator)
