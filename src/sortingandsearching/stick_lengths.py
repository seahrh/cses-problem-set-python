"""
There are n sticks with some lengths. Your task is to modify the sticks so that each stick has the same length.
You can either lengthen and shorten each stick.
Both operations cost x where x is the difference between the new and original length.
What is the minimum total cost?
Input
The first input line contains an integer n: the number of sticks.
Then there are n integers: p1,p2,…,pn: the lengths of the sticks.
Output
Print one integer: the minimum total cost.

Constraints
1≤n≤2⋅10^5
1≤pi≤10^9
Example
Input:
5
2 3 1 5 2
Output:
5

SOLUTION: Sort the array, use the median to divide the array into two equal-sized partitions.
Time O(N lg N)
Space O(1)
"""
from typing import List


def solve(arr: List[int]) -> int:
    if len(arr) == 0:
        raise ValueError("array must not be empty")
    arr.sort()
    median = arr[int(len(arr) / 2)]
    cost: int = 0
    for a in arr:
        cost += abs(median - a)
    return cost


if __name__ == "__main__":
    _ = input()
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_arr)
    print(_res)
