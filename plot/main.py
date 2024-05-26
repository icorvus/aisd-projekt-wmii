from hull import ConvexHullSearcher
from world import WorldGenerator, WorldVisualizer


def main():
    width = 100
    height = 100
    number_of_points = 25
    world_generator = WorldGenerator(width=width, height=height)
    world = world_generator.generate_world(number_of_points=number_of_points)
    WorldVisualizer.plot_world(world)
    world.fence_points = ConvexHullSearcher(world.land_points).find_convex_hull()
    WorldVisualizer.plot_fence(world)


if __name__ == "__main__":
    main()
