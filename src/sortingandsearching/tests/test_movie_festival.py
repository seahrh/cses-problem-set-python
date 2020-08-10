from sortingandsearching.movie_festival import *


class TestMovieFestival:
    def test_array_length_of_2_or_less(self):
        assert solve([Movie(start=1, end=2)]) == 1
        assert solve([Movie(start=1, end=2), Movie(start=2, end=3)]) == 2
        assert solve([Movie(start=1, end=2), Movie(start=1, end=2)]) == 1

    def test_case_1(self):
        assert (
            solve([Movie(start=3, end=5), Movie(start=4, end=9), Movie(start=5, end=8)])
            == 2
        )

    def test_case_2(self):
        assert (
            solve(
                [
                    Movie(start=6, end=7),
                    Movie(start=4, end=5),
                    Movie(start=8, end=9),
                    Movie(start=2, end=3),
                    Movie(start=10, end=11),
                    Movie(start=1, end=2),
                    Movie(start=9, end=10),
                    Movie(start=3, end=4),
                    Movie(start=5, end=6),
                    Movie(start=7, end=8),
                ]
            )
            == 10
        )

    def test_case_3(self):
        assert (
            solve(
                [
                    Movie(start=404, end=882),
                    Movie(start=690, end=974),
                    Movie(start=201, end=255),
                    Movie(start=800, end=933),
                    Movie(start=525, end=819),
                    Movie(start=457, end=601),
                    Movie(start=461, end=978),
                    Movie(start=832, end=932),
                    Movie(start=699, end=804),
                    Movie(start=795, end=860),
                ]
            )
            == 4
        )
