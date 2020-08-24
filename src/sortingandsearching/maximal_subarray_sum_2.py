"""
Given an array of n integers, find the maximum sum of values in a contiguous subarray with length between a and b.
Input
The first input line has three integers n, a and b: the size of the array and the minimum and maximum subarray length.
The second line has n integers x1,x2,…,xn: the array values.
Output
Print one integer: the maximum subarray sum.
Constraints
1≤n≤2⋅10^5
1≤a≤b≤n
−10^9≤xi≤10^9
Example
Input:
8 1 2
-1 3 -2 5 3 -5 2 2
Output:
8

SOLUTION
TODO Incomplete solution, requires self balancing BST
See https://discuss.codechef.com/t/help-with-maximum-subarray-sum-ii-from-cses/73404
"""
import sys
from typing import List


def solve(arr: List[int], a: int, b: int) -> int:
    if len(arr) == 0:
        raise ValueError("array must not be empty")
    _max: int = -sys.maxsize
    _sum, _len, i, j = 0, 0, 0, 0
    while j < len(arr):
        _sum += arr[j]
        _len = j - i + 1
        if _len > b:
            _sum -= arr[i]
            i += 1
        # no more updates to _sum after this point
        if a <= _len:
            _max = max(_max, _sum)
        j += 1
    while i < len(arr) and _len >= a:
        _sum -= arr[i]
        _max = max(_max, _sum)
        i += 1
        _len -= 1
    return _max


if __name__ == "__main__":
    _, _a, _b = [int(s) for s in input().split()]
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_arr, _a, _b)
    print(_res)
