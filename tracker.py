# tracker.py - Assignment Tracker: lists my upcoming assignments


def show(items):
    print("Upcoming Assignments")
    print("=" * 30)
    for item in items:
        print(f"{item['due']}  {item['name']}")


assignments = [
    {"name": "CSE 335 Lab 6", "due": "2026-10-24"},
    {"name": "CSE 463 Assignment 3", "due": "2026-11-04"},
    {"name": "CSE 463 Growing a Competency", "due": "2026-10-28"},
    {"name": "CSE 335 Project", "due": "2026-11-18"},
]

if __name__ == "__main__":
    show(assignments)
