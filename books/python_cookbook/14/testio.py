import unittest
import errno

class TestIO(unittest.TestCase):
    def test_file_not_found(self):
        try:
            f = open('/etc/passwd')
        except IOError as e:
            self.assertEqual(e.errno, errno.ENOENT)
        else:
            self.fail('IOError not raised')
#             pass
            
if __name__ == '__main__':
    unittest.main()