from sortingandsearching.apartments import *


class TestApartments:
    def test_one_apartment_one_applicant(self):
        assert solve(apartments=[30], applicants=[25], tolerance=5) == 1
        assert solve(apartments=[30], applicants=[5], tolerance=5) == 0

    def test_zero_allocation(self):
        assert solve(apartments=[30, 75], applicants=[45, 80], tolerance=1) == 0

    def test_case_1(self):
        apartments = [30, 60, 75]
        applicants = [60, 45, 80, 60]
        assert solve(apartments, applicants, tolerance=5) == 2
        assert solve(apartments, applicants, tolerance=0) == 1
        assert solve(apartments, applicants, tolerance=15) == 3

    def test_case_2(self):
        assert (
            solve(
                applicants=[37, 62, 56, 69, 34, 46, 10, 86, 16, 49],
                apartments=[50, 95, 47, 43, 9, 62, 83, 71, 71, 7],
                tolerance=0,
            )
            == 1
        )

    def test_case_3(self):
        assert (
            solve(
                applicants=[90, 41, 20, 39, 49, 21, 35, 31, 74, 86],
                apartments=[14, 24, 24, 7, 82, 85, 82, 4, 60, 95],
                tolerance=10,
            )
            == 6
        )

    def test_case_4(self):
        assert (
            solve(
                applicants=[59, 5, 65, 15, 42, 81, 58, 96, 50, 1],
                apartments=[18, 59, 71, 65, 97, 83, 80, 68, 92, 67],
                tolerance=1000,
            )
            == 10
        )
