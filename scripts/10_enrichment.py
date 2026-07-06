from pathlib import Path
import pandas as pd
import gseapy as gp

project = Path(__file__).resolve().parent.parent
results = project / "results"

df = pd.read_csv(results / "significant_genes_FDR.csv")
gene_list = df["Gene"].tolist()

print(f"Number of genes: {len(gene_list)}")

enr = gp.enrichr(
    gene_list=gene_list,
    gene_sets="GO_Biological_Process_2023",
    organism="hsapiens",
    outdir=None   # Don't generate plots yet
)

print(enr.results.head(20))
print("\nNumber of enriched terms:", len(enr.results))