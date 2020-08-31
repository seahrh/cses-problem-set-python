"""
Consider a money system consisting of n coins. Each coin has a positive integer value.
Calculate the number of distinct ways you can produce a money sum x using the available coins.
For example, if the coins are {2,3,5} and the desired sum is 9, there are 8 ways:
2+2+5
2+5+2
5+2+2
3+3+3
2+2+2+3
2+2+3+2
2+3+2+2
3+2+2+2
Input
The first input line has two integers n and x: the number of coins and the desired sum of money.
The second line has n distinct integers c1,c2,…,cn: the value of each coin.
Output
Print one integer: the number of ways modulo 10^9+7.
Constraints
1≤n≤100
1≤x≤10^6
1≤ci≤10^6
Example
Input:
3 9
2 3 5
Output:
8
"""
from bisect import bisect_right
from typing import List


def solve(target: int, coins: List[int]) -> int:
    mod: int = int(1e9) + 7
    memo: List[int] = [0] * (target + 1)
    coins.sort()
    tail = bisect_right(coins, target)
    for i in range(tail):
        c = coins[i]
        memo[c] = 1
    min_coin = coins[0]
    for i in range(min_coin + 1, target + 1):
        tail = bisect_right(coins, i)
        for j in range(tail):
            c = coins[j]
            memo[i] += memo[i - c]
            memo[i] = memo[i] % mod
    return memo[target]


if __name__ == "__main__":
    _, _target = [int(s) for s in input().split()]
    _coins: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_target, _coins)
    print(_res)
