"""
You are given a DNA sequence: a string consisting of characters A, C, G, and T.
Find the longest repetition in the sequence. This is a maximum-length substring containing only one type of character.
Input
The only input line contains a string of n characters.
Output
Print one integer: the length of the longest repetition.
Constraints
1≤n≤10^6
Example
Input:
ATTCGGGA
Output:
3

SOLUTION
Time O(N)
Space O(1)
"""


def solve(s: str) -> int:
    curr = 1
    res: int = curr
    prev: str = s[0]
    for i in range(1, len(s)):
        if s[i] == prev:
            curr += 1
            res = max(res, curr)
            continue
        prev = s[i]
        curr = 1
    return res


if __name__ == "__main__":
    _s = input()
    _res: int = solve(_s)
    print(_res)
