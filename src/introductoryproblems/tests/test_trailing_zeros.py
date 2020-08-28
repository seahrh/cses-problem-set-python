from introductoryproblems.trailing_zeros import *


class TestTrailingZeros:
    def test_case_1(self):
        assert solve(1) == 0
        assert solve(19) == 3
        assert solve(20) == 4
        assert solve(21) == 4
