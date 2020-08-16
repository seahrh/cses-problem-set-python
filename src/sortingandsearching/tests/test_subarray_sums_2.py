from sortingandsearching.subarray_sums_2 import *


class TestSubarraySums2:
    def test_case_1(self):
        assert solve(target=7, arr=[2, -1, 3, 5, -2]) == 2

    def test_case_2(self):
        assert solve(target=38, arr=[1, 4, 20, 3, 10, 5]) == 2

    def test_case_3(self):
        assert solve(target=0, arr=[0, 0, 0, 0, 0]) == 15
