import unittest
from redKnight import *

class MyTestCase(unittest.TestCase):

    def test_checkBreakCondition(self):
        movmentsTMP = {
            (-2, 1): "UR",
            (0, 2): "R",
            (2, 1): "LR",
            (-2, -1): "UL",
            (0, -2): "L",
            (2, -1): "LL"
        }
        for item in movmentsTMP:
            x,y = item
            actual = isAvailable(x,y)
            expected = True
            self.assertEqual(expected, actual)

    def test_checkBreakCondition2(self):
        expected = False
        actual = isAvailable(4, 1)
        self.assertEqual(expected, actual)

    def test_checkBreakCondition3(self):
        expected = False
        actual = isAvailable(1, 5)
        self.assertEqual(expected, actual)

    def test_checkBreakCondition4(self):
        expected = True
        actual = isAvailable(4, 8)
        self.assertEqual(expected, actual)

    def test_sortPath1(self):
        path = ["UL"]
        self.assertEqual(path, sortInOrder(path))

    def test_sortPath2(self):
        path = ["UL", "UR"]
        expected = path
        self.assertEqual(expected, sortInOrder(path))
    def testSearchShortenPath_right(self):
        actual = printShortestPath(7,0,2,0,6)
        expected = "2\nR R"
        self.assertEqual(actual, expected)

    def testSearchShortenPath_left(self):
        actual = printShortestPath(7, 0, 6, 0, 2)
        expected = "2\nL L"
        self.assertEqual(actual, expected)

    def testSearchShortenPath_up(self):
        actual = printShortestPath(7, 6,0,  2,0 )
        expected = "2\nUL UR"
        self.assertEqual(actual, expected)

    def testSearchShortenPath_down(self):
        actual = printShortestPath(7, 0,0, 4,0 )
        expected = "2\nLR LL"
        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
