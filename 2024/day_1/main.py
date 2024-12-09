"""Advent of code 2024. Day 1 solution."""

from pathlib import Path

script_dir = Path(__file__).resolve().parent


def load_input(filename: str) -> list[int]:
    """Load the input file and parse."""
    input_path = script_dir / filename
    print(f"Input: {input_path}")
    list_a = []
    list_b = []
    with open(input_path) as f:
        for line in f:
            a, b = line.strip().split()
            list_a.append(int(a))
            list_b.append(int(b))
    print(f"List A: {list_a}")
    print(f"List B: {list_b}")
    return list_a, list_b


def part_1() -> int:
    """Part 1 solution."""
    list_a, list_b = load_input("input.txt")
    distances = []
    while len(list_a) > 0:
        list_a_min = min(list_a)
        list_a.remove(list_a_min)

        list_b_min = min(list_b)
        list_b.remove(list_b_min)
        distance = abs(list_a_min - list_b_min)
        print(f"List A Min: {list_a_min}. List B Min: {list_b_min}. Distance: {distance}")
        distances.append(distance)

    distance_sum = sum(distances)
    print(f"Lists exhausted. sum distance: {distance_sum}")
    return distance_sum


def part_2() -> int:
    """Part 2 solution."""
    list_a, list_b = load_input("input.txt")

    sim_scores = []
    for item in list_a:
        list_b_count = list_b.count(item)
        print(f"ID: {item} in list b { list_b_count} times.")
        sim_scores.append(item * list_b_count)

    return sum(sim_scores)


if __name__ == "__main__":
    print("Advent of code 2024. Day 1 Solution.")

    # p1_sol = part_1()
    # print(f"Part 1 Solution: {p1_sol}")

    p2_sol = part_2()
    print(f"Part 2 solution: {p2_sol}")
