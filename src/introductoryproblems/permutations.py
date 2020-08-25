"""
A permutation of integers 1,2,…,n is called beautiful if there are no adjacent elements whose difference is 1.
Given n, construct a beautiful permutation if such a permutation exists.
Input
The only input line contains an integer n.
Output
Print a beautiful permutation of integers 1,2,…,n.
If there are several solutions, you may print any of them. If there are no solutions, print "NO SOLUTION".
Constraints
1≤n≤10^6
Example 1
Input:
5
Output:
4 2 5 3 1
Example 2
Input:
3
Output:
NO SOLUTION

SOLUTION
Pick all the even numbers first then the odd numbers.
Time O(N)
Space O(N): store the output, else O(1) if the output is printed.
"""
from typing import List


def solve(n: int) -> List[int]:
    res: List[int] = []
    if n == 1:
        return [1]
    if n < 4:
        return res
    for i in range(2, n + 1, 2):
        res.append(i)
    for i in range(1, n + 1, 2):
        res.append(i)
    return res


if __name__ == "__main__":
    _n = int(input())
    _res: List[str] = [str(x) for x in solve(_n)]
    if len(_res) == 0:
        print("NO SOLUTION")
    else:
        print(" ".join(_res))
