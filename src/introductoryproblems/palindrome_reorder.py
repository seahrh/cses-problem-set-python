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

SOLUTION
Find the single character that has odd count.
Palindrome cannot have more than 1 char with odd count e.g. ___AB___  where A and B have odd count.
Time O(N)
Space O(N)
"""
from typing import Optional, Set


def solve(s: str) -> Optional[str]:
    odd_counts: Set[str] = set()
    left: str = ""
    for c in s:
        if c not in odd_counts:
            odd_counts.add(c)
        else:
            # so far this char has even count, so add it to the left/right partitions
            odd_counts.remove(c)
            left += c
    if len(odd_counts) > 1:
        return None
    mid: str = next(iter(odd_counts), "")  # default empty string
    right: str = left[::-1]
    return left + mid + right


if __name__ == "__main__":
    _s = input()
    _res: Optional[str] = solve(_s)
    if _res is None:
        print("NO SOLUTION")
    else:
        print(_res)
