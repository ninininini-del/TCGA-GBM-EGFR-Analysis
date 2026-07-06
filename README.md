# TCGA-GBM-EGFR-Analysis

End-to-end bioinformatics analysis of TCGA glioblastoma using RNA-seq, mutation, and clinical data in Python


# EGFR-Associated Transcriptomic Analysis in Glioblastoma (TCGA)

## Overview

This project investigates the molecular consequences of **EGFR mutations in Glioblastoma (GBM)** using publicly available data from **The Cancer Genome Atlas (TCGA)**.

RNA sequencing, mutation, and clinical datasets were integrated to identify transcriptomic alterations associated with EGFR mutations and to evaluate their biological and clinical relevance.

---

## Objectives

- Compare EGFR-mutated and wild-type GBM tumors
- Perform differential gene expression analysis
- Apply multiple-testing correction (Benjamini–Hochberg FDR)
- Visualize transcriptomic differences
- Perform GO and KEGG pathway enrichment
- Evaluate patient survival using Kaplan–Meier analysis

---

## Dataset

Source:

The Cancer Genome Atlas (TCGA)

Cancer type:

Glioblastoma Multiforme (GBM)

Data types:

- RNA-seq
- Somatic mutations
- Clinical information

---

## Software

Python 3

Libraries

- pandas
- numpy
- scipy
- matplotlib
- scikit-learn
- statsmodels
- lifelines
- gseapy

---

## Workflow

TCGA Data

↓

Quality control

↓

Patient matching

↓

EGFR mutation stratification

↓

Differential expression

↓

Volcano plot

↓

Heatmap

↓

Principal Component Analysis

↓

GO enrichment

↓

KEGG enrichment

↓

Kaplan–Meier survival analysis

---

## Results

### Cohort

- 141 matched patients
- 45 EGFR-mutated
- 96 EGFR wild-type

### Differential expression

- 323 significant genes (FDR < 0.05)

Top genes included:

- EGFR
- MASP1
- TACR1
- HOXB3
- SOX9

### GO enrichment

Major enriched biological processes included:

- EGFR signaling
- Fatty acid metabolism
- Lipid metabolism
- Ketone body metabolism

### KEGG

Top pathways included:

- Gap Junction
- Ferroptosis
- Central Carbon Metabolism in Cancer
- Fatty Acid Elongation

### Survival

Kaplan–Meier analysis demonstrated **no significant difference** in overall survival between EGFR-mutated and wild-type patients.

Log-rank test

p = 0.7804

---

## Figures

<img width="1366" height="647" alt="Figure_3" src="https://github.com/user-attachments/assets/d8d5917f-6b1d-4c2f-a033-114f2cb74e6e" />
<img width="818" height="638" alt="Figure_2" src="https://github.com/user-attachments/assets/62ee22ff-a4c4-48d4-8265-3124ac207f7e" />
<img width="681" height="638" alt="Figure_1" src="https://github.com/user-attachments/assets/7d1d0680-2f06-47b6-a7bf-265a48e68c6e" />


---

## Author

Ines Kellou

Interested in Bioinformatics, Cancer Genomics and Computational Biology.
