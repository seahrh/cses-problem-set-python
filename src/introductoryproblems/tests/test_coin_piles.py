from introductoryproblems.coin_piles import *


class TestCoinPiles:
    def test_case_1(self):
        assert solve(0, 0)
        assert not solve(1, 8)
        assert solve(3, 6)
        assert solve(2, 1)
        assert not solve(2, 2)
        assert solve(3, 3)
