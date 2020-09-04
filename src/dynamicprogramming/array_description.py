"""
You know that an array has n integers between 1 and m, and the difference between two adjacent values is at most 1.
Given a description of the array where some values may be unknown,
your task is to count the number of arrays that match the description.
Input
The first input line has two integers n and m: the array size and the upper bound for each value.
The next line has n integers x1,x2,…,xn: the contents of the array. Value 0 denotes an unknown value.
Output
Print one integer: the number of arrays modulo 10^9+7.
Constraints
1≤n≤10^5
1≤m≤100
0≤xi≤m
Example
Input:
3 5
2 0 2
Output:
3
Explanation: The arrays [2,1,2], [2,2,2] and [2,3,2] match the description.

SOLUTION
Bottom-up DP, fill memo table row-wise.
dp[i][j] = number of ways to generate the required array by considering the first i items
and ith item equals j.
Recurrence relation: dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] + dp[i - 1][j + 1] (top 3 cells)
Answer: sum the last row i.e. all possible ways for all N items
Time O(NM)
Space O(NM)
"""
from typing import List


def solve(m: int, arr: List[int]) -> int:
    mod: int = int(1e9) + 7
    n = len(arr)
    dp: List[List[int]] = [[0] * (m + 1) for _ in range(n + 1)]
    # base case: array has only one element
    for j in range(1, m + 1):
        if arr[0] == 0 or arr[0] == j:
            dp[1][j] = 1
    # so start from 2nd array element onwards
    for i in range(2, n + 1):
        for j in range(1, m + 1):
            if arr[i - 1] == 0 or arr[i - 1] == j:
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % mod
                if j + 1 <= m:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j + 1]) % mod
    return sum(dp[n]) % mod


if __name__ == "__main__":
    _, _m = [int(s) for s in input().split()]
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_m, _arr)
    print(_res)
