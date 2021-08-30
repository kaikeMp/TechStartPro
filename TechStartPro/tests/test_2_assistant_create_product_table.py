import unittest
import assistant
from database import *

class TestAssistant(unittest.TestCase):
    def test_create_product_table(self):
        # Test if a product table is created on database
        # If a '.db' file already exists, it must be deleted.
        self.assertEqual(assistant.create_product_table(), 'i', msg='Product table created')
if __name__=='__name__':
    unittest.main