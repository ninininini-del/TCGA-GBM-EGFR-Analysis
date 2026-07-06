from pathlib import Path
import pandas as pd

# -------------------------
# Load the datasets
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
# Get patient IDs
# -------------------------
rna_patients = set(rna.columns[1:])       # Skip "attrib_name"
mutation_patients = set(mutation.columns[1:])

common = sorted(rna_patients.intersection(mutation_patients))

print(f"RNA patients: {len(rna_patients)}")
print(f"Mutation patients: {len(mutation_patients)}")
print(f"Common patients: {len(common)}")

print("\nFirst 10 common patients:")
for patient in common[:10]:
    print(patient)