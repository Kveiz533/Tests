import unittest
import math
from rectangle import *
from triangle import *
from circle import *

class RectangleTestCase(unittest.TestCase):
    def test_zero_area_perimeter(self):
        res = rc_area(10, 0)
        self.assertEqual(res, 0)

        res = rc_area(0, 78)
        self.assertEqual(res, 0)

        res = rc_perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_not_zero_area_perimeteruare_mul(self):
        res = rc_area(10, 1)
        self.assertEqual(res, 10)

        res = rc_area(52, 52)
        self.assertEqual(res, 2704)

        res = rc_perimeter(10, 2)
        self.assertEqual(res, 24)

    def test_rect_is_square(self):
        res = is_square(10, 1)
        self.assertFalse(res)

        res = is_square(10, -10)
        self.assertFalse(res)

        res = is_square(10, 10)
        self.assertTrue(res)


class TriangleTestCase(unittest.TestCase):
    def test_zero_area_perimeter(self):
        res = tr_area(10, 0)
        self.assertEqual(res, 0)

        res = tr_area(0, 78)
        self.assertEqual(res, 0)

        res = tr_perimeter(0, 0, 0)
        self.assertEqual(res, 0)

    def test_not_zero_area_perimeteruare_mul(self):
        res = tr_area(3, 6)
        self.assertEqual(res, 9)

        res = tr_area(8, 10)
        self.assertEqual(res, 40)

        res = tr_perimeter(10, 2, 12)
        self.assertEqual(res, 24)

    def test_tr_is_rectangular(self):
        res = is_rectangular(10, 1, 5)
        self.assertFalse(res)

        res = is_rectangular(3, -4, 5)
        self.assertFalse(res)

        res = is_rectangular(3, 4, 5)
        self.assertTrue(res)


class Circle(unittest.TestCase):
    def test_zero_area_perimeter(self):
        res = cr_area(0)
        self.assertEqual(res, 0)

        res = cr_perimeter(0)
        self.assertEqual(res, 0)

    def test_not_zero_area_perimeteruare_mul(self):
        res = cr_area(3)
        self.assertEqual(res, math.pi * 9)

        res = cr_area(8)
        self.assertEqual(res, math.pi * 64)

        res = cr_perimeter(10)
        self.assertEqual(res, math.pi * 20)
