from introductoryproblems.two_sets import *


class TestTwoSets:
    def test_case_1(self):
        assert solve(7) == ([7, 6, 1], [5, 4, 3, 2])

    def test_case_2(self):
        assert solve(6) == ([], [])
