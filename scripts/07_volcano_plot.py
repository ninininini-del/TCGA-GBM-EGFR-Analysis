import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -------------------------
# Load results
# -------------------------
df = pd.read_csv("../results/EGFR_differential_expression.csv")

# -------------------------
# Clean data
# -------------------------
df = df.dropna()

# Add -log10(p-value)
df["neg_log10_p"] = -np.log10(df["PValue"])

# -------------------------
# Define significance
# -------------------------
df["significant"] = (df["PValue"] < 0.05) & (abs(df["Log2FoldChange"]) > 1)

# -------------------------
# Plot
# -------------------------
plt.figure(figsize=(10, 7))

# Non-significant genes
plt.scatter(
    df["Log2FoldChange"],
    df["neg_log10_p"],
    c="gray",
    alpha=0.5,
    s=10
)

# Significant genes
sig = df[df["significant"]]

plt.scatter(
    sig["Log2FoldChange"],
    sig["neg_log10_p"],
    c="red",
    alpha=0.7,
    s=10
)

# Highlight EGFR
egfr = df[df["Gene"] == "EGFR"]

plt.scatter(
    egfr["Log2FoldChange"],
    egfr["neg_log10_p"],
    c="blue",
    s=80,
    label="EGFR"
)

# Labels
plt.axhline(-np.log10(0.05), linestyle="--", color="black")
plt.axvline(-1, linestyle="--", color="black")
plt.axvline(1, linestyle="--", color="black")

plt.title("EGFR Differential Expression Volcano Plot")
plt.xlabel("Log2 Fold Change")
plt.ylabel("-log10(P-value)")
plt.legend()

plt.tight_layout()
plt.show()