import unittest
import leap_year

class TestLeapYear(unittest.TestCase):
    def test_multiple_of_4(self):
        self.assertEqual(leap_year.leap_year(2024), "Leap year")

if __name__ == "__main__":
    unittest.main(verbosity=2) 