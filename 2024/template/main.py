"""Advent of code 2024. Day x solution."""

from pathlib import Path

script_dir = Path(__file__).resolve().parent


def load_input(filename: str) -> None:
    """Load the input file and parse."""
    input_path = script_dir / filename
    print(f"Input: {input_path}")


def part_1() -> int:
    """Part 1 solution."""
    pass


def part_2() -> int:
    """Part 2 solution."""
    pass


if __name__ == "__main__":
    print("Advent of code 2024. Day x Solution.")

    p1_sol = part_1()
    print(f"Part 1 Solution: {p1_sol}")

    p2_sol = part_2()
    print(f"Part 2 solution: {p2_sol}")
