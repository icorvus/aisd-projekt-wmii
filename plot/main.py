import random

import matplotlib.pyplot as plt

height = 1000
width = 1000

def generate_random_point():
    return (random.uniform(0, width), random.uniform(0, height))

def plot_random_points():
    points = [generate_random_point() for i in range(100)]
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    plt.scatter(x, y)
    plt.show()


def main():
    plot_random_points()

if __name__ == "__main__":
    main()