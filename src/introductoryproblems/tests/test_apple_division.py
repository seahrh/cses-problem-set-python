from introductoryproblems.apple_division import *


class TestAppleDivision:
    def test_unsorted_weights(self):
        assert solve([3, 1, 1]) == 1

    def test_case_1(self):
        assert solve([3, 2, 7, 4, 1]) == 1

    def test_case_2(self):
        assert solve([603, 324, 573, 493, 659, 521, 654, 70, 718, 257]) == 2
