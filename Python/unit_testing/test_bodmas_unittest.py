import bodmas
import unittest # This is imported from the standard unittest library

class TestBodmas(unittest.TestCase):        # Test suite
    def test_addition(self):  # test case
        self.assertEquals(bodmas.addition(3, 1), 4)
        self.assertEquals(bodmas.addition(-5, 1), -4)

    def test_subtration(self):  # test case
        self.assertEquals(bodmas.subtraction(3, 1), 2)
        self.assertEquals(bodmas.subtraction(-5, 1), -6)

if __name__ == '__main__':
    unittest.main()