import unittest
from main import greet

class TestGreet(unittest.TestCase):
    def test_greet_output(self):
        # This test just ensures greet() runs without error
        greet()

if __name__ == "__main__":
    unittest.main()