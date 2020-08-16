from sortingandsearching.nearest_smaller_values import *


class TestNearestSmallerValues:
    def test_case_1(self):
        assert solve([2, 5, 1, 4, 8, 3, 2, 5]) == [0, 1, 0, 3, 4, 3, 3, 7]

    def test_case_2(self):
        assert solve([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_case_3(self):
        assert solve([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    def test_case_4(self):
        assert solve([1, 10, 9, 8, 7, 6, 5, 4, 3, 2]) == [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
