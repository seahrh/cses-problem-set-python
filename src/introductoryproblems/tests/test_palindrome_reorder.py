from introductoryproblems.palindrome_reorder import *


class TestPalindromeReorder:
    def test_case_1(self):
        assert solve("AAAACACBA") == "AAACBCAAA"
        assert solve("MMAAD") == "AMDMA"
        assert solve("MMAAAD") is None
