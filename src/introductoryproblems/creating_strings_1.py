"""
Given a string, your task is to generate all different strings that can be created using its characters.
Input
The only input line has a string of length n. Each character is between a–z.
Output
First print an integer k: the number of strings. Then print k lines: the strings in alphabetical order.
Constraints
1≤n≤8
Example
Input:
aabac
Output:
20
aaabc
aaacb
aabac
aabca
aacab
aacba
abaac
abaca
abcaa
acaab
acaba
acbaa
baaac
baaca
bacaa
bcaaa
caaab
caaba
cabaa
cbaaa

SOLUTION
Backtracking without pruning: enumerate all possibilities.
Time O(N * N!): N recursive calls.
Inserting the character takes factorial time because there are N! permutations (partials).
Space O(N): recursive call stack
"""
from typing import List, Set


def _solve(remainder: str, result: Set[str]) -> None:
    if len(remainder) == 1:  # base case
        result.add(remainder)
        return
    head = remainder[0]
    # pass a new empty set to store the partial solutions
    partials: Set[str] = set()
    _solve(remainder[1:], partials)
    for p in partials:
        for i in range(len(p) + 1):
            result.add(p[:i] + head + p[i:])


def solve(s: str) -> Set[str]:
    res: Set[str] = set()
    _solve(s, res)
    return res


if __name__ == "__main__":
    _s = input()
    _res: List[str] = list(solve(_s))
    print(len(_res))
    _res.sort()
    for line in _res:
        print(line)
