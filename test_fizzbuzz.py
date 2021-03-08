import unittest
import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_multiple_of_3(self):
        self.assertEqual(fizzbuzz.fizzbuzz(18), "Fizz")

    def test_multiple_of_5(self):
        self.assertEqual(fizzbuzz.fizzbuzz(40), "Buzz")

    def test_multiple_of_3_and_5(self):
        self.assertEqual(fizzbuzz.fizzbuzz(60), "FizzBuzz")

    def test_other_number(self):
        self.assertEqual(fizzbuzz.fizzbuzz(87), "87")

if __name__ == '__main__':
    unittest.main(verbosity=2)