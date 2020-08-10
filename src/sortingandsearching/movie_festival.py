"""
In a movie festival n movies will be shown. You know the starting and ending time of each movie.
What is the maximum number of movies you can watch entirely?
Input
The first input line has an integer n: the number of movies.
After this, there are n lines that describe the movies.
Each line has two integers a and b: the starting and ending times of a movie.
Output
Print one integer: the maximum number of movies.

Constraints
1≤n≤2⋅10^5
1≤a<b≤10^9
Example
Input:
3
3 5
4 9
5 8
Output:
2
"""
from typing import List, NamedTuple


class Movie(NamedTuple):
    end: int
    start: int


def solve(movies: List[Movie]) -> int:
    movies.sort()  # sort by end times
    end = 0
    res: int = 0
    for m in movies:
        if m.start >= end:
            res += 1
            end = m.end
    return res


if __name__ == "__main__":
    n = int(input())
    _movies: List[Movie] = []
    for _ in range(n):
        a, b = [int(s) for s in input().split()]
        _movies.append(Movie(start=a, end=b))
    _res: int = solve(_movies)
    print(_res)
