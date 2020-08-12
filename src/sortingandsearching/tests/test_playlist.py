from sortingandsearching.playlist import *


class TestPlaylist:
    def test_array_length_of_2_or_less(self):
        assert solve([1]) == 1
        assert solve([2, 1]) == 2
        assert solve([1, 1]) == 1

    def test_case_1(self):
        assert solve([1, 2, 1, 3, 2, 7, 4, 2]) == 5

    def test_case_2(self):
        assert solve([2, 3, 4, 5, 2, 10, 9, 8, 6, 1]) == 9
