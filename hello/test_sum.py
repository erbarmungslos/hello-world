from unittest import TestCase, main
from test import sum

class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(sum(5,2), 7)
       # self.fail()


if __name__ == '__main__':
    main()