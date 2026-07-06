import numpy as np
import pandas as pd

# Load results
df = pd.read_csv("../results/EGFR_differential_expression.csv")

print("Shape:", df.shape)

print("\nTop 10 genes (by P-value):")
print(df.head(10))

print("\nTop 10 most upregulated genes:")
print(df.sort_values("Log2FoldChange", ascending=False).head(10))

print("\nTop 10 most downregulated genes:")
print(df.sort_values("Log2FoldChange").head(10))

# Remove missing values (just in case)
df = df.dropna()

# Add -log10(PValue)
df["neg_log10_p"] = -np.log10(df["PValue"])

sig = df[df["PValue"] < 0.05]

print("\nSignificant genes:", len(sig))
print(sig.head(10))