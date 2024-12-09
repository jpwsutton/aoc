"""Advent of code 2024. Day 2 solution."""

from pathlib import Path

script_dir = Path(__file__).resolve().parent


def load_input(filename: str) -> list[list[int]]:
    """Load the input file and parse."""
    input_path = script_dir / filename
    print(f"Input: {input_path}")
    reports = []
    with open(input_path) as f:
        for line in f:
            reports.append([int(x) for x in line.split()])
    return reports


def check_report(report: list[int]) -> bool:
    """Check if report is safe (True) or unsafe (False)."""
    sorted_asc = all(report[i] <= report[i + 1] for i in range(len(report) - 1))
    sorted_dsc = all(report[i] >= report[i + 1] for i in range(len(report) - 1))
    is_sorted = sorted_asc or sorted_dsc

    # print(f"Sorted: {is_sorted}. Asc: {sorted_asc}. Dsc: {sorted_dsc}")

    for previous, current in zip(report, report[1:]):

        change = abs(previous - current)
        # print(f"comparing: {previous}, {current}. Change: {change}")
        if change < 1 or change > 3:
            return False

    return is_sorted


def check_report_dampen(report: list[int]) -> bool:
    """Check if report is safe (True) or unsafe (False)."""
    # There is probably a really elegant solution for this.
    # However.. I am not an elegant person.

    for idx, _ in enumerate(report):

        test_list = list(report)
        test_list.pop(idx)
        if check_report(test_list) is True:
            return True

    return False


def part_1() -> int:
    """Part 1 solution."""
    reports = load_input("input.txt")
    report_status = []
    for report in reports:
        report_status.append(check_report(report))

    return sum(report_status)


def part_2() -> int:
    """Part 2 solution."""
    reports = load_input("input.txt")
    report_statuses = []
    for report in reports:
        dampened = False
        report_status = check_report(report)
        if report_status is False:
            # Process it again with dampening
            dampened = True
            report_status = check_report_dampen(report)
        print(f"Processing report: {report}: {report_status}. Dampened: {dampened}")
        report_statuses.append(report_status)

    return sum(report_statuses)


if __name__ == "__main__":
    print("Advent of code 2024. Day 2 Solution.")

    p1_sol = part_1()
    print(f"Part 1 Solution: {p1_sol}")

    p2_sol = part_2()
    print(f"Part 2 solution: {p2_sol}")

    # 502 - too low
