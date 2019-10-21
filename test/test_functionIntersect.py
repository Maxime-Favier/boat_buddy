import unittest
from fonctions.functionIntersect import functionIntersect


class Intersection(unittest.TestCase):

    def test_droitesParalleles(self):
        # Exeptions droites parallèles
        with self.assertRaises(Exception):
            functionIntersect(1, 0, 1, 5)

    def test_intersection00(self):
        # intersection en 0, 0 quand b et c =0
        pt = functionIntersect(1, 0, -4, 0)
        self.assertTupleEqual(pt, (0, 0))

    def test_intersection12(self):
        # intersection en 1, 2
        pt = functionIntersect(-2, 4, 3, -1)
        self.assertTupleEqual(pt, (1, 2))

    def test_intersection52(self):
        pt = functionIntersect(-5 / 7, 11 / 7, 3 / 5, -5)
        self.assertTupleEqual(pt, (5, -2))


if __name__ == '__main__':
    unittest.main()
