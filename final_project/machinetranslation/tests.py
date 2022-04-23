'''
Doc to code for test function in tranlator.py
'''
import unittest

from translator import english_to_french 
from translator import french_to_english

class TestenglishToFrench(unittest.TestCase):
    '''tests the english to french translation'''
    def test_en2fr(self):
        '''here comes 4 tests 2 for asserteq 2 for assertNoteq'''
        self.assertNotEqual(english_to_french(0), 0)
        # test when null is given as input the output is null.
        self.assertNotEqual(english_to_french('null'), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # test when word is given as input the output is translated.
        self.assertEqual(english_to_french('Road'), 'Route')

class TestfrenchToEnglish(unittest.TestCase):
    '''tests the french to english translation'''
    def test_fr2en(self):
        '''here comes 4 tests 2 for asserteq 2 for assertNoteq'''
        self.assertNotEqual(french_to_english(0), 0)
        # test when null is given as input the output is null.
        self.assertNotEqual(french_to_english('null'), '')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # test when word is given as input the output is translated.
        self.assertEqual(french_to_english('Route'), 'Road')

unittest.main()
