from dynamicprogramming.coin_combinations_2 import *


class TestCoinCombinations2:
    def test_multiples_of_1(self):
        assert solve(target=1, coins=[1]) == 1
        assert solve(target=2, coins=[1]) == 1
        assert solve(target=3, coins=[1]) == 1

    def test_multiples_of_1_and_2(self):
        assert solve(target=1, coins=[1, 2]) == 1
        assert solve(target=2, coins=[1, 2]) == 2
        assert solve(target=3, coins=[1, 2]) == 2
        assert solve(target=4, coins=[1, 2]) == 3

    def test_case_1(self):
        assert solve(target=1, coins=[2, 3, 5]) == 0
        assert solve(target=2, coins=[2, 3, 5]) == 1
        assert solve(target=3, coins=[2, 3, 5]) == 1
        assert solve(target=4, coins=[2, 3, 5]) == 1
        assert solve(target=5, coins=[2, 3, 5]) == 2
        assert solve(target=6, coins=[2, 3, 5]) == 2
        assert solve(target=7, coins=[2, 3, 5]) == 2
        assert solve(target=8, coins=[2, 3, 5]) == 3
        assert solve(target=9, coins=[2, 3, 5]) == 3
