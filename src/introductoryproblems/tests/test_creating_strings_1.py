from introductoryproblems.creating_strings_1 import *


class TestCreatingStrings1:
    def test_string_length_of_2_or_less(self):
        assert solve("a") == {"a"}
        assert solve("aa") == {"aa"}
        assert solve("ab") == {"ab", "ba"}

    def test_case_1(self):
        assert solve("aabac") == {
            "aaabc",
            "aaacb",
            "aabac",
            "aabca",
            "aacab",
            "aacba",
            "abaac",
            "abaca",
            "abcaa",
            "acaab",
            "acaba",
            "acbaa",
            "baaac",
            "baaca",
            "bacaa",
            "bcaaa",
            "caaab",
            "caaba",
            "cabaa",
            "cbaaa",
        }
