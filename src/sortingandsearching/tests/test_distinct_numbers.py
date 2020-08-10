from sortingandsearching.distinct_numbers import *


class TestDistinctNumbers:
    def test_array_length_of_2_or_less(self):
        assert count_distinct([]) == 0
        assert count_distinct([1]) == 1
        assert count_distinct([1, 1]) == 1
        assert count_distinct([2, 1]) == 2

    def test_case_1(self):
        assert count_distinct([2, 3, 2, 2, 3]) == 2

    def test_case_2(self):
        assert count_distinct([7, 4, 10, 9, 6, 1, 8, 2, 5, 3]) == 10

    def test_case_3(self):
        assert count_distinct([5, 9, 5, 5, 10, 9, 3, 1, 8, 8]) == 6
