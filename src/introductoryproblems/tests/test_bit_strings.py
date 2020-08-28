from introductoryproblems.bit_strings import *


class TestBitStrings:
    def test_case_1(self):
        assert solve(1) == 2
        assert solve(3) == 8
