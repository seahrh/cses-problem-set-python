"""
You have to process n tasks. Each task has a duration and a deadline,
and you will process the tasks in some order one after another.
Your reward for a task is d−f where d is its deadline and f is your finishing time.
(The starting time is 0, and you have to process all tasks even if a task would yield negative reward.)
What is your maximum reward if you act optimally?
Input
The first input line has an integer n: the number of tasks.
After this, there are n lines that describe the tasks.
Each line has two integers a and d: the duration and deadline of the task.
Output
Print one integer: the maximum reward.
Constraints
1≤n≤2⋅10^5
1≤a,d≤10^6
Example
Input:
3
6 10
8 15
5 12
Output:
2

SOLUTION
To minimise penalty, sort the tasks by shortest duration first, then shortest deadline.
Time O(N lg N)
Space O(1)
"""
from typing import List, NamedTuple


class Task(NamedTuple):
    duration: int
    deadline: int


def solve(tasks: List[Task]) -> int:
    tasks.sort()
    curr = 0
    res: int = 0
    for t in tasks:
        curr += t.duration
        res += t.deadline - curr
    return res


if __name__ == "__main__":
    n = int(input())
    _tasks: List[Task] = []
    for _ in range(n):
        duration, deadline = [int(s) for s in input().split()]
        _tasks.append(Task(duration, deadline))
    _res: int = solve(_tasks)
    print(_res)
