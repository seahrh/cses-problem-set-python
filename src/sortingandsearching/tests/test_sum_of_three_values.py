from sortingandsearching.sum_of_three_values import *


class TestSumOfThreeValues:
    def test_array_length_of_2_or_less(self):
        assert solve(target=3, arr=[1]) is None
        assert solve(target=3, arr=[1, 2]) is None

    def test_case_1(self):
        assert solve(target=8, arr=[2, 7, 5, 1]) == (4, 1, 3)

    def test_case_2(self):
        assert solve(target=5, arr=[1, 3, 2]) is None

    def test_case_3(self):
        assert solve(target=6, arr=[1, 3, 2]) == (1, 3, 2)

    def test_case_4(self):
        assert solve(target=3, arr=[2, 1, 1, 2, 2, 1, 1]) == (2, 3, 7)

    def test_case_5(self):
        assert solve(target=4, arr=[1, 1, 2, 2, 1, 2, 1]) == (1, 2, 6)
