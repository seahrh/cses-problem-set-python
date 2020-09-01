"""
There are n books, and Kotivalo and Justiina are going to read them all.
For each book, you know the time it takes to read it.
They both read each book from beginning to end, and they cannot read a book at the same time.
What is the minimum total time required?
Input
The first input line has an integer n: the number of books.
The second line has n integers t1,t2,…,tn: the time required to read each book.
Output
Print one integer: the minimum total time.
Constraints
1≤n≤2⋅10^5
1≤ti≤10^9
Example
Input:
3
2 8 3
Output:
16

SOLUTION
Sort books by reading time. This ensures they cannot read a book at the same time.
So get a cumulative sum of reading times from both ends of the sorted books.
Terminate when sum(left) >= sum(right).
The result is the sum of the two partitions. There is no idle time even if one partition is longer than the other.
Because the other reader can start reading the other partition as soon as she is done with the first partition.
However this is not true if a partition contains only a single book as one book cannot be subdivided.
So the first reader who finishes her partition is forced to wait for the second reader to finish.
Time O(N lg N)
Space O(N): store the sum of reading times from the right end
"""
from typing import List


def solve(books: List[int]) -> int:
    books.sort()
    right_sum: List[int] = [0] * len(books)
    _sum = 0
    for i in range(len(books) - 1, -1, -1):
        _sum += books[i]
        right_sum[i] = _sum
    _sum = 0
    # invariant: left partition can be empty but right partition must have at least 1 book
    for i in range(len(books) - 1):
        _sum += books[i]
        if _sum >= right_sum[i + 1]:
            return _sum + right_sum[i + 1]
    return books[-1] * 2


if __name__ == "__main__":
    _ = input()
    _books: List[int] = [int(s) for s in input().split()]
    _res: int = solve(_books)
    print(_res)
