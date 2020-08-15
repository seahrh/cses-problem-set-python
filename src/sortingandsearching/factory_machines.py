"""
A factory has n machines which can be used to make products. Your goal is to make a total of t products.
For each machine, you know the number of seconds it needs to make a single product.
The machines can work simultaneously, and you can freely decide their schedule.
What is the shortest time needed to make t products?
Input
The first input line has two integers n and t: the number of machines and products.
The next line has n integers k1,k2,…,kn: the time needed to make a product using each machine.
Output
Print one integer: the minimum time needed to make t products.
Constraints
1≤n≤2⋅10^5
1≤t≤10^9
1≤ki≤10^9
Example
Input:
3 7
3 2 5
Output:
8
Explanation: Machine 1 makes two products, machine 2 makes four products and machine 3 makes one product.

SOLUTION
The time range is a sorted array. Do binary search to find the solution.
Time O(N lg T^2)
Space O(1)
"""
from typing import List


def solve(target: int, machines: List[int]) -> int:
    _max = max(machines)  # Time O(N)
    lo = 1
    hi = _max * target
    res: int = hi
    while lo <= hi:  # Time O(N lg T^2)
        mid = int(lo / 2 + hi / 2)
        products = 0
        for m in machines:  # Time O(N)
            products += int(mid / m)
            if products >= target:
                break
        if products >= target:
            res = mid
            hi = mid - 1
            continue
        lo = mid + 1
    return res


if __name__ == "__main__":
    _, t = [int(s) for s in input().split()]
    _machines: List[int] = [int(s) for s in input().split()]
    _res: int = solve(t, _machines)
    print(_res)
