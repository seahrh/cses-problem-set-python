from sortingandsearching.concert_tickets import *


class TestConcertTickets:
    def test_1_ticket_only(self):
        assert solve(tickets=[4], customers=[4]) == [4]
        assert solve(tickets=[5], customers=[4]) == [-1]
        assert solve(tickets=[4], customers=[4, 4]) == [4, -1]
        assert solve(tickets=[4], customers=[3, 4]) == [-1, 4]

    def test_case_1(self):
        assert solve(tickets=[5, 3, 7, 8, 5], customers=[4, 8, 3]) == [3, 8, -1]

    def test_case_2(self):
        assert solve(tickets=[5, 3, 7, 8, 5], customers=[6, 8, 3, 8, 7]) == [
            5,
            8,
            3,
            7,
            5,
        ]

    def test_case_3(self):
        assert solve(
            tickets=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            customers=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ) == [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    def test_case_4(self):
        assert solve(
            tickets=[9, 3, 9, 6, 6, 8, 6, 2, 6, 3],
            customers=[9, 5, 4, 6, 3, 9, 3, 3, 5, 2],
        ) == [9, 3, 3, 6, 2, 9, -1, -1, -1, -1]
