from dynamicprogramming.book_shop import *


class TestBookShop:
    def test_2_items_or_less(self):
        assert solve(budget=10, prices=[4], pages=[5]) == 5
        assert solve(budget=1, prices=[4], pages=[5]) == 0
        assert solve(budget=8, prices=[4, 8], pages=[5, 12]) == 12
        assert solve(budget=7, prices=[4, 8], pages=[5, 12]) == 5
        assert solve(budget=3, prices=[4, 8], pages=[5, 12]) == 0

    def test_case_1(self):
        assert solve(budget=10, prices=[4, 8, 5, 3], pages=[5, 12, 8, 1]) == 13
