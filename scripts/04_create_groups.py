from pathlib import Path
import pandas as pd

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
# Find common patients
# -------------------------
rna_patients = set(rna.columns[1:])
mutation_patients = set(mutation.columns[1:])

common = sorted(rna_patients.intersection(mutation_patients))

# -------------------------
# Find EGFR row
# -------------------------
egfr = mutation[mutation["attrib_name"] == "EGFR"]

# -------------------------
# Separate patients
# -------------------------
mutated = []
wildtype = []

for patient in common:
    value = int(egfr[patient].values[0])

    if value == 1:
        mutated.append(patient)
    else:
        wildtype.append(patient)

print(f"EGFR mutated patients: {len(mutated)}")
print(f"EGFR wild-type patients: {len(wildtype)}")

print("\nFirst 10 mutated:")
print(mutated[:10])

print("\nFirst 10 wild-type:")
print(wildtype[:10])