from dynamicprogramming.array_description import *


class TestArrayDescription:
    def test_array_length_of_2_or_less(self):
        assert solve(m=5, arr=[2]) == 1
        assert solve(m=5, arr=[0]) == 5
        assert solve(m=5, arr=[2, 3]) == 1
        assert solve(m=5, arr=[1, 0]) == 2
        assert solve(m=5, arr=[2, 0]) == 3
        assert solve(m=5, arr=[0, 1]) == 2
        assert solve(m=5, arr=[0, 2]) == 3
        assert solve(m=5, arr=[0, 0]) == 13

    def test_case_1(self):
        assert solve(m=5, arr=[2, 0, 2]) == 3
