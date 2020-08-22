from sortingandsearching.subarray_divisibility import *


class TestSubarrayDivisibility:
    def test_array_length_of_2_or_less(self):
        assert solve([2]) == 1
        assert solve([-2]) == 1
        assert solve([0]) == 1
        assert solve([0, 0]) == 3
        assert solve([2, 2]) == 3
        assert solve([2, 1]) == 1
        assert solve([1, 1]) == 1
        assert solve([-1, 1]) == 1
        assert solve([-2, -2]) == 3
        assert solve([-2, -1]) == 1
        assert solve([-1, -1]) == 1

    def test_case_1(self):
        assert solve([3, 1, 2, 7, 4]) == 1

    def test_case_2(self):
        assert solve([3, -1, -2, -7, 4]) == 3
