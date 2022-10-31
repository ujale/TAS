from Python.unit_testing import task26
import unittest


class Testtask(unittest.TestCase):
    def test_compare_string(self):  # test case
        self.assertEquals(task26.compare_string("boy", "girl"), False)
        self.assertEqual(task26.compare_string("goat", "goat"), True)
        self.assertEqual(task26.compare_string("bill", "goat"), False)

    def test_compare_num(self):  # test case2
        self.assertEqual(task26.compare_num(3, 4), False)
        self.assertEqual(task26.compare_num(8, 8), True)
        self.assertEqual(task26.compare_num(3, 4), False)


if __name__ == '__main__':
    unittest.main()
