from sortingandsearching.ferris_wheel import *


class TestFerrisWheel:
    def test_array_length_of_1(self):
        assert solve(10, weights=[1]) == 1
        assert solve(10, weights=[10]) == 1

    def test_both_children_can_fit_in_the_gondola(self):
        assert solve(10, weights=[1, 2]) == 1
        assert solve(10, weights=[5, 5]) == 1

    def test_second_child_cannot_fit_in_the_gondola(self):
        assert solve(10, weights=[1, 10]) == 2

    def test_case_1(self):
        assert solve(10, weights=[7, 2, 3, 9]) == 3

    def test_case_2(self):
        assert solve(10, weights=[1, 9, 1, 9]) == 2

    def test_case_3(self):
        assert solve(2, weights=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]) == 5

    def test_case_4(self):
        assert solve(2, weights=[1, 2, 2, 1, 1, 2, 2, 2, 2, 2]) == 9

    def test_case_5(self):
        assert solve(10, weights=[10, 9, 7, 10, 9, 8, 5, 6, 6, 5]) == 9

    def test_case_6(self):
        assert solve(15, weights=[9, 8, 8, 9, 10, 8, 5, 8, 7, 10]) == 8

    def test_case_7(self):
        assert solve(20, weights=[5, 9, 6, 5, 8, 9, 10, 6, 5, 6]) == 5
