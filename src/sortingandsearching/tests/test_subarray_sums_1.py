from sortingandsearching.subarray_sums_1 import *


class TestSubarraySums1:
    def test_array_length_of_2_or_less(self):
        assert solve(target=9, arr=[1]) == 0
        assert solve(target=9, arr=[9]) == 1
        assert solve(target=9, arr=[10]) == 0
        assert solve(target=9, arr=[1, 2]) == 0
        assert solve(target=9, arr=[1, 8]) == 1
        assert solve(target=9, arr=[1, 10]) == 0
        assert solve(target=9, arr=[9, 9]) == 2

    def test_case_1(self):
        assert solve(target=7, arr=[2, 4, 1, 2, 7]) == 3

    def test_case_2(self):
        assert solve(target=7, arr=[1, 1, 1, 1, 1, 1, 1, 1, 3, 4]) == 4
