from pathlib import Path
import pandas as pd

# -------------------------
# Paths
# -------------------------
project = Path(__file__).resolve().parent.parent
results = project / "results"

# -------------------------
# Load differential expression results
# -------------------------
df = pd.read_csv(results / "EGFR_differential_expression_FDR.csv")

# -------------------------
# Split genes
# -------------------------
up = df[
    (df["FDR"] < 0.05) &
    (df["Log2FoldChange"] > 1)
]

down = df[
    (df["FDR"] < 0.05) &
    (df["Log2FoldChange"] < -1)
]

print("Upregulated genes:", len(up))
print("Downregulated genes:", len(down))

print("\nTop upregulated genes:")
print(up[["Gene", "Log2FoldChange", "FDR"]].head())

print("\nTop downregulated genes:")
print(down[["Gene", "Log2FoldChange", "FDR"]].head())