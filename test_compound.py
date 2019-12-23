import unittest
from solution import processList

class TestCompound(unittest.TestCase):

    def test_basic(self):
        words = set(['man', 'woman', 'manhandle', 'handle', 'race', 'drag', 'car', 'racecar', 'computer', 'bag', 'dragon', 'manbag'])
        expected = ['manbag', 'manhandle', 'racecar']
        self.assertEqual(processList(words), expected)

    def test_confusing(self):
        words = set(['man', 'manhandle', 'manhandleman'])
        expected = ['manhandleman']
        self.assertEqual(processList(words), expected)

    def test_advanced(self):
        words = set(['cat', 'cats', 's', 'and', 'sand', 'catsand'])
        expected = ['cats', 'catsand', 'sand']
        self.assertEqual(processList(words), expected)

    def test_fail(self):
        words = set(['man'])
        expected = []
        self.assertEqual(processList(words), expected)

        words = set([])
        self.assertEqual(processList(words), expected)

    def test_mcec(self):
        words = set(['ab', 'cd', 'abcde'])
        expected = []
        self.assertEqual(processList(words), expected)

        words = set(['ab', 'bc', 'abc'])
        self.assertEqual(processList(words), expected)


if __name__ == '__main__':
    unittest.main()
