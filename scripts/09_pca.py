from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

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
# Expression matrix
# -------------------------
expression = rna.set_index("attrib_name")

expression = expression[common]

# patients = rows
expression = expression.T

# -------------------------
# Standardize
# -------------------------
scaler = StandardScaler()

scaled = scaler.fit_transform(expression)

# -------------------------
# PCA
# -------------------------
pca = PCA(n_components=2)

components = pca.fit_transform(scaled)

pca_df = pd.DataFrame(
    components,
    columns=["PC1", "PC2"]
)

pca_df["Group"] = [
    "EGFR Mutated" if patient in mutated else "Wild Type"
    for patient in common
]

# -------------------------
# Plot
# -------------------------
plt.figure(figsize=(8,6))

colors = {
    "EGFR Mutated":"red",
    "Wild Type":"blue"
}

for group in colors:

    subset = pca_df[pca_df["Group"] == group]

    plt.scatter(
        subset["PC1"],
        subset["PC2"],
        label=group,
        alpha=0.8
    )

plt.xlabel(f"PC1 ({pca.explained_variance_ratio_[0]*100:.1f}% variance)")
plt.ylabel(f"PC2 ({pca.explained_variance_ratio_[1]*100:.1f}% variance)")

plt.title("PCA of GBM RNA-seq")

plt.legend()

plt.tight_layout()

plt.show()