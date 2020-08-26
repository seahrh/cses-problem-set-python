"""
You are given an array of n integers, and your task is to find two values (at distinct positions) whose sum is x.
Input
The first input line has two integers n and x: the array size and the target sum.
The second line has n integers a1,a2,…,an: the array values.
Output
Print two integers: the positions of the values. If there are several solutions, you may print any of them.
If there are no solutions, print IMPOSSIBLE.
Constraints
1≤n≤2⋅10^5
1≤x,ai≤10^9
Example
Input:
4 8
2 7 5 1
Output:
2 4

SOLUTION
Sort the array then search for the pair from both ends.
Time O(N lg N)
Space O(N): requirement to return the positions, hence need to store the positions after sorting.
Otherwise, only O(1) space required.
"""
from typing import List, Tuple, NamedTuple, Set


class Item(NamedTuple):
    value: int
    position: int  # one-indexed as per requirement


def solve(arr: List[int], target: int) -> Set[Tuple[int, int]]:
    res: Set[Tuple[int, int]] = set()
    if len(arr) < 2:
        return res
    items: List[Item] = [Item(value=a, position=i + 1) for i, a in enumerate(arr)]
    items.sort()
    i = 0
    j = len(items) - 1
    while i < j:
        _sum = items[i].value + items[j].value
        if _sum == target:
            pos_i = items[i].position
            pos_j = items[j].position
            if pos_i <= pos_j:
                res.add((pos_i, pos_j))
            else:
                res.add((pos_j, pos_i))
            i += 1
            j -= 1
            continue
        if _sum < target:
            i += 1
            continue
        j -= 1
    return res


if __name__ == "__main__":
    _, x = [int(s) for s in input().split()]
    _arr: List[int] = [int(s) for s in input().split()]
    _res: Set[Tuple[int, int]] = solve(_arr, target=x)
    if len(_res) == 0:
        print("IMPOSSIBLE")
    else:
        for left, right in _res:
            print(f"{left} {right}")
