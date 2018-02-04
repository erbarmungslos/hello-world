from unittest import TestCase
from test import sum

class TestSum(TestCase):
    def test_sum(self):
        self.assertEqual(sum(5,2), 7)
        self.fail()
