"""
You are given all numbers between 1,2,…,n except one. Your task is to find the missing number.
Input
The first input line contains an integer n.
The second line contains n−1 numbers. Each number is distinct and between 1 and n (inclusive).
Output
Print the missing number.
Constraints
2≤n≤2⋅10^5
Example
Input:
5
2 3 1 5
Output:
4

SOLUTION
Missing number = Expected sum - Actual sum
Expected sum is the Triangle Number given by N(N + 1) / 2
Time O(N)
Space O(1)
"""
from typing import List


def solve(arr: List[int]) -> int:
    n = len(arr) + 1
    expected = int(n * (n + 1) / 2)
    actual = sum(arr)
    return expected - actual


if __name__ == "__main__":
    _ = input()
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_arr)
    print(_res)
