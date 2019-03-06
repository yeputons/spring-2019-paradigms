#!/usr/bin/env python3
class Point:
    def __init__(self, x, y):
        pass

    def __lt__(self, other):
        return (self.x, self.y) < (other.x, other.y)


class PointWithId(Point):
    def __init__(self, x, y, index):
        pass

    def __lt__(self, other):
        if isinstance(other, PointWithId):
            return (
                (self.x, self.y, self.index) <
                (other.x, other.y, other.index)
            )
        return (self.x, self.y) < (other.x, other.y)


a = [
    Point(1, 2),
    PointWithId(1, 2, 10),
    Point(1, 2),
    PointWithId(1, 2, 1),
]
