from sortingandsearching.reading_books import *


class TestReadingBooks:
    def test_case_1(self):
        assert solve([2, 8, 3]) == 16

    def test_case_2(self):
        assert solve([1000, 1000, 1000, 1000, 1000]) == 5000

    def test_case_3(self):
        assert solve([1, 2, 3, 4, 5, 6, 9, 8, 7, 16]) == 61
