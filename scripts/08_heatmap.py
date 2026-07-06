from pathlib import Path
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# -------------------------
# Load data
# -------------------------
project = Path(__file__).resolve().parent.parent
data = project / "data"
results_folder = project / "results"

rna = pd.read_csv(
    data / "RNAseq.cct",
    sep="\t"
)

mutation = pd.read_csv(
    data / "Human__TCGA_GBM__WUSM__Mutation__GAIIx__01_28_2016__BI__Gene__Firehose_MutSig2CV.cbt.txt",
    sep="\t"
)

results = pd.read_csv(
    results_folder / "EGFR_differential_expression.csv"
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
# Top 50 genes
# -------------------------
top50 = results.head(50)["Gene"]

heatmap = rna[rna["attrib_name"].isin(top50)]

heatmap = heatmap.set_index("attrib_name")

heatmap = heatmap[mutated + wildtype]

# -------------------------
# Plot
# -------------------------
plt.figure(figsize=(14,10))

sns.heatmap(
    heatmap,
    cmap="coolwarm",
    xticklabels=False,
    yticklabels=True
)

plt.title("Top 50 Differentially Expressed Genes")
plt.xlabel("Patients")
plt.ylabel("Genes")

plt.tight_layout()
plt.show()