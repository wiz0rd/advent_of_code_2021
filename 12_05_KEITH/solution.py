from collections import Counter
from aocd import get_data

coordinates_data = get_data(day=5, year=2021).splitlines()

# with open('input.txt') as f:
#     coordinates_data = f.read().split('\n')


def get_values_between(v1, v2, multiplier):

    if v1 > v2:
        return [*range(v1, v2 - 1, -1)]
    elif v1 < v2:
        return [*range(v1, v2 + 1)]
    else:
        return [v1] * multiplier


def get_intersections_count(coordinates_data, include_diagonal):
    lines = []
    for coordinates_set in coordinates_data:
        (x1, y1), (x2, y2) = [
            tuple(int(i) for i in x_y.split(",")) for x_y in coordinates_set.split("->")
        ]

        x_dist = abs(x1 - x2)
        y_dist = abs(y1 - y2)

        is_diagonal = x_dist != 0 and y_dist != 0

        if is_diagonal and not include_diagonal:
            continue

        multiplier = max(x_dist, y_dist) + 1
        x_values = get_values_between(x1, x2, multiplier)
        y_values = get_values_between(y1, y2, multiplier)

        for idx, x in enumerate(x_values):
            lines.append(((x, y_values[idx])))

    count = Counter(lines)
    return len([i for i in count.values() if i > 1])


def part1():
    return get_intersections_count(coordinates_data, False)


def part2():
    return get_intersections_count(coordinates_data, True)


print("\n", "----PART 1-----", "\n")
print(part1())
print("\n", "----PART 2-----", "\n")
print(part2())