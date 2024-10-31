import unittest

def add(a,b):
    return a+b

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-1, -1), -2)
    
    def test_add_positive_and_negative(self):
        self.assertEqual(add(-1, 5), 4)
    
    def test_add_zero(self):
        self.assertEqual(add(0, 10), 10)
        self.assertEqual(add(10, 0), 10)
    
    def test_add_floats(self):
        self.assertAlmostEqual(add(1.5, 2.7), 4.2, places=7)

if __name__ == '__main__':
    unittest.main()