from pathlib import Path
import pandas as pd
import gseapy as gp

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
# Select strongly upregulated genes
# -------------------------
up = df[
    (df["FDR"] < 0.05) &
    (df["Log2FoldChange"] > 1)
]

gene_list = up["Gene"].tolist()

print(f"Upregulated genes: {len(gene_list)}")

# -------------------------
# KEGG enrichment
# -------------------------
enr = gp.enrichr(
    gene_list=gene_list,
    gene_sets="KEGG_2021_Human",
    organism="hsapiens",
    outdir=None
)

kegg = enr.results

# -------------------------
# Show the top KEGG pathways
# -------------------------
print("\nTop 20 KEGG pathways:\n")

print(
    kegg[
        [
            "Term",
            "P-value",
            "Adjusted P-value",
            "Combined Score"
        ]
    ].head(20)
)

# -------------------------
# Save all KEGG results
# -------------------------
kegg.to_csv(
    results / "KEGG_upregulated.csv",
    index=False
)

print("\nResults saved!")

# -------------------------
# Save only significant pathways
# -------------------------
kegg_sig = kegg[kegg["Adjusted P-value"] < 0.05]

kegg_sig.to_csv(
    results / "KEGG_significant.csv",
    index=False
)

print(f"Significant KEGG pathways: {len(kegg_sig)}")