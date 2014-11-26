
import unittest

# 이해를 돕기 위한 간단한 함수
def parse_int(s):
    return int(s)

class TestConversion(unittest.TestCase):
    def test_bad_int(self):
        self.assertRaisesRegex(ValueError, 'invalid literal2 .*', 
                               parse_int, 'N/A')
        
if __name__ == '__main__':
    unittest.main()