from introductoryproblems.permutations import *


class TestPermutations:
    def test_case_1(self):
        assert solve(5) == [2, 4, 1, 3, 5]

    def test_case_2(self):
        assert solve(3) == []
