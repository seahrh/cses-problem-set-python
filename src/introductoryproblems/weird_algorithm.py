"""
Consider an algorithm that takes as input a positive integer n.
If n is even, the algorithm divides it by two, and if n is odd, the algorithm multiplies it by three and adds one.
The algorithm repeats this, until n is one. For example, the sequence for n=3 is as follows:
3→10→5→16→8→4→2→1
Your task is to simulate the execution of the algorithm for a given value of n.
Input
The only input line contains an integer n.
Output
Print a line that contains all values of n during the algorithm.
Constraints
1≤n≤106
Example
Input:
3
Output:
3 10 5 16 8 4 2 1
"""
from typing import List


def solve(n: int) -> List[int]:
    res: List[int] = [n]
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = n * 3 + 1
        res.append(n)
    return res


if __name__ == "__main__":
    _n = int(input())
    _res: List[str] = [str(x) for x in solve(_n)]
    print(" ".join(_res))
