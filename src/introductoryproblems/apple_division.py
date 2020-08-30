"""
There are n apples with known weights.
Divide the apples into two groups so that the difference between the weights of the groups is minimal.
Input
The first input line has an integer n: the number of apples.
The next line has n integers p1,p2,…,pn: the weight of each apple.
Output
Print one integer: the minimum difference between the weights of the groups.
Constraints
1≤n≤20
1≤pi≤10^9
Example
Input:
5
3 2 7 4 1
Output:
1
Explanation: Group 1 has weights 2, 3 and 4 (total weight 9), and group 2 has weights 1 and 7 (total weight 8).

SOLUTION
Membership of the best groups do not follow a sorted ordering, so sorting doesn't help.
Backtracking brute force without pruning; either add current apple to first group or not.
Time O(2^N)
Space O(N): depth of recursive call stack
"""
from typing import List


def _solve(
    arr: List[int], total: int, index: int, first_sum: int, second_sum: int, best: int,
) -> int:
    # Backtracking function must return the best value
    # because the `best` argument is an immutable integer (hence pass by value)
    if index == len(arr):
        return min(best, abs(first_sum - second_sum))
    # compare best scores from the left and right subtrees of the recursion tree
    best = _solve(arr, total, index + 1, first_sum + arr[index], second_sum, best)
    best = _solve(arr, total, index + 1, first_sum, second_sum + arr[index], best)
    return best


def solve(arr: List[int]) -> int:
    return _solve(
        arr, total=sum(arr), index=0, first_sum=0, second_sum=0, best=int(1e9)
    )


if __name__ == "__main__":
    _ = input()
    _arr: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_arr)
    print(_res)
