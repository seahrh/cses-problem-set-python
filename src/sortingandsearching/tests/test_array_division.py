from sortingandsearching.array_division import *


class TestArrayDivision:
    def test_array_length_of_2_or_less(self):
        assert solve(k=1, arr=[2]) == 2
        assert solve(k=1, arr=[2, 1]) == 3
        assert solve(k=2, arr=[2, 1]) == 2

    def test_case_1(self):
        assert solve(k=1, arr=[2, 4, 7, 3, 5]) == 21
        assert solve(k=2, arr=[2, 4, 7, 3, 5]) == 13
        assert solve(k=3, arr=[2, 4, 7, 3, 5]) == 8
        assert solve(k=4, arr=[2, 4, 7, 3, 5]) == 7
        assert solve(k=5, arr=[2, 4, 7, 3, 5]) == 7
