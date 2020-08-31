from dynamicprogramming.minimizing_coins import *


class TestMinimizingCoins:
    def test_impossible(self):
        assert solve(target=1, coins=[2]) == -1
        assert solve(target=11, coins=[5, 7]) == -1

    def test_case_1(self):
        assert solve(target=11, coins=[1, 5, 7]) == 3
