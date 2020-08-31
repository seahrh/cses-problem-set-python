"""
You are given an integer n. On each step, you may subtract from it any one-digit number that appears in it.
How many steps are required to make the number equal to 0?
Input
The only input line has an integer n.
Output
Print one integer: the minimum number of steps.
Constraints
1≤n≤10^6
Example
Input:
27
Output:
5
Explanation: An optimal solution is 27→20→18→10→9→0.

SOLUTION
dp[x] = minimum number of operations to go from x to zero.
When considering a number x, for each digit in the decimal representation of x, we can try to remove it.
The transition is therefore: dp[x] = min of dp[x-d] for each digit d of x
Time O(N)
Space O(N)
"""
from typing import List


def solve(n: int) -> int:
    memo: List[int] = [n] * (n + 1)
    memo[0] = 0
    for i in range(1, n + 1):
        remainder = i
        while remainder != 0:  # Time O(1) because max 7 digits
            d = remainder % 10
            if remainder - d >= 0:
                memo[i] = min(memo[i], memo[i - d] + 1)
            remainder = int(remainder / 10)  # chop off the last digit
    return memo[n]


if __name__ == "__main__":
    _n = int(input())
    _res: int = solve(_n)
    print(_res)
