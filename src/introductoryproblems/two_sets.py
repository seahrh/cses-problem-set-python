"""
Your task is to divide the numbers 1,2,…,n into two sets of equal sum.
Input
The only input line contains an integer n.
Output
Print "YES", if the division is possible, and "NO" otherwise.
After this, if the division is possible, print an example of how to create the sets.
First, print the number of elements in the first set followed by the elements themselves in a separate line,
and then, print the second set in a similar way.
Constraints
1≤n≤10^6
Example 1
Input:
7
Output:
YES
4
1 2 4 7
3
3 5 6
Example 2
Input:
6
Output:
NO

SOLUTION
There must be a solution if the sum is even (no solution if the sum is odd).
The "budget" for each subset is half of the sum. Loop N..1 to partition the set.
If the budget of the first subset is not enough to cover the current number, add it to the other subset.
Time O(N)
Space O(N): store the output, else O(1) if just printing the result
"""
from typing import List, Tuple


def solve(n: int) -> Tuple[List[int], List[int]]:
    _sum = int(n * (n + 1) / 2)
    arr1: List[int] = []
    arr2: List[int] = []
    if _sum % 2 == 1:
        return arr1, arr2
    budget = int(_sum / 2)
    for i in range(n, 0, -1):
        if budget - i >= 0:
            arr1.append(i)
            budget -= i
        else:
            arr2.append(i)
    return arr1, arr2


if __name__ == "__main__":
    _n = int(input())
    s1, s2 = solve(_n)
    if len(s1) == 0:
        print("NO")
    else:
        print("YES")
        print(f"{len(s1)}")
        print(" ".join([str(x) for x in s1]))
        print(f"{len(s2)}")
        print(" ".join([str(x) for x in s2]))
