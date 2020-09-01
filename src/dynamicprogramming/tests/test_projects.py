from dynamicprogramming.projects import *


class TestProjects:
    def test_single_project(self):
        assert solve([Project(start=2, end=4, reward=4)]) == 4

    def test_mutually_exclusive_projects(self):
        assert (
            solve(
                [Project(start=2, end=4, reward=4), Project(start=3, end=6, reward=6)]
            )
            == 6
        )

    def test_case_1(self):
        assert (
            solve(
                [
                    Project(start=2, end=4, reward=4),
                    Project(start=3, end=6, reward=6),
                    Project(start=5, end=7, reward=3),
                ]
            )
            == 7
        )
        assert (
            solve(
                [
                    Project(start=2, end=4, reward=4),
                    Project(start=3, end=6, reward=6),
                    Project(start=6, end=8, reward=2),
                    Project(start=5, end=7, reward=3),
                ]
            )
            == 7
        )
