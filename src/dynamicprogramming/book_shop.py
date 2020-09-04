"""
You are in a book shop which sells n different books. You know the price and number of pages of each book.
You have decided that the total price of your purchases will be at most x.
What is the maximum number of pages you can buy? You can buy each book at most once.
Input
The first input line contains two integers n and x: the number of books and the maximum total price.
The next line contains n integers h1,h2,…,hn: the price of each book.
The last line contains n integers s1,s2,…,sn: the number of pages of each book.
Output
Print one integer: the maximum number of pages.
Constraints
1≤n≤1000
1≤x≤10^5
1≤hi,si≤1000
Example
Input:
4 10
4 8 5 3
5 12 8 1
Output:
13
Explanation: You can buy books 1 and 3. Their price is 4+5=9 and the number of pages is 5+8=13.

SOLUTION
0/1 Knapsack problem
Bottom-up Dynamic programming (tabulation) works only if weights and capacity are positive integers.
dp[i][j] = maximum number of pages for considering only the first i books and budget j.
dp[i][j] = max(did not take current item, take current item)
Time O(NB)
Space O(NB)

See https://www.youtube.com/watch?v=nLmhmB6NzcM
"""
from typing import List


def solve(budget: int, prices: List[int], pages: List[int]) -> int:
    n = len(prices)
    # Fill table row-wise. Rows are items [0, N] and columns are budget [0, B]
    dp: List[List[int]] = [[0] * (budget + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, budget + 1):
            item = i - 1
            remainder = j - prices[item]
            add_item = 0
            if remainder >= 0:
                add_item = dp[i - 1][remainder] + pages[item]
            # decide whether to add ith item or not
            dp[i][j] = max(dp[i - 1][j], add_item)
    return dp[-1][-1]


if __name__ == "__main__":
    _, _budget = [int(s) for s in input().split()]
    _prices: List[int] = [int(s) for s in input().split()]
    _pages: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_budget, _prices, _pages)
    print(_res)
