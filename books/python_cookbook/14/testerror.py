import unittest
from testconversion import parse_int
class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        try:
            r = parse_int('N/A')
        except ValueError as e:
            self.assertEqual(type(e), ValueError)
            
if __name__ == '__main__':
    unittest.main()