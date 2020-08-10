from sortingandsearching.sum_of_two_values import *


class TestSumOfTwoValues:
    def test_array_length_of_2_or_less(self):
        assert solve([2], target=4) == set()
        assert solve([2, 2], target=4) == {(1, 2)}
        assert solve([2, 2], target=3) == set()

    def test_no_pair_found(self):
        assert solve([2, 7, 5, 1], target=4) == set()
        assert solve([1, 2, 3], target=2) == set()
        assert solve([1, 3, 2], target=6) == set()

    def test_case_1(self):
        assert solve([2, 7, 5, 1], target=8) == {(2, 4)}

    def test_case_2(self):
        assert solve([2, 1, 3], target=3) == {(1, 2)}

    def test_case_3(self):
        assert solve([4, 5, 3], target=8) == {(2, 3)}
