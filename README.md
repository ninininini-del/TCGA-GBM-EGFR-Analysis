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

(Add your four figures here.)

---

## Author

Nini Lovebooks

Biomedical Sciences Student

Interested in Bioinformatics, Cancer Genomics and Computational Biology.
