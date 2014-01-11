import unittest
from rlist import rlist


def add_one(x): return x+1
def add(x, y): return x + y

class RListTest(unittest.TestCase):
    def setUp(self):
        self.list = rlist([1,2,3])
        return

    def test_map(self):
        self.assertEqual([2, 3, 4], self.list.map(add_one))

    def test_reduce(self):
        self.assertEqual(6, self.list.reduce(add))

    def test_any(self):
        self.assertTrue(self.list.any(lambda x: x > 2))
        self.assertFalse(self.list.any(lambda x: x > 3))

    def test_filter(self):
        self.assertEqual([1,2], self.list.filter(lambda x: x != 3))

    def test_all(self):
        self.assertTrue(self.list.all(lambda x: x > 0))
        self.assertFalse(self.list.all(lambda x: x > 2))

    def test_max(self):
        self.assertEqual(3, self.list.max())

    def test_min(self):
        self.assertEqual(1, self.list.min())

    def test_sum(self):
        self.assertEqual(6, self.list.sum())

    def test_zip(self):
        self.assertEqual([(1, "a"), (2, "b"), (3, "c")], self.list.zip(["a", "b", "c"]))

    def test_size(self):
        self.assertEqual(3, self.list.size())

    def test_find(self):
        self.assertEqual(3, self.list.find(lambda x:x == 3))
        self.assertEqual(None, self.list.find(lambda x:x == 4))
