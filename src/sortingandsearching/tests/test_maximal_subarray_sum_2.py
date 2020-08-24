import pytest
from sortingandsearching.maximal_subarray_sum_2 import *


@pytest.mark.skip(reason="solution requires self balancing BST")
class TestMaximalSubarraySum2:
    def test_array_length_of_2_or_less(self):
        assert solve([1], a=1, b=1) == 1
        assert solve([-1], a=1, b=1) == -1
        assert solve([2, 1], a=1, b=2) == 3
        assert solve([-2, -1], a=1, b=2) == -1

    def test_case_1(self):
        assert solve([-1, 3, -2, 5, 3, -5, 2, 2], a=1, b=8) == 9

    def test_case_2(self):
        assert solve([24, 7, -27, 17, -67, 65, -23, 58, 85, -39], a=1, b=10) == 185

    def test_case_3(self):
        assert solve([99, -59, 31, 83, -79, 64, -20, -87, 40, -31], a=1, b=10) == 154

    def test_case_4(self):
        assert solve([-19, 61, 60, 33, 67, 19, -8, 92, 59, -37], a=1, b=10) == 383

    def test_case_5(self):
        assert solve([-1, 3, -2, 5, 3, -5, 2, 2], a=1, b=2) == 8

    def test_case_6(self):
        assert solve([-22, 0, 78, -48, 94, 68, -7, -73, 8, 62], a=7, b=7) == 163
