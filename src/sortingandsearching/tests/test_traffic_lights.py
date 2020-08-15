from sortingandsearching.traffic_lights import *


class TestTrafficLights:
    def test_case_1(self):
        assert solve(x=8, traffic_lights=[3, 6, 2]) == [5, 3, 3]

    def test_case_2(self):
        assert solve(x=10, traffic_lights=[1, 2, 3, 4, 5]) == [9, 8, 7, 6, 5]

    def test_case_3(self):
        assert solve(x=10, traffic_lights=[5, 4, 3, 2, 1]) == [5, 5, 5, 5, 5]

    def test_case_4(self):
        assert solve(x=10, traffic_lights=[2, 3, 6, 4, 1]) == [8, 7, 4, 4, 4]

    def test_case_5(self):
        assert solve(x=10, traffic_lights=[3, 6, 5, 4, 9]) == [7, 4, 4, 4, 3]

    def test_case_6(self):
        assert solve(x=10, traffic_lights=[9, 3, 6, 1, 4]) == [9, 6, 3, 3, 3]
