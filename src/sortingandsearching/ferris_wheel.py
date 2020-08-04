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
Pick the children from lightest to heaviest.
Time O(N lg N)
Space O(1)
"""
from typing import List


def gondolas(max_weight: int, weights: List[int]) -> int:
    weights.sort()
    res: int = 0
    curr: int = 0
    for w in weights:
        if curr > 0:
            res += 1
            if curr + w <= max_weight:
                curr = 0
                continue
            # 2nd child cannot fit, so take the next gondola
        elif max_weight - w < w:
            # empty gondola, remaining capacity is smaller than all subsequent (heavier) children
            curr = 0
            res += 1
            continue
        curr = w
    # edge case: only 1 child
    if curr > 0:
        res += 1
    return res
