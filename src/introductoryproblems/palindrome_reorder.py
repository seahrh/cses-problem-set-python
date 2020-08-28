"""
Given a string, your task is to reorder its letters in such a way that it becomes a palindrome
(i.e., it reads the same forwards and backwards).
Input
The only input line has a string of length n consisting of characters A–Z.
Output
Print a palindrome consisting of the characters of the original string. You may print any valid solution.
If there are no solutions, print "NO SOLUTION".
Constraints
1≤n≤10^6
Example
Input:
AAAACACBA
Output:
AACABACAA
"""
from collections import defaultdict
from typing import Optional, DefaultDict


def solve(s: str) -> Optional[str]:
    counts: DefaultDict[str, int] = defaultdict(int)
    odd_count = 0
    for c in s:
        counts[c] += 1
        if counts[c] % 2 == 1:
            odd_count += 1
        else:
            odd_count -= 1
    if odd_count > 1:
        return None
    first: str = ""
    second: str = ""
    mid: str = ""
    for code in range(ord("A"), ord("Z") + 1):
        c = chr(code)
        if counts[c] % 2 == 1:
            mid = c
            continue
        frag: str = c * int(counts[c] / 2)
        first += frag
        second = frag + second
    return first + mid + second


if __name__ == "__main__":
    _s = input()
    _res: Optional[str] = solve(_s)
    if _res is None:
        print("NO SOLUTION")
    else:
        print(_res)
