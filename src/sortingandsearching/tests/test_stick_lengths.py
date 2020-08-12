from sortingandsearching.stick_lengths import *


class TestStickLengths:
    def test_array_length_of_2_or_less(self):
        assert solve([9]) == 0
        assert solve([2, 1]) == 1

    def test_case_1(self):
        assert solve([2, 3, 1, 5, 2]) == 5

    def test_case_2(self):
        assert solve([1, 4, 7, 8, 10, 3, 2, 5, 6, 9]) == 25
