import unittest

from programs.一元二次方程 import *
from 算法与程序框图 import *


class MyTestCase(unittest.TestCase):
    def test_get_root(self):
        self.assertEqual(get_root("1,2,3", "2,3,5"), (1, 1))  # add assertion here

    def test_is_prime(self):
        self.assertTrue(is_prime(11))
        self.assertFalse(is_prime(9))

    def test_estimate(self):
        self.assertEqual(get_estimate(), (1.4140625, 1.41796875))

    def test_tri_area(self):
        self.assertEqual(get_triangle_area(3, 4, 5), 6)

    def test_is_tri(self):
        self.assertTrue(is_triangle(3, 4, 5))

    def test_x2(self):
        self.assertTrue(get_x2_root(1, 4, 4))

    def test_array(self):
        self.assertEqual(get_array_sum(), 5050)

    def test_year(self):
        self.assertEqual(get_year(), 2014)


if __name__ == '__main__':
    unittest.main()
