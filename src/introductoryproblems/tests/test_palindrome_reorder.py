from introductoryproblems.palindrome_reorder import *


class TestPalindromeReorder:
    def test_case_1(self):
        assert solve("AAAACACBA") == "AACABACAA"
        assert solve("MMAAD") == "MADAM"
        assert solve("MMAADDD") == "MADDDAM"
        assert solve("MMAAAD") is None
