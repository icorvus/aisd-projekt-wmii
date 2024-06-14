from pathlib import Path

from route_optimizer import RouteOptimizer
from segment_tree import SegmentTree


def main():
    with Path.open("guards.txt") as file:
        guards = list(map(int, file.readline().split()))
    print(f"Loaded {len(guards)} guards")

    with Path.open("points.txt") as file:
        max_stops = int(file.readline())
        brightness = list(map(int, file.readline().split()))
    print(f"Loaded {len(brightness)} points")
    print(f"Min brightness: {min(brightness)}, Max brightness: {max(brightness)}")
    print(f"Max stops: {max_stops}")

    print(
        "Enter the range in which you will search for "
        "the guard with the highest energy",
    )
    a, b = map(int, input().split())

    seg_tree = SegmentTree(guards)
    energy, guard_with_highest_energy_index = seg_tree.query(a, b)

    print(
        f"Guard with the highest energy in the range {a}-{b} "
        f"is the guard with index {guard_with_highest_energy_index} "
        f"and his energy is: {energy}",
    )

    optimizer = RouteOptimizer(brightness, max_stops)

    melody_listened, stops = optimizer.naive_patrol_route_optimization()

    print("The route optimizer has found the following stops:")
    print(stops)
    print(f"Melody will be listened: {melody_listened} times")


if __name__ == "__main__":
    main()
