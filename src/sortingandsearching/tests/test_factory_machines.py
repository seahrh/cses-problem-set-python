from sortingandsearching.factory_machines import *


class TestFactoryMachines:
    def test_array_length_of_2_or_less(self):
        assert solve(target=3, machines=[2]) == 6
        assert solve(target=2, machines=[2, 1]) == 2
        assert solve(target=1, machines=[2, 1]) == 1

    def test_case_1(self):
        assert solve(target=7, machines=[3, 2, 5]) == 8

    def test_case_2(self):
        assert solve(target=10, machines=[6, 5, 1, 2, 1, 5, 10, 4, 6, 6]) == 4

    def test_case_3(self):
        assert solve(target=10, machines=[6, 6, 4, 3, 4, 9, 3, 2, 6, 10]) == 6

    def test_case_4(self):
        assert solve(target=10, machines=[5, 4, 10, 7, 8, 4, 1, 8, 9, 2]) == 5
