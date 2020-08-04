from sortingandsearching.ferris_wheel import *


class TestFerrisWheel:
    def test_array_length_of_1(self):
        assert gondolas(10, weights=[1]) == 1
        assert gondolas(10, weights=[10]) == 1

    def test_array_length_of_2(self):
        assert gondolas(10, weights=[1, 2]) == 1
        assert gondolas(10, weights=[5, 5]) == 1
        assert gondolas(10, weights=[10, 1]) == 2
        assert gondolas(10, weights=[10, 10]) == 2

    def test_case_1(self):
        assert gondolas(10, weights=[7, 2, 3, 9]) == 3
