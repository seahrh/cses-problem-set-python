"""
You are given an array containing n positive integers.
Your task is to divide the array into k subarrays so that the maximum sum in a subarray is as small as possible.
Input
The first input line contains two integers n and k: the size of the array and the number of subarrays in the division.
The next line contains n integers x1,x2,…,xn: the contents of the array.
Output
Print one integer: the maximum sum in a subarray in the optimal division.
Constraints
1≤n≤2⋅10^5
1≤k≤n
1≤xi≤10^9
Example
Input:
5 3
2 4 7 3 5
Output:
8
Explanation: An optimal division is [2,4],[7],[3,5] where the sums of the subarrays are 6,7,8.
The largest sum is the last sum 8.

SOLUTION
Binary search on the range of `max_sum` between `lo` and `hi`.
Smallest subarray has length 1, so smallest sum `lo` is the max element.
Largest subarray is the entire array, so largest sum `hi` is the sum of the array.
If #subarrays is greater than k (subarrays are too short), increase max_sum.
If #subarrays is less than or equals k (subarrays are too long), decrease max_sum.

Time O(N lg X)
Space O(1)
"""
from typing import List


def _is_greater_than_k(max_sum: int, k: int, arr: List[int]) -> bool:
    """Return True if the number of subarrays is greater than k."""
    subarray_count = 0
    _sum = 0
    for i in range(len(arr)):  # Time O(N)
        _sum += arr[i]
        if _sum > max_sum:
            subarray_count += 1
            if subarray_count == k and i != len(arr) - 1:
                return True
            _sum = arr[i]
    subarray_count += 1  # remember to add the last subarray!
    return subarray_count > k


def solve(k: int, arr: List[int]) -> int:
    lo = 1
    hi = 0
    for a in arr:
        lo = max(lo, a)
        hi += a
    res: int = hi
    while lo <= hi:  # Time O(lg X . N)
        mid = int(lo / 2 + hi / 2)
        if _is_greater_than_k(max_sum=mid, k=k, arr=arr):
            lo = mid + 1
            continue
        # found a possible solution, keep going left to find a smaller max_sum.
        res = mid
        hi = mid - 1
    return res


if __name__ == "__main__":
    _, _k = [int(s) for s in input().split()]
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_k, _arr)
    print(_res)
