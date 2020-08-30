"""
Your task is to count the number of ways to construct sum n by throwing a dice one or more times.
Each throw produces an outcome between 1 and 6.
For example, if n=3, there are 4 ways:
1+1+1
1+2
2+1
3
Input
The only input line has an integer n.
Output
Print the number of ways modulo 10^9+7.
Constraints
1≤n≤106
Example
Input:
3
Output:
4

SOLUTION
Bottom up DP approach: adding a die roll to previous entries
f[x] = f[x-1] + f[x-2] + f[x-3] + f[x-4] + f[x-5] + f[x-6]
Time O(N)
Space O(N): memo array
"""
from typing import List


def solve(n: int) -> int:
    mod: int = int(1e9 + 7)
    memo: List[int] = [0] * (n + 1)
    # required to initialize f(1) through f(6); single die to get sum
    memo[0] = 1
    for i in range(n + 1):
        for j in range(1, 7):
            if i - j >= 0:
                memo[i] += memo[i - j]
                memo[i] = memo[i] % mod
    return memo[n]


if __name__ == "__main__":
    _n = int(input())
    _res: int = solve(_n)
    print(_res)
