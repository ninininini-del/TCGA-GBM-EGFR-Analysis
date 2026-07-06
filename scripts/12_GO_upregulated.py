from pathlib import Path
import pandas as pd
import gseapy as gp

project = Path(__file__).resolve().parent.parent
results = project / "results"

# Load differential expression results
df = pd.read_csv(results / "EGFR_differential_expression_FDR.csv")

# Keep only strongly upregulated genes
up = df[
    (df["FDR"] < 0.05) &
    (df["Log2FoldChange"] > 1)
]

gene_list = up["Gene"].tolist()

print(f"Upregulated genes: {len(gene_list)}")

enr = gp.enrichr(
    gene_list=gene_list,
    gene_sets="GO_Biological_Process_2023",
    organism="hsapiens",
    outdir=None
)

go = enr.results

# Show the 20 best GO terms regardless of significance
print(go[[
    "Term",
    "P-value",
    "Adjusted P-value",
    "Combined Score"
]].head(20))