from statsmodels.stats.multitest import multipletests

from pathlib import Path
import pandas as pd
from scipy.stats import ttest_ind

# -------------------------
# Load data
# -------------------------
project = Path(__file__).resolve().parent.parent
data = project / "data"

rna = pd.read_csv(
    data / "RNAseq.cct",
    sep="\t"
)

mutation = pd.read_csv(
    data / "Human__TCGA_GBM__WUSM__Mutation__GAIIx__01_28_2016__BI__Gene__Firehose_MutSig2CV.cbt.txt",
    sep="\t"
)

# -------------------------
# Common patients
# -------------------------
rna_patients = set(rna.columns[1:])
mutation_patients = set(mutation.columns[1:])

common = sorted(rna_patients.intersection(mutation_patients))

# -------------------------
# EGFR groups
# -------------------------
egfr = mutation[mutation["attrib_name"] == "EGFR"]

mutated = []
wildtype = []

for patient in common:
    if int(egfr[patient].values[0]) == 1:
        mutated.append(patient)
    else:
        wildtype.append(patient)

# -------------------------
# Differential expression
# -------------------------
results = []

for _, row in rna.iterrows():

    gene = row["attrib_name"]

    mut_expr = row[mutated].astype(float)
    wt_expr = row[wildtype].astype(float)

    fold_change = mut_expr.mean() - wt_expr.mean()

    stat, p = ttest_ind(
        mut_expr,
        wt_expr,
        equal_var=False,
        nan_policy="omit"
    )

    results.append([gene, fold_change, p])

results = pd.DataFrame(
    results,
    columns=["Gene", "Log2FoldChange", "PValue"]
)

# Add FDR correction
results["FDR"] = multipletests(
    results["PValue"],
    method="fdr_bh"
)[1]

# Sort by FDR
results = results.sort_values("FDR")

print(results.head(20))

results.to_csv(
    "../results/EGFR_differential_expression_FDR.csv",
    index=False
)

print("\nResults saved!")













