"""Student Attendance Cleaner
Reads attendance.txt, cleans the names, removes duplicates and saves
the sorted result to attendance_clean.csv.
"""

import csv

INPUT_FILE = "attendance.txt"
OUTPUT_FILE = "attendance_clean.csv"


def main():
    try:
        with open(INPUT_FILE, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found. Keep it in the same folder as this script.")
        return

    # List comprehension: strip extra spaces + Title Case (blank lines skipped)
    cleaned = [line.strip().title() for line in lines if line.strip()]

    unique_students = set(cleaned)       # set removes duplicate names
    sorted_students = sorted(unique_students)

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["name"])
        writer.writerows([name] for name in sorted_students)

    blank_lines = len(lines) - len(cleaned)
    print(f"Original number of records : {len(cleaned)}")
    if blank_lines:
        print(f"(Blank lines skipped       : {blank_lines})")
    print(f"Unique students            : {len(unique_students)}")
    print("\nCleaned attendance list:")
    for number, name in enumerate(sorted_students, start=1):
        print(f"  {number}. {name}")
    print(f"\nSaved to {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
