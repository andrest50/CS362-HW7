import unittest
import leap_year

class TestLeapYear(unittest.TestCase):
    def test_multiple_of_4(self):
        self.assertEqual(leap_year.leap_year(2024), "Leap year")

    def test_multiple_of_100(self):
        self.assertEqual(leap_year.leap_year(2100), "Not a leap year")

if __name__ == "__main__":
    unittest.main(verbosity=2) 