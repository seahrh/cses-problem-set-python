from sortingandsearching.towers import *


class TestTowers:
    def test_array_length_of_2_or_less(self):
        assert solve([1]) == 1
        assert solve([2, 1]) == 1
        assert solve([1, 2]) == 2

    def test_case_1(self):
        assert solve([3, 8, 2, 1, 5]) == 2

    def test_case_2(self):
        assert solve([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 10

    def test_case_3(self):
        assert solve([10, 4, 5, 9, 4, 10, 2, 7, 4, 6]) == 4

    def test_case_4(self):
        assert solve([1, 2, 3, 4, 5, 8, 7, 1, 9, 1]) == 7

    def test_case_5(self):
        assert solve([10, 9, 8, 7, 6, 10, 4, 3, 2, 1]) == 2
