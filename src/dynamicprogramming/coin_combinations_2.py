"""
Consider a money system consisting of n coins. Each coin has a positive integer value.
Your task is to calculate the number of distinct ordered ways you can produce a money sum x using the available coins.
For example, if the coins are {2,3,5} and the desired sum is 9, there are 3 ways:
2+2+5
3+3+3
2+2+2+3
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
3

SOLUTION
Bottom up DP: state is given by first C coins (exploit requirement in sorted order), target sum
Memoization table has shape (#coins, target). Fill table row by row.
Time O(X)
Space O(X)
"""
from typing import List


def solve(target: int, coins: List[int]) -> int:
    mod: int = int(1e9) + 7
    memo: List[List[int]] = [[0] * (target + 1) for _ in range(len(coins))]
    coins.sort()
    # if sum equals coin value, initialize as 1 (sum - coin == 0)
    for i in range(len(coins)):
        memo[i][0] = 1
    min_coin = coins[0]
    for i in range(len(coins)):
        for j in range(min_coin, target + 1):
            # carry over the output from top cell
            if i - 1 >= 0:
                memo[i][j] = max(memo[i][j], memo[i - 1][j])
            c = coins[i]
            if j - c >= 0:
                memo[i][j] += memo[i][j - c]
                memo[i][j] = memo[i][j] % mod
    return memo[-1][target]


if __name__ == "__main__":
    _, _target = [int(s) for s in input().split()]
    _coins: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_target, _coins)
    print(_res)
