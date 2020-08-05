"""
There are n concert tickets available, each with a certain price.
Then, m customers arrive, **one after another**.
Each customer announces the maximum price he or she is willing to pay for a ticket,
and after this, they will get a ticket with the **nearest possible price**
such that it does not exceed the maximum price.

Input
The first input line contains integers n and m: the number of tickets and the number of customers.
The next line contains n integers h1,h2,…,hn: the price of each ticket.
The last line contains m integers t1,t2,…,tm: the maximum price for each customer.

Output
Print, for each customer, the price that they will pay for their ticket.
After this, the ticket cannot be purchased again.
If a customer cannot get any ticket, print −1.

Constraints
1≤n,m≤2⋅10^5
1≤hi,ti≤10^9

Example
Input:
5 3
5 3 7 8 5
4 8 3
Output:
3
8
-1

See https://cses.fi/problemset/task/1091
SOLUTION
Requirement: Sell the most expensive ticket that meets the customer's budget
Time O((N + M) lg N)
Space O(N): store the ticket prices in a multiset (Counter).
"""
from bisect import bisect
from collections import Counter
from typing import List


def prices(tickets: List[int], customers: List[int]) -> List[int]:
    # Counter elements are returned in insertion order, so sort the tickets first.
    tickets.sort()
    c = Counter(tickets)  # O(N) space
    res: List[int] = []
    for budget in customers:
        remaining = list(c.elements())  # O(N) space
        # highest price that meets the customer's budget
        i = bisect(remaining, budget) - 1  # O(lg N) time
        if i >= 0:
            res.append(remaining[i])
            c[remaining[i]] -= 1
            continue
        res.append(-1)
    return res
