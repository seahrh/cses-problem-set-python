from sortingandsearching.concert_tickets import *


class TestConcertTickets:
    def test_1_ticket_only(self):
        assert prices(tickets=[4], customers=[4]) == [4]
        assert prices(tickets=[5], customers=[4]) == [-1]
        assert prices(tickets=[4], customers=[4, 4]) == [4, -1]
        assert prices(tickets=[4], customers=[3, 4]) == [-1, 4]

    def test_case_1(self):
        assert prices(tickets=[5, 3, 7, 8, 5], customers=[4, 8, 3]) == [3, 8, -1]

    def test_case_2(self):
        assert prices(tickets=[5, 3, 7, 8, 5], customers=[6, 8, 3, 8, 7]) == [
            5,
            8,
            3,
            7,
            5,
        ]
