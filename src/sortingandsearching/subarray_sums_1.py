"""
Given an array of n positive integers, your task is to count the number of subarrays having sum x.
Input
The first input line has two integers n and x: the size of the array and the target sum x.
The next line has n integers a1,a2,…,an: the contents of the array.
Output
Print one integer: the required number of subarrays.
Constraints
1≤n≤2⋅10^5
1≤x,ai≤10^9
Example
Input:
5 7
2 4 1 2 7
Output:
3

SOLUTION
Sliding window
Time O(N)
Space O(1)
"""
from typing import List


def solve(target: int, arr: List[int]) -> int:
    i, j, _sum = 0, 0, 0
    res: int = 0
    while j < len(arr) or _sum >= target:  # handle the last subarray!
        if _sum < target:
            _sum += arr[j]
            j += 1
            continue
        if _sum == target:
            res += 1
        _sum -= arr[i]
        i += 1
    return res


if __name__ == "__main__":
    _, _target = [int(s) for s in input().split()]
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_target, _arr)
    print(_res)
