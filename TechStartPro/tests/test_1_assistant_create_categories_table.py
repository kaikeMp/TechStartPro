import unittest
import assistant
from database import *

class TestAssistant(unittest.TestCase):
    def test_create_cat_table(self):
        #Test if a categories table is created on database
        #If a '.db' file already exists, it must be deleted.
        self.assertEqual(assistant.create_cat_table(), 'i', msg='Categories table created')

if __name__=='__name__':
    unittest.main
