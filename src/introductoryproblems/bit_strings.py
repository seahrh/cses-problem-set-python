"""
Your task is to calculate the number of bit strings of length n.
For example, if n=3, the correct answer is 8
because the possible bit strings are 000, 001, 010, 011, 100, 101, 110, and 111.
Input
The only input line has an integer n.
Output
Print the result modulo 10^9+7.
Constraints
1≤n≤10^6
Example
Input:
3
Output:
8

SOLUTION
Naive implementation: int(math.pow(2, n) % (1e9 + 7))
The above will throw overflow error (math range error) for large N.
To prevent overflow error, apply modulus in each iteration of N.
Time O(N)
Space O(1)
"""


def solve(n: int) -> int:
    mod = 1e9 + 7
    res: int = 1
    for _ in range(n):
        res = int(res * 2 % mod)
    return res


if __name__ == "__main__":
    _n = int(input())
    _res: int = solve(_n)
    print(_res)
