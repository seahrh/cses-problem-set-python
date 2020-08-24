"""
You are given an array of n integers.
Your task is to calculate the median of each window of k elements, from left to right.
The median is the middle element when the elements are sorted.
If the number of elements is even, there are two possible medians and we assume that the median is the smaller of them.
Input
The first input line contains two integers n and k: the number of elements and the size of the window.
Then there are n integers x1,x2,…,xn: the contents of the array.
Output
Print n−k+1 values: the medians.
Constraints
1≤k≤n≤2⋅10^5
1≤xi≤10^9
Example
Input:
8 3
2 4 3 5 8 1 2 1
Output:
3 4 5 5 2 1

SOLUTION
Cannot use heap because deleting (finding) an arbitrary item in heap takes O(N) time.
"""
from collections import Counter
from typing import List


def solve(k: int, arr: List[int]) -> List[int]:
    res: List[int] = []
    window = list(arr[:k])
    window.sort()
    mid = int(k / 2)
    smaller = Counter(window[: mid + 1])
    larger = Counter(window[mid + 1 :])
    smaller_len = mid + 1
    larger_len = k - 1 - mid
    smaller_max = 0
    larger_min = 0
    # res.append(max_heap[0])
    head = 1
    tail = head + k - 1
    while tail < len(arr):
        if arr[tail] >= larger_min:
            # update sorted keys
            larger[arr[tail]] += 1
            larger_len += 1
        else:
            # update sorted keys
            smaller[arr[tail]] += 1
            smaller_len += 1
        prev = head - 1
        if arr[prev] >= larger_min:
            larger[arr[prev]] -= 1
            larger_len -= 1
        else:
            smaller[arr[head - 1]] -= 1
            smaller_len -= 1
        # TODO balance the sets
        if larger_len > smaller_len:
            larger[larger_min] -= 1
            larger_len -= 1
            smaller[larger_min] += 1
            smaller_max = larger_min
            smaller_len += 1
        if smaller_len - larger_len > 1:
            smaller[smaller_max] -= 1
        # TODO add median of current window
        head += 1
        tail = head + k - 1
    return res
