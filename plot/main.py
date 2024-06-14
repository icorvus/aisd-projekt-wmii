import sys
import numpy as np
from point import LandPoint
from relations import build_graph, draw_graph, read_input
from world import WorldVisualizer, World
from hull import ConvexHullSearcher
from max_flow import EdmondsKarp
from utils import read_relations, read_points_and_matrix, generate_points_and_matrix


def print_matrix(matrix: np.ndarray):
    for row in matrix:
        print(", ".join(f"{val:2d}" for val in row))


def main():
    if len(sys.argv) == 3:
        points_and_matrix_file = sys.argv[1]
        relations_file = sys.argv[2]

        # Reading points and matrix from file
        points, matrix = read_points_and_matrix(points_and_matrix_file)

        # Reading relations from file
        people, relations = read_relations(relations_file)

    else:
        # Generate random points and matrix
        num_points = 10
        points, matrix = generate_points_and_matrix(num_points)

        # Manually input relations
        people, relations = read_input()

    # Generate world and plot points
    world = World(width=100, height=100, land_points=[LandPoint(x, y) for x, y in points])
    WorldVisualizer.plot_world(world)
    world.fence_points = ConvexHullSearcher(world.land_points).find_convex_hull()
    WorldVisualizer.plot_fence(world)

    # Print matrix
    print("Matrix:")
    print_matrix(matrix)

    # Max flow calculation
    ek = EdmondsKarp(matrix)
    source, sink = 0, len(matrix) - 1
    max_flow = ek.edmonds_karp(source, sink)
    print(f"Max flow from {source} to {sink}: {max_flow}")

    # Graph relations
    g, source, sink, front_ids, back_ids = build_graph(people, relations)
    max_matching = g.edmonds_karp_relations(source, sink)
    print(f'Max association: {max_matching}')
    draw_graph(people, relations, front_ids, back_ids)

if __name__ == "__main__":
    main()
