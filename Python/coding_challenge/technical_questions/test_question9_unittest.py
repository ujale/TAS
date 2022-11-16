import question9
import unittest


class UpperCaseConverter(unittest.TestCase):
    def test_convert_string_to_uppercase(self):
        pass

    def uppercase_converter(self, string):
        self.assertEquals(question9.uppercase_converter("biscuit"), "BISCUIT")


if __name__ == '__main__':
    unittest.main()
