"""Read risk_register.csv, rank risks and draw a 5x5 likelihood/impact heatmap."""
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # no window needed; we only save a PNG
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

HERE = Path(__file__).parent
CSV_PATH = HERE / "risk_register.csv"
PNG_PATH = HERE / "heatmap.png"


def rating(score: int) -> str:
    if score >= 17:
        return "Critical"
    if score >= 10:
        return "High"
    if score >= 5:
        return "Medium"
    return "Low"


def load_risks():
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        risks = []
        for row in csv.DictReader(f):
            row["likelihood"] = int(row["likelihood"])
            row["impact"] = int(row["impact"])
            row["score"] = row["likelihood"] * row["impact"]
            row["rating"] = rating(row["score"])
            risks.append(row)
    return risks


def print_summary(risks):
    print(f"{'ID':<7}{'Score':<7}{'Rating':<10}{'Owner':<20}Title")
    print("-" * 80)
    for r in sorted(risks, key=lambda x: x["score"], reverse=True):
        print(f"{r['risk_id']:<7}{r['score']:<7}{r['rating']:<10}{r['owner']:<20}{r['title']}")
    counts = defaultdict(int)
    for r in risks:
        counts[r["rating"]] += 1
    print("\nTotals:", ", ".join(f"{k}: {counts[k]}" for k in ["Critical", "High", "Medium", "Low"]))


def draw_heatmap(risks):
    # Background colour of each cell by score band
    band = [[0] * 5 for _ in range(5)]
    for li in range(1, 6):
        for im in range(1, 6):
            s = li * im
            band[li - 1][im - 1] = 3 if s >= 17 else 2 if s >= 10 else 1 if s >= 5 else 0
    cmap = ListedColormap(["#c8e6c9", "#fff59d", "#ffcc80", "#ef9a9a"])

    cell_ids = defaultdict(list)
    for r in risks:
        cell_ids[(r["likelihood"], r["impact"])].append(r["risk_id"])

    fig, ax = plt.subplots(figsize=(8, 7))
    ax.imshow(band, cmap=cmap, origin="lower", extent=(0.5, 5.5, 0.5, 5.5))
    for (li, im), ids in cell_ids.items():
        ax.text(im, li, "\n".join(ids), ha="center", va="center", fontsize=8, fontweight="bold")
    ax.set_xticks(range(1, 6))
    ax.set_yticks(range(1, 6))
    ax.set_xlabel("Impact")
    ax.set_ylabel("Likelihood")
    ax.set_title("Meridian Pay: Risk Heatmap")
    ax.grid(color="white", linewidth=2)
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=150)
    print(f"Saved {PNG_PATH.name}")


if __name__ == "__main__":
    data = load_risks()
    print_summary(data)
    draw_heatmap(data)
