"""Wilson intervals and two-proportion z-tests for the accuracies reported in the paper (Appendix D).

Following the paper, each test is run on correct-answer counts reconstructed from the
reported accuracies (k = round(accuracy * n)). It is an unpaired test: per-item
predictions would be needed for a paired McNemar test.
"""
from math import erfc, sqrt


def wilson(k, n, z=1.96):
    p = k / n
    c = (p + z * z / (2 * n)) / (1 + z * z / n)
    h = z * sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / (1 + z * z / n)
    return c - h, c + h


def two_prop(k1, k2, n):
    p1, p2 = k1 / n, k2 / n
    p = (k1 + k2) / (2 * n)
    z = (p1 - p2) / sqrt(p * (1 - p) * (2 / n))
    # erfc keeps precision in the far tail, where 1 - erf underflows to 0.
    return z, erfc(abs(z) / sqrt(2))


COMPARISONS = [
    ("II-Bench", "LAD vs GPT-4o-mini", 0.812, 0.635, 1399),
    ("CII-Bench", "LAD vs GPT-4o-mini", 0.538, 0.356, 800),
    ("II-Bench", "LAD vs GPT-4o", 0.812, 0.726, 1399),
    ("II-Bench", "LAD vs Claude-4.6-Sonnet", 0.812, 0.810, 1399),
    ("CII-Bench", "LAD vs GPT-4o", 0.538, 0.541, 800),
    ("S100-en", "LAD vs GPT-4o-mini", 0.74, 0.44, 50),
    ("S100-zh", "LAD vs GPT-4o-mini", 0.52, 0.42, 50),
    ("S100-en", "LAD vs Gemini-3.0-Pro", 0.74, 0.76, 50),
]

if __name__ == "__main__":
    for bench, name, a, b, n in COMPARISONS:
        k1, k2 = round(a * n), round(b * n)
        z, p = two_prop(k1, k2, n)
        lo, hi = wilson(k1, n)
        print(f"{bench:10s} {name:28s} {k1}/{n} [{lo:.3f},{hi:.3f}] vs {k2}/{n}  z={z:.2f} p={p:.3g}")
