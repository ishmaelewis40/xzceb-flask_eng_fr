import unittest
from translator import english_to_french
from translator import french_to_english


class TestEnglishToFrench(unittest.TestCase):

    def test_english_to_french(self):
        self.assertNotEqual(english_to_french(''), '')
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')


    def test_french_to_english_translate(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('bonjour'), 'bonjour')
        self.assertNotEqual(french_to_english(''), '')

   

if __name__ == '__main__':
    unittest.main()