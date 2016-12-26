"""Module for testing issue1."""

import unittest

import issue1


class TestIssue1Methods(unittest.TestCase):
    def setUp(self):
        self.string1 = 'The quick brown fox jumps over the lazy dog'
        self.string2 = 'Foxes are beautiful animals'
        self.string3 = 'The sun is shining brightly'
        self.string4 = '123'

    def tearDown(self):
        self.string1 = None
        self.string2 = None
        self.string3 = None
        self.string4 = None

    def test_find_substring(self):
        result = issue1.find_substring(self.string1, self.string2)
        self.assertEqual(result, 'fox')

    def test_if_substring_no_found(self):
        result = issue1.find_substring(self.string1, self.string4)
        self.assertEqual(result, None)

    def test_get_nouns(self):
        result = issue1.get_nouns('nounlist.txt')
        self.assertEqual(len(result), 4401)

    def test_is_noun_true(self):
        nouns = issue1.get_nouns('nounlist.txt')
        result = 'fox' in nouns
        self.assertTrue(result)

    def test_is_noun_false(self):
        nouns = issue1.get_nouns('nounlist.txt')
        result = 'happy' in nouns
        self.assertFalse(result)

    def test_make_plural_from_aberrant_map(self):
        result = issue1.make_plural('woman')
        self.assertEqual(result, 'women')

    def test_make_plural_empty_str(self):
        result = issue1.make_plural('')
        self.assertEqual(result, '')

    def test_make_plural_sxz(self):
        result = issue1.make_plural('fox')
        self.assertEqual(result, 'foxes')

    def test_make_plural_aeioudgkprt_h(self):
        result = issue1.make_plural('branch')
        self.assertEqual(result, 'branches')

    def test_make_plural_aeiou_y(self):
        result = issue1.make_plural('baby')
        self.assertEqual(result, 'babies')

    def test_make_plural_s(self):
        result = issue1.make_plural('holiday')
        self.assertEqual(result, 'holidays')

    def test_main_correct(self):
        result = issue1.main(self.string1, self.string2, 'nounlist.txt')
        self.assertEqual(result, 'foxes')

    def test_main_not_noun_or_empty(self):
        result = issue1.main(self.string1, self.string3, 'nounlist.txt')
        self.assertEqual(result, '')


if __name__ == '__main__':
    unittest.main()
