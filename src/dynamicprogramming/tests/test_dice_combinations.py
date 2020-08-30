from dynamicprogramming.dice_combinations import *


class TestDiceCombinations:
    def test_case_1(self):
        assert solve(1) == 1
        assert solve(2) == 2
        assert solve(3) == 4
        assert solve(4) == 8
        assert solve(5) == 16
        assert solve(6) == 32
        assert solve(7) == 63
        assert solve(8) == 125
        assert solve(9) == 248
