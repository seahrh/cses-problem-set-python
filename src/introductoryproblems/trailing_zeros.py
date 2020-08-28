"""
Your task is to calculate the number of trailing zeros in the factorial n!.
For example, 20!=2432902008176640000 and it has 4 trailing zeros.
Input
The only input line has an integer n.
Output
Print the number of trailing zeros in n!.
Constraints
1≤n≤10^9
Example
Input:
20
Output:
4

SOLUTION
Consider a factorial like 19!:
19! = 1*2* 3*4* 5*6*7*8*9* 10* 11* 12* 13*14*15* 16* 17*18*19
A trailing zero is created with multiples of 10
and multiples of 10 are created with pairs of 5-multiples and 2-multiples.
Therefore, to count the number of zeros, we only need to count the pairs of multiples of 5 and 2.
There will always be more multiples of 2 than 5, though, so simply counting the multiples of 5 is sufficient.
One "gotcha" here is 15 contributes a multiple of 5 (and therefore one trailing zero),
while 25 contributes two (because 25 = 5 * 5).
"""


def solve(n: int) -> int:
    count = 0
    i = 5
    while int(n / i) > 0:
        count += int(n / i)
        i *= 5
    return count


if __name__ == "__main__":
    _n = int(input())
    _res: int = solve(_n)
    print(_res)
