"""
Given an array of n integers, count the number of subarrays where the sum of values is divisible by n.
Input
The first input line has an integer n: the size of the array.
The next line has n integers a1,a2,…,an: the contents of the array.
Output
Print one integer: the required number of subarrays.
Constraints
1≤n≤2⋅10^5
−10^9≤ai≤10^9
Example
Input:
5
3 1 2 7 4
Output:
1

SOLUTION
Time O(N)
Space O(N): store the counts of remainders

See
- https://www.geeksforgeeks.org/count-sub-arrays-sum-divisible-k/
- https://en.wikipedia.org/wiki/Triangular_number
"""
from typing import List, Set


def solve(arr: List[int]) -> int:
    res: int = 0
    n = len(arr)
    # Map remainder to count of prefix subarrays
    counts: List[int] = [0] * n
    # sum of prefix subarray
    _sum = 0
    for a in arr:
        _sum += a
        # Take modulus twice as sum can be negative
        counts[(_sum % n + n) % n] += 1
    for c in counts:
        if c > 1:
            # the number of ways in which the subarrays can be combined to form longer subarrays
            # follows the Triangle Number, sum of 1 to (C-1) inclusive.
            # Given by the formula N(N + 1) / 2
            # where N is (C-1) because the first prefix subarray is not included.
            res += int(c * (c - 1) / 2)
    # add array elements which equals N
    res += counts[0]
    return res


if __name__ == "__main__":
    _ = input()
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_arr)
    print(_res)
