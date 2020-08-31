from dynamicprogramming.removing_digits import *


class TestRemovingDigits:
    def test_case_1(self):
        assert solve(27) == 5
        assert solve(20) == 4
        assert solve(18) == 3
        assert solve(10) == 2
        assert solve(9) == 1
