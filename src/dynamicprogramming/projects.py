"""
There are n projects you can attend.
For each project, you know its starting and ending days and the amount of money you would get as reward.
You can only attend one project during a day.
What is the maximum amount of money you can earn?
Input
The first input line contains an integer n: the number of projects. After this, there are n lines.
Each line has three integers ai, bi, and pi: the starting day, the ending day, and the reward.
Output
Print one integer: the maximum amount of money you can earn.
Constraints
1≤n≤2⋅10^5
1≤ai≤bi≤10^9
1≤pi≤10^9
Example
Input:
4
2 4 4
3 6 6
6 8 2
5 7 3
Output:
7

SOLUTION
Bottom-up DP, dp[i] = max reward for considering the first i projects
Two choices: either do project i or give it up (same as dp[i - 1]).
Do project i = reward(i) + dp[j]
where j is the nearest project on the left that ends before the start date of project i.
Time O(N lg N): binary search in the loop
Space O(N): memo array

See https://www.youtube.com/watch?v=MJn3ogwsUbo
"""
from bisect import bisect_left
from typing import List, NamedTuple


class Project(NamedTuple):
    end: int
    start: int
    reward: int


def solve(projects: List[Project]) -> int:
    projects.sort()
    memo: List[int] = [0] * len(projects)
    memo[0] = projects[0].reward
    for i in range(1, len(projects)):
        # find nearest project on the left that ends before the start date of current project
        s = projects[i].start
        j = bisect_left(projects, Project(end=s, start=1, reward=1)) - 1
        alt = projects[i].reward
        if j != -1:
            alt += memo[j]
        memo[i] = max(memo[i - 1], alt)
    return memo[-1]


if __name__ == "__main__":
    n = int(input())
    _projects: List[Project] = []
    for _ in range(n):
        start, end, reward = [int(s) for s in input().split()]
        _projects.append(Project(end=end, start=start, reward=reward))
    _res: int = solve(_projects)
    print(_res)
