"""
Consider a money system consisting of n coins. Each coin has a positive integer value.
Produce a sum of money x using the available coins in such a way that the number of coins is minimal.
For example, if the coins are {1,5,7} and the desired sum is 11, an optimal solution is 5+5+1 which requires 3 coins.
Input
The first input line has two integers n and x: the number of coins and the desired sum of money.
The second line has n distinct integers c1,c2,…,cn: the value of each coin.
Output
Print one integer: the minimum number of coins. If it is not possible to produce the desired sum, print −1.
Constraints
1≤n≤100
1≤x≤10^6
1≤ci≤10^6
Example
Input:
3 11
1 5 7
Output:
3

SOLUTION
We look at the last coin added to get sum x, say it has value v.
We need dp[x-v] coins to get value x-v, and 1 coin for value v.
Therefore we need dp[x-v]+1 coins if we are to use a coin with value v.
Time O(X)
Space O(X)

See https://codeforces.com/blog/entry/70018
"""
from bisect import bisect_right
from typing import List


def solve(target: int, coins: List[int]) -> int:
    coins.sort()
    impossible = target + 1
    memo: List[int] = [impossible] * (target + 1)
    # bottom up from base case
    for c in coins:
        if c > target:
            break
        memo[c] = 1
    min_coin = coins[0]
    for i in range(min_coin + 1, target + 1):
        if memo[i] != impossible:  # base case already filled
            continue
        best = impossible
        # i is larger than this left partition of coins
        # target of zero is impossible
        tail = bisect_right(coins, i)
        for j in range(tail):
            c = coins[j]
            best = min(best, memo[i - c] + 1)
        memo[i] = best
    if memo[target] == impossible:
        return -1
    return memo[target]


if __name__ == "__main__":
    _, _target = [int(s) for s in input().split()]
    _coins: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_target, _coins)
    print(_res)
