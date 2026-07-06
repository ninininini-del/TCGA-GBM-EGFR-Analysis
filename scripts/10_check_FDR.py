import pandas as pd

df = pd.read_csv("../results/EGFR_differential_expression_FDR.csv")

print(df.head(20))

sig = df[df["FDR"] < 0.05]

print("\nNumber of significant genes:", len(sig))

print("\nTop significant genes:")
print(sig.head(20))

sig.to_csv(
    "../results/significant_genes_FDR.csv",
    index=False
)

print("\nFile saved!")