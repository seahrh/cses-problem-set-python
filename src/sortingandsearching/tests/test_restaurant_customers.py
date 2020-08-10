from sortingandsearching.restaurant_customers import *


class TestRestaurantCustomers:
    def test_max_1_customer_in_restaurant(self):
        assert solve([(1, 2)]) == 1
        assert solve([(8, 12), (1, 4), (5, 7)]) == 1
        assert (
            solve(
                [
                    (1, 2),
                    (3, 4),
                    (5, 6),
                    (7, 8),
                    (9, 10),
                    (11, 12),
                    (13, 14),
                    (15, 16),
                    (17, 18),
                    (19, 20),
                ]
            )
            == 1
        )

    def test_case_1(self):
        assert solve([(5, 8), (2, 4), (3, 9)]) == 2

    def test_case_2(self):
        assert solve([(6, 7), (5, 8), (2, 4), (3, 9)]) == 3

    def test_case_3(self):
        assert (
            solve(
                [
                    (1, 20),
                    (2, 19),
                    (3, 18),
                    (4, 17),
                    (5, 16),
                    (6, 15),
                    (7, 14),
                    (8, 13),
                    (9, 12),
                    (10, 11),
                ]
            )
            == 10
        )

    def test_case_4(self):
        assert (
            solve(
                [
                    (45, 84),
                    (2, 43),
                    (34, 64),
                    (42, 99),
                    (50, 80),
                    (12, 21),
                    (72, 82),
                    (39, 86),
                    (33, 89),
                    (47, 97),
                ]
            )
            == 7
        )

    def test_case_5(self):
        assert solve([(1, 10), (2, 4), (3, 5), (7, 9)]) == 3
