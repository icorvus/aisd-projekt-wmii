import numpy as np
from relations import read_input, build_graph, draw_graph
from world import WorldGenerator, WorldVisualizer, World
from hull import ConvexHullSearcher
from max_flow import EdmondsKarp
from utils import create_random_matrix_for_flow


def print_matrix(matrix: np.ndarray):
    for row in matrix:
        print(", ".join(f"{val:2d}" for val in row))


def main():
    width = 50
    height = 50
    number_of_points = 10
    world_generator = WorldGenerator(width=width, height=height)
    world = world_generator.generate_world(number_of_points=number_of_points)
    WorldVisualizer.plot_world(world)
    world.fence_points = ConvexHullSearcher(world.land_points).find_convex_hull()
    WorldVisualizer.plot_fence(world)


    points_on_fence, points_inside_fence = world.count_points()
    total_points = points_on_fence + points_inside_fence
    print(f"Points on fence: {points_on_fence}, Points inside fence: {points_inside_fence}")
    print(f"Total points: {total_points}")
    matrix = create_random_matrix_for_flow(total_points)
    print_matrix(matrix)
    # print("Random matrix:\n", matrix)
    ek = EdmondsKarp(matrix)
    source, sink = 0, total_points - 1
    max_flow = ek.edmonds_karp(source, sink)
    print(f"Max flow from {source} to {sink}: {max_flow}")


    people, relations = read_input()
    g, source, sink, front_ids, back_ids = build_graph(people, relations)
    max_matching = g.edmonds_karp_relations(source, sink)
    print(f'Max association: {max_matching}')
    draw_graph(people, relations, front_ids, back_ids)


if __name__ == "__main__":
    main()