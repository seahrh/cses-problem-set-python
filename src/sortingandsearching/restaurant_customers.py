"""
You are given the arrival and leaving times of n customers in a restaurant.
What was the maximum number of customers?
Input
The first input line has an integer n: the number of customers.
After this, there are n lines that describe the customers.
Each line has two integers a and b: the arrival and leaving times of a customer.
You may assume that all arrival and leaving times are distinct.
Output
Print one integer: the maximum number of customers.
Constraints
1=n=2·10^5
1=a<b=10^9
Example
Input:
3
5 8
2 4
3 9
Output:
2

SOLUTION
Put all arrival and departures in a "timeline" array, then sort the array.
Increment the count when it is an arrival, else decrement.
Time O(N lg N)
Space O(N)
"""
import sys
from typing import List, Tuple, NamedTuple


class Timing(NamedTuple):
    time: int
    is_arrival: bool


def solve(customers: List[Tuple[int, int]]) -> int:
    curr = 0
    _max: int = -sys.maxsize
    timings: List[Timing] = []
    for arrival, departure in customers:
        timings.append(Timing(arrival, True))
        timings.append(Timing(departure, False))
    timings.sort()
    for t in timings:
        if t.is_arrival:
            curr += 1
        else:
            curr -= 1
        _max = max(curr, _max)
    return _max


if __name__ == "__main__":
    n = int(input())
    _customers: List[Tuple[int, int]] = []
    for _ in range(n):
        a, b = [int(s) for s in input().split()]
        _customers.append((a, b))
    _res: int = solve(_customers)
    print(_res)
