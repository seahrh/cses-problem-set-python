"""
There are n children who want to go to a Ferris wheel, and your task is to find a gondola for each child.

Each gondola may have one or two children in it, and in addition, the total weight in a gondola may not exceed x.
You know the weight of every child.

What is the minimum number of gondolas needed for the children?

Input
The first input line contains two integers n and x: the number of children and the maximum allowed weight.
The next line contains n integers p1,p2,…,pn: the weight of each child.

Output
Print one integer: the minimum number of gondolas.

Constraints
1≤n≤2⋅10^5
1≤x≤10^9
1≤pi≤x

Example
Input:
4 10
7 2 3 9
Output:
3

See https://cses.fi/problemset/task/1090
SOLUTION
Sort the children by weight. Start with the heaviest child and try to pair with the lightest child.
If the lightest child cannot be added to the gondola, then the heavy child must take the gondola alone,
because there isn't a lighter child.
Time O(N lg N)
Space O(1)
"""
from typing import List


def solve(max_weight: int, weights: List[int]) -> int:
    weights.sort()
    res: int = 0
    i = 0
    j = len(weights) - 1
    curr = weights[j]
    # number of slots currently occupied
    slots = 1
    # i must not meet j, cannot pair with ownself
    while i < j:
        is_heavy_child_taken = False
        if slots == 2:  # successful pairing
            is_heavy_child_taken = True
        elif curr + weights[i] > max_weight:  # heavy child takes the gondola alone
            is_heavy_child_taken = True
        if is_heavy_child_taken:
            res += 1
            j -= 1
            curr = weights[j]
            slots = 1
            continue  # required for the case where the heavy child takes the gondola alone
        curr += weights[i]
        i += 1
        slots += 1
    res += 1  # the remaining unpaired child
    return res


if __name__ == "__main__":
    _, _max = [int(s) for s in input().split()]
    _weights: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_max, _weights)
    print(_res)
