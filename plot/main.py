from hull import ConvexHullSearcher
from world import NetworkGenerator, NetworkVisualizer, WorldGenerator, WorldVisualizer

from max_flow import MaxFlowFinder

import random

def main():
    width = 50
    height = 50
    number_of_points = 10
    world_generator = WorldGenerator(width=width, height=height)
    world = world_generator.generate_world(number_of_points=number_of_points)
    WorldVisualizer.plot_world(world)
    world.fence_points = ConvexHullSearcher(world.land_points).find_convex_hull()
    WorldVisualizer.plot_fence(world)

    network = NetworkGenerator(world).generate_network(25, 0.1, range(1, 10))
    NetworkVisualizer.plot_network(network)

    random_two_points = random.sample(world.land_points, 2)

    edges, max_flow = MaxFlowFinder(network).find_max_flow(random_two_points[0], random_two_points[1])

    print(len(edges), max_flow)



if __name__ == "__main__":
    main()
