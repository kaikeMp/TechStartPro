import unittest
import assistant


class TestAssistant(unittest.TestCase):
    def test_add_product(self):
        #['TV', 'philco', '500.0', 'Guitarra,Teclado']
        #list = ['TV', 'philco', '500.0', 'Guitarra,Teclado']
        #Tests whether a product can be add to database.
        self.assertEqual(assistant.add_product(['TV', 'philco', '500.0', 'Guitarra,Teclado']), 'i')


if __name__=='__name__':
    unittest.main