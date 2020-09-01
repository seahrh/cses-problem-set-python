"""
You are given n cubes in a certain order, and your task is to build towers using them.
Whenever two cubes are one on top of the other, the upper cube must be smaller than the lower cube.
You must process the cubes in the given order.
You can always either place the cube on top of an existing tower, or begin a new tower.
What is the minimum possible number of towers?
Input
The first input line contains an integer n: the number of cubes.
The next line contains n integers k1,k2,…,kn: the sizes of the cubes.
Output
Print one integer: the minimum number of towers.
Constraints
1≤n≤2⋅10^5
1≤ki≤10^9
Example
Input:
5
3 8 2 1 5
Output:
2

SOLUTION
Put the towers in a sorted array.
Start with the first tower and grow this array iteratively (maintain the sorted property).
Time O(N lg N): binary search where to insert in sorted array
Space O(N): store the towers in an array
"""
from bisect import bisect_right
from typing import List


def solve(arr: List[int]) -> int:
    if len(arr) == 0:
        raise ValueError("array must not be empty")
    towers: List[int] = [arr[0]]
    for i in range(1, len(arr)):
        # Time O(lg N): get the nearest item on the right that is larger than arr[i]
        j = bisect_right(towers, arr[i])
        if j == len(towers):
            towers.append(arr[i])
            continue
        towers[j] = arr[i]
    return len(towers)


if __name__ == "__main__":
    _ = input()
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_arr)
    print(_res)
