
import unittest
from josephus import josephus


class TestJosephus(unittest.TestCase):
    def testJosephus(self):
        # tuple로 해줘야 dictionary의 key값이 될 수 있다. immutable 이기 때문
        problems = [(6, 3), (40, 3), (3, 1)]
        answers = [(3, 5), (11, 26), (2, 3)]

        d = {}
        for k, v in zip(problems, answers):
            d[k] = v

        for k, v in d.items():
            N, K = k
            test_answer = josephus(N, K)
            self.assertEqual(tuple(test_answer), v)
            
if __name__ == '__main__':
    unittest.main()