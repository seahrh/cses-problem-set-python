"""
Given an array of n integers, your task is to count the number of subarrays having sum x.
Input
The first input line has two integers n and x: the size of the array and the target sum x.
The next line has n integers a1,a2,…,an: the contents of the array.
Output
Print one integer: the required number of subarrays.
Constraints
1≤n≤2⋅10^5
−10^9≤x,ai≤10^9
Example
Input:
5 7
2 -1 3 5 -2
Output:
2

SOLUTION
Trick to find "non-prefix" subarrays that do not contain the 1st element.
Traverse array from left to right. There are three regions containing the sums: PREFIX, TARGET, UNKNOWN.
CURRENT_SUM is the sum of elements from index 0 to current index.
If there is a prefix sum matching (CURRENT_SUM - TARGET), then there is a "middle" subarray with TARGET sum.
Time O(N)
Space O(N)

See https://www.geeksforgeeks.org/find-subarray-with-given-sum-in-array-of-integers/
"""
from typing import List, Set, Dict


def solve(target: int, arr: List[int]) -> int:
    # Map prefix sum to the tail index of the prefix
    prefix_sums: Dict[int, Set[int]] = {}
    res: int = 0
    _sum = 0
    for i in range(len(arr)):
        _sum += arr[i]
        if _sum == target:  # prefix subarray
            res += 1
        ps = _sum - target
        if ps in prefix_sums:
            # number of "non-prefix" subarrays ending at current index
            res += len(prefix_sums[ps])
        if _sum not in prefix_sums:
            prefix_sums[_sum] = {i}
        else:
            prefix_sums[_sum].add(i)
    return res


if __name__ == "__main__":
    _, _target = [int(s) for s in input().split()]
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_target, _arr)
    print(_res)
