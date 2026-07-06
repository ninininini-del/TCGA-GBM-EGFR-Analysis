from pathlib import Path
import pandas as pd

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

clinical = pd.read_csv(
    data / "Human__TCGA_GBM__MS__Clinical__Clinical__01_28_2016__BI__Clinical__Firehose.tsi.txt",
    sep="\t"
)

print("===== RNA =====")
print(rna.head())
print()

print("===== Mutation =====")
print(mutation.head())
print()

print("===== Clinical =====")
print(clinical.head())