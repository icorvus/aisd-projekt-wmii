import numpy as np
import random


def read_points_and_matrix(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Read number of points
    num_points = int(lines[0].strip())
    points = []
    for i in range(1, num_points + 1):
        x, y = map(float, lines[i].strip().split())
        points.append((x, y))

    # Read matrix
    matrix = []
    for line in lines[num_points + 1:]:
        if line.strip() == 'end':
            break
        matrix.append(list(map(int, line.strip().split())))
    matrix = np.array(matrix)

    return points, matrix


def read_relations(filename: str):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Read number of people
    n = int(lines[0].strip())
    people = []
    for i in range(1, n + 1):
        hands = lines[i].strip()
        people.append({'id': i - 1, 'hands': hands})

    relations = []
    for line in lines[n + 1:]:
        if line.strip() == 'end':
            break
        u, v = map(int, line.strip().split())
        relations.append((u, v))

    return people, relations


def generate_points_and_matrix(num_points):
    points = []
    for _ in range(num_points):
        x = round(random.uniform(0, 100), 2)
        y = round(random.uniform(0, 100), 2)
        points.append((x, y))

    matrix = np.random.randint(0, 11, size=(num_points, num_points))
    matrix = np.triu(matrix)  # gorny trojkat
    matrix = matrix + matrix.T - np.diag(matrix.diagonal())  # symetria
    np.fill_diagonal(matrix, 0)

    return points, matrix
