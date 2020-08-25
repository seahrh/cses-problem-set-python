"""
You are given an array of n integers.
Modify the array so that it is increasing, i.e., every element is at least as large as the previous element.
On each turn, you may increase the value of any element by one. What is the minimum number of turns required?
Input
The first input line contains an integer n: the size of the array.
Then, the second line contains n integers x1,x2,…,xn: the contents of the array.
Output
Print the minimum number of turns.
Constraints
1≤n≤2⋅10^5
1≤xi≤10^9
Example
Input:
5
3 2 5 1 7
Output:
5

SOLUTION
Time O(N)
Space O(1)
"""
from typing import List


def solve(arr: List[int]) -> int:
    res: int = 0
    prev = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < prev:
            res += prev - arr[i]
            continue
        prev = arr[i]
    return res


if __name__ == "__main__":
    _ = input()
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_arr)
    print(_res)
