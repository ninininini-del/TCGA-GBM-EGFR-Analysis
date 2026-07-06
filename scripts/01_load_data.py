from pathlib import Path
import pandas as pd

# Project folder
project = Path(__file__).resolve().parent.parent

# Data folder
data = project / "data"

# Load RNA
rna = pd.read_csv(
    data / "RNAseq.cct",
    sep="\t"
)

# Load mutation
mutation = pd.read_csv(
    data / "Human__TCGA_GBM__WUSM__Mutation__GAIIx__01_28_2016__BI__Gene__Firehose_MutSig2CV.cbt.txt",
    sep="\t"
)

# Load clinical
clinical = pd.read_csv(
    data / "Human__TCGA_GBM__MS__Clinical__Clinical__01_28_2016__BI__Clinical__Firehose.tsi.txt",
    sep="\t"
)

print("RNA:", rna.shape)
print("Mutation:", mutation.shape)
print("Clinical:", clinical.shape)