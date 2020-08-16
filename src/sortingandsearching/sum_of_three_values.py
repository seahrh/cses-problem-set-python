"""
You are given an array of n integers, and your task is to find three values (at distinct positions) whose sum is x.
Input
The first input line has two integers n and x: the array size and the target sum.
The second line has n integers a1,a2,…,an: the array values.
Output
Print three integers: the positions of the values.
If there are several solutions, you may print any of them. If there are no solutions, print IMPOSSIBLE.
Constraints
1=n=5000
1=x,ai=10^9
Example
Input:
4 8
2 7 5 1
Output:
1 3 4

SOLUTION
Sort the array and run through all indices of a possible first element of a triplet.
For each possible first element, make a bi-directional sweep of the remaining part of the array.
Time O(N^2)
Space O(N): store the positions in the original unsorted array, else O(1) space.
"""
from typing import Tuple, List, Optional, NamedTuple


class Item(NamedTuple):
    value: int
    position: int


def solve(target: int, arr: List[int]) -> Optional[Tuple[int, int, int]]:
    items: List[Item] = [Item(v, i + 1) for i, v in enumerate(arr)]
    items.sort()
    for i in range(len(items) - 2):  # maintain two slots ahead for j, k
        j = i + 1
        k = len(items) - 1
        while j < k:
            _sum = items[i].value + items[j].value + items[k].value
            if _sum == target:
                return items[i].position, items[j].position, items[k].position
            if _sum < target:
                j += 1
                continue
            k -= 1
    return None


if __name__ == "__main__":
    _, _target = [int(s) for s in input().split()]
    _arr: List[int] = [int(s) for s in input().split()]
    _res: Optional[Tuple[int, int, int]] = solve(_target, _arr)
    if _res is None:
        print("IMPOSSIBLE")
    else:
        print(f"{_res[0]} {_res[1]} {_res[2]}")
