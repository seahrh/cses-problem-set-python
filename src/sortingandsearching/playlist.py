"""
You are given a playlist of a radio station since its establishment. The playlist has a total of n songs.
What is the longest sequence of successive songs where each song is unique?
Input
The first input line contains an integer n: the number of songs.
The next line has n integers k1,k2,…,kn: the id number of each song.
Output
Print the length of the longest sequence of unique songs.
Constraints
1≤n≤2⋅10^5
1≤ki≤10^9
Example
Input:
8
1 2 1 3 2 7 4 2
Output:
5

SOLUTION: Sliding window
Grow the window on the right side when new item is found.
Shrink window from the left side until the "first" duplicate is no longer in the window.
Time O(N)
Space O(N)
"""
from typing import List, Set


def solve(arr: List[int]) -> int:
    if len(arr) == 0:
        raise ValueError("array must not be empty")
    window: Set[int] = set()
    _max: int = 0
    i, j = 0, 0
    while j < len(arr):
        # grow the window on the right side
        if arr[j] not in window:
            window.add(arr[j])
            j += 1
            # only need to update max when the window is growing
            _max = max(_max, len(window))
            continue
        # shrink the window from the left side
        window.remove(arr[i])
        i += 1
    return _max


if __name__ == "__main__":
    _ = input()
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_arr)
    print(_res)
