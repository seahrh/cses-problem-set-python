"""
Given an array of n integers, your task is to find the maximum sum of values in a contiguous, nonempty subarray.
Input
The first input line has an integer n: the size of the array.
The second line has n integers x1,x2,…,xn: the array values.
Output
Print one integer: the maximum subarray sum.

Constraints
1≤n≤2⋅105
−109≤xi≤109
Example
Input:
8
-1 3 -2 5 3 -5 2 2
Output:
9
SOLUTION
If sum drops below zero, that subsequence will not contribute to the maximal subarray
since max is reduced by adding the negative sum.
If the array contains all negative numbers, sum is reset for each element,
effectively picking the smallest negative number.
Time O(N)
Space O(1)
"""
import sys
from typing import List


def solve(arr: List[int]) -> int:
    if len(arr) == 0:
        raise ValueError("array must not be empty")
    _max: int = -sys.maxsize
    _sum = 0
    for a in arr:
        _sum += a
        _max = max(_max, _sum)
        if _sum < 0:
            _sum = 0
    return _max


if __name__ == "__main__":
    _ = input()
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_arr)
    print(_res)
