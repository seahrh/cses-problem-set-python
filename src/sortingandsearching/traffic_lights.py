"""
There is a street of length x whose positions are numbered 0,1,…,x.
Initially there are no traffic lights, but n sets of traffic lights are added to the street one after another.
Your task is to calculate the length of the longest passage without traffic lights after each addition.
Input
The first input line contains two integers x and n: the length of the street and the number of sets of traffic lights.
Then, the next line contains n integers p1,p2,…,pn: the position of each set of traffic lights.
Each position is distinct.
Output
Print the length of the longest passage without traffic lights after each addition.
Constraints
1≤x≤10^9
1≤n≤2⋅10^5
0<pi<x
Example
Input:
8 3
3 6 2
Output:
5 3 3

Clarifications
- Traffic light is inserted to the right of the position.
- Position 0 is not part of the length

SOLUTION
BST to insert position of traffic lights in O(lg X) time.
Max heap to track longest length
Frequency map to keep counts of lengths
"""
from collections import defaultdict
from heapq import heappush, heappop
from typing import List, Optional, DefaultDict


class Node:
    def __init__(
        self,
        value: int,
        left: Optional["Node"] = None,
        right: Optional["Node"] = None,
        smaller_ancestor: Optional["Node"] = None,
        larger_ancestor: Optional["Node"] = None,
    ):
        self.value = value
        self.left = left
        self.right = right
        self.smaller_ancestor = smaller_ancestor
        self.larger_ancestor = larger_ancestor


def insert_bst(root: Node, node: Node) -> None:
    """Add a node to an UNBALANCED binary search tree."""
    if root is None:
        raise ValueError("Tree must have a root")
    if node.value < root.value:
        node.larger_ancestor = root
        if root.left is None:
            root.left = node
        else:
            insert_bst(root.left, node)
    else:
        node.smaller_ancestor = root
        if root.right is None:
            root.right = node
        else:
            insert_bst(root.right, node)


def solve(x: int, traffic_lights: List[int]) -> List[int]:
    res: List[int] = []
    max_heap: List[int] = []
    freq: DefaultDict[int, int] = defaultdict(int)
    root: Node = Node(0)
    insert_bst(root, Node(x))
    for curr in traffic_lights:
        node: Node = Node(curr)
        insert_bst(root, node)  # Time O(lg X)
        if node.larger_ancestor is None:
            raise ValueError("missing backedge: larger ancestor")
        if node.smaller_ancestor is None:
            raise ValueError("missing backedge: smaller ancestor")
        original = node.larger_ancestor.value - node.smaller_ancestor.value
        left = curr - node.smaller_ancestor.value
        right = node.larger_ancestor.value - curr
        heappush(max_heap, -left)  # Time O(lg X)
        heappush(max_heap, -right)
        freq[original] -= 1
        freq[left] += 1
        freq[right] += 1
        _max = -max_heap[0]
        while freq[_max] == 0:
            heappop(max_heap)  # Time O(lg X) or O(X) if array is shortened?
            _max = -max_heap[0]
        res.append(_max)
    return res


if __name__ == "__main__":
    _x, _ = [int(s) for s in input().split()]
    _traffic_lights: List[int] = [int(s) for s in input().split()]
    _res: List[str] = [str(i) for i in solve(_x, _traffic_lights)]
    print(" ".join(_res))
