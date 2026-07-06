from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from lifelines import KaplanMeierFitter
from lifelines.statistics import logrank_test

# -------------------------
# Paths
# -------------------------
project = Path(__file__).resolve().parent.parent
data = project / "data"
results = project / "results"

# -------------------------
# Load data
# -------------------------
mutation = pd.read_csv(
    data / "Human__TCGA_GBM__WUSM__Mutation__GAIIx__01_28_2016__BI__Gene__Firehose_MutSig2CV.cbt.txt",
    sep="\t"
)

clinical = pd.read_csv(
    data / "Human__TCGA_GBM__MS__Clinical__Clinical__01_28_2016__BI__Clinical__Firehose.tsi.txt",
    sep="\t"
)

# -------------------------
# Extract EGFR mutation row
# -------------------------
egfr = mutation[mutation["attrib_name"] == "EGFR"]

# -------------------------
# Extract survival information
# -------------------------
survival = clinical[clinical["attrib_name"] == "overall_survival"]
status = clinical[clinical["attrib_name"] == "status"]

# -------------------------
# Keep only patients present in both datasets
# -------------------------
patients = sorted(
    set(egfr.columns[1:]).intersection(survival.columns[1:])
)

records = []

for patient in patients:

    try:
        mut = int(egfr[patient].values[0])
        time = float(survival[patient].values[0])
        event = int(status[patient].values[0])

        records.append([patient, mut, time, event])

    except:
        continue

df = pd.DataFrame(
    records,
    columns=["Patient", "Mutation", "Time", "Status"]
)

print(df.head())

# -------------------------
# Split groups
# -------------------------
mut = df[df["Mutation"] == 1]
wt = df[df["Mutation"] == 0]

print(f"\nEGFR mutated patients: {len(mut)}")
print(f"EGFR wild-type patients: {len(wt)}")

# -------------------------
# Kaplan-Meier
# -------------------------
kmf = KaplanMeierFitter()

plt.figure(figsize=(8,6))

kmf.fit(
    mut["Time"],
    event_observed=mut["Status"],
    label="EGFR Mutated"
)
kmf.plot_survival_function()

kmf.fit(
    wt["Time"],
    event_observed=wt["Status"],
    label="EGFR Wild-Type"
)
kmf.plot_survival_function()

# -------------------------
# Log-rank test
# -------------------------
test = logrank_test(
    mut["Time"],
    wt["Time"],
    event_observed_A=mut["Status"],
    event_observed_B=wt["Status"]
)

plt.title("Kaplan-Meier Survival Curve")
plt.xlabel("Days")
plt.ylabel("Survival Probability")

plt.text(
    0.60,
    0.15,
    f"Log-rank p = {test.p_value:.4f}",
    transform=plt.gca().transAxes,
    fontsize=10,
    bbox=dict(facecolor="white")
)

plt.grid(True)

plt.savefig(results / "Kaplan_Meier_EGFR.png", dpi=300)

plt.show()

print("\nLog-rank p-value:", test.p_value)
print("\nFigure saved!")