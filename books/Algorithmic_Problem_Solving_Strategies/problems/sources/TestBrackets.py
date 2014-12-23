import unittest
from brackets import well_matched


class TestBrackets(unittest.TestCase):
    def testBrackets(self):
        s = '''()()
({[}])
({}[(){}])
)
}
}}}
{}[]()
{[([()])]}
{[([()])]'''
        problems = s.split('\n')
        # answers = [True, False, True, False, False, False, True, True, False]
        answers = ['YES', 'NO', 'YES', 'NO', 'NO', 'NO', 'YES', 'YES', 'NO']
        d = {}
        for k, v in zip(problems, answers):
            d[k] = v

        for k, v in d.items():
            test_answer = well_matched(k)
            self.assertEqual(test_answer, v)

if __name__ == '__main__':
    unittest.main()