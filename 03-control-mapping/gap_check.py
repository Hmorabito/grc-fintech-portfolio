"""Check the control library for gaps: missing mappings, owners, evidence, and coverage per framework."""
import csv
from pathlib import Path

CSV_PATH = Path(__file__).parent / "controls.csv"
FRAMEWORKS = {"nist_csf": "NIST CSF 2.0", "iso_27001": "ISO 27001", "soc2": "SOC 2"}


def is_empty(value: str) -> bool:
    return value is None or value.strip() in ("", "N/A")


def main():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        controls = list(csv.DictReader(f))
    total = len(controls)
    print(f"Controls loaded: {total}\n")

    print("== Coverage by framework ==")
    for col, name in FRAMEWORKS.items():
        mapped = sum(1 for c in controls if not is_empty(c[col]))
        print(f"{name:<14} {mapped}/{total} controls mapped ({100 * mapped / total:.0f}%)")

    print("\n== Gaps ==")
    issues = 0
    for c in controls:
        problems = []
        for col, name in FRAMEWORKS.items():
            if is_empty(c[col]):
                problems.append(f"no {name} mapping")
        if is_empty(c["owner"]):
            problems.append("no owner")
        if c["status"] == "Implemented" and is_empty(c["evidence"]):
            problems.append("marked Implemented but has no evidence")
        if c["status"] in ("Not implemented", "Planned"):
            problems.append(f"status: {c['status']}")
        if problems:
            issues += 1
            print(f"{c['control_id']} {c['control_name']}: " + "; ".join(problems))
    if issues == 0:
        print("No gaps found.")

    print("\n== Status summary ==")
    for status in ["Implemented", "Partial", "Planned", "Not implemented"]:
        n = sum(1 for c in controls if c["status"] == status)
        print(f"{status:<16} {n}")


if __name__ == "__main__":
    main()
