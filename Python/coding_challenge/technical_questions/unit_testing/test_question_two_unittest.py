from Python.coding_challenge.technical_questions.unit_testing import question2
import unittest


class TestPower(unittest.TestCase):
    def test_power_of_number(self):
        self.assertEquals(question2.power_of_number(2, 3), 8)
        self.assertEquals(question2.power_of_number(5, 3), 125)


if __name__ == '__main__':
    unittest.main()
