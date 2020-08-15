from sortingandsearching.tasks_and_deadlines import *


class TestTasksAndDeadlines:
    def test_case_1(self):
        assert solve([Task(6, 10), Task(8, 15), Task(5, 12)]) == 2

    def test_case_2(self):
        assert (
            solve(
                [
                    Task(1, 6),
                    Task(1, 4),
                    Task(1, 8),
                    Task(1, 2),
                    Task(1, 10),
                    Task(1, 1),
                    Task(1, 9),
                    Task(1, 3),
                    Task(1, 5),
                    Task(1, 7),
                ]
            )
            == 0
        )
