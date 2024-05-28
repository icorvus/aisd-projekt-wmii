import math
import matplotlib.pyplot as plt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Graham:
    def __init__(self, points):
        self.points = points

    def Left_index(self):
        minn = 0
        for i in range(1, len(self.points)):
            if self.points[i].x < self.points[minn].x:
                minn = i
            elif self.points[i].x == self.points[minn].x:
                if self.points[i].y > self.points[minn].y:
                    minn = i
        return minn

    def orientation(self, p, q, r):
        val = (q.y - p.y) * (r.x - q.x) - \
              (q.x - p.x) * (r.y - q.y)

        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2

    def convexHull(self):
        n = len(self.points)
        if n < 3:
            return []

        l = self.Left_index()

        hull = []

        p = l
        q = 0
        while True:
            hull.append(p)
            q = (p + 1) % n

            for i in range(n):
                if self.orientation(self.points[p],
                                    self.points[i], self.points[q]) == 2:
                    q = i

            p = q
            if p == l:
                break

        return hull

    def distance(self, point1, point2):
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

    def convexHullLength(self):
        hull_indices = self.convexHull()
        if not hull_indices:
            return 0

        hull_points = [self.points[i] for i in hull_indices]
        length = 0
        for i in range(len(hull_points)):
            length += self.distance(hull_points[i], hull_points[(i + 1) % len(hull_points)])
        return length

    def plotConvexHull(self):
        hull_indices = self.convexHull()
        if not hull_indices:
            return

        hull_points = [self.points[i] for i in hull_indices]

        # Dodaj pierwszy punkt na koniec listy, aby zamknąć otoczkę
        hull_points.append(hull_points[0])

        # Wykres punktów
        x_points = [point.x for point in self.points]
        y_points = [point.y for point in self.points]
        plt.scatter(x_points, y_points, label='Punkty')

        # Wykres otoczki wypukłej
        x_hull = [point.x for point in hull_points]
        y_hull = [point.y for point in hull_points]
        plt.plot(x_hull, y_hull, 'r-', label='Otoczka wypukła')

        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Otoczka wypukła')
        plt.legend()
        plt.show()
        plt.savefig("plot_hull.png")
        plt.close()

    def is_inside_hull(self, point):
        hull_indices = self.convexHull()
        if not hull_indices:
            return False

        hull_points = [self.points[i] for i in hull_indices]

        def on_segment(p, q, r):
            return (q.x <= max(p.x, r.x) and q.x >= min(p.x, r.x) and
                    q.y <= max(p.y, r.y) and q.y >= min(p.y, r.y))

        def direction(p, q, r):
            val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y)
            if val == 0:
                return 0
            elif val > 0:
                return 1
            else:
                return 2

        def is_point_in_polygon(polygon, p):
            n = len(polygon)
            if n < 3:
                return False

            extreme = Point(1e10, p.y)

            count = 0
            i = 0
            while True:
                next = (i + 1) % n
                if direction(polygon[i], p, polygon[next]) == 0 and on_segment(polygon[i], p, polygon[next]):
                    return True

                if direction(polygon[i], p, extreme) != direction(polygon[next], p, extreme) and \
                        direction(p, polygon[i], polygon[next]) != direction(extreme, polygon[i], polygon[next]):
                    count += 1

                i = next
                if i == 0:
                    break

            return count % 2 == 1

        return is_point_in_polygon(hull_points, point)

    def addPoint(self, point):
        self.points.append(point)

    def updatePoints(self, points):
        self.points = points
