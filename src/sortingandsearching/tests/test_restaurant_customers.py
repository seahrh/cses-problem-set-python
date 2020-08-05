from sortingandsearching.restaurant_customers import *


class TestRestaurantCustomers:
    def test_max_1_customer_in_restaurant(self):
        assert max_customers([(1, 2)]) == 1
        assert max_customers([(8, 12), (1, 4), (5, 7)]) == 1

    def test_case_1(self):
        assert max_customers([(5, 8), (2, 4), (3, 9)]) == 2

    def test_case_2(self):
        assert max_customers([(6, 7), (5, 8), (2, 4), (3, 9)]) == 3
