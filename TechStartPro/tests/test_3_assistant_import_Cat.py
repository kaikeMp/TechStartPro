import unittest
import assistant
from database import *

class TestAssistant(unittest.TestCase):
    def test_import_cat(self):
        #Tests whether a list of categories can be imported.
        """We have two lists to test:
                    categories.csv
                    categories2.csv"""
        self.assertEqual(assistant.importCat('categories.csv'), 'i', msg='CAtegories list imported')
        self.assertEqual(assistant.importCat('categories2.csv'), 'i', msg='CAtegories list imported')

if __name__=='__name__':
    unittest.main