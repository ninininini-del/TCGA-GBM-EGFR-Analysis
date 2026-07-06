from pathlib import Path
import pandas as pd

project = Path(__file__).resolve().parent.parent
data = project / "data"

clinical = pd.read_csv(
    data / "Human__TCGA_GBM__MS__Clinical__Clinical__01_28_2016__BI__Clinical__Firehose.tsi.txt",
    sep="\t"
)

print(clinical["attrib_name"].tolist())