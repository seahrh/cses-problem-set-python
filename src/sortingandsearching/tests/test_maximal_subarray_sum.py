from sortingandsearching.maximal_subarray_sum import *


class TestMaximalSubarraySum:
    def test_array_length_of_2_or_less(self):
        assert solve([1]) == 1
        assert solve([-1]) == -1
        assert solve([2, 1]) == 3
        assert solve([-2, -1]) == -1

    def test_case_1(self):
        assert solve([-1, 3, -2, 5, 3, -5, 2, 2]) == 9

    def test_case_2(self):
        assert solve([24, 7, -27, 17, -67, 65, -23, 58, 85, -39]) == 185

    def test_case_3(self):
        assert solve([99, -59, 31, 83, -79, 64, -20, -87, 40, -31]) == 154

    def test_case_4(self):
        assert solve([-19, 61, 60, 33, 67, 19, -8, 92, 59, -37]) == 383
