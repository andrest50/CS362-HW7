import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_multiple_of_3(self):
        self.assertEqual(fizzbuzz.fizzbuzz(18), "Fizz")

if __name__ == '__main__':
    unittest.main(verbosity=2)