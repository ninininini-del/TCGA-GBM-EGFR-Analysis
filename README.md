# 🧬 EGFR-Associated Transcriptomic Analysis in TCGA Glioblastoma

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Bioinformatics](https://img.shields.io/badge/Bioinformatics-TCGA-green)
![RNA-seq](https://img.shields.io/badge/RNA--seq-Analysis-orange)
![Status](https://img.shields.io/badge/Project-Completed-success)

---

## Project Overview

This project investigates the transcriptomic and clinical impact of **EGFR mutations** in **Glioblastoma Multiforme (GBM)** using publicly available **TCGA** datasets.

The analysis integrates:

- RNA sequencing (RNA-seq)
- Somatic mutation data
- Clinical information

to identify genes and biological pathways associated with EGFR mutation status and evaluate whether EGFR mutations influence patient survival.

---

## Objectives

- Match patients across RNA-seq, mutation and clinical datasets
- Compare EGFR-mutated and EGFR wild-type tumors
- Identify differentially expressed genes
- Perform multiple testing correction (Benjamini–Hochberg FDR)
- Explore transcriptomic variation
- Identify enriched biological pathways
- Evaluate overall survival

---

## Dataset

Source:

**The Cancer Genome Atlas (TCGA)**

Cancer type:

Glioblastoma Multiforme (GBM)

Data used:

- RNA sequencing
- Mutation profiles
- Clinical data

---

## Tools

- Python
- Pandas
- NumPy
- SciPy
- Statsmodels
- Scikit-learn
- Matplotlib
- Lifelines
- GSEApy

---

## Workflow

```text
TCGA Data
      │
      ▼
Data Cleaning
      │
      ▼
Patient Matching
      │
      ▼
EGFR Mutation Stratification
      │
      ▼
Differential Expression Analysis
      │
      ├── Volcano Plot
      ├── Heatmap
      ├── PCA
      ├── GO Enrichment
      ├── KEGG Enrichment
      ▼
Kaplan–Meier Survival Analysis
```

---

## Main Results

### Cohort

- 141 matched patients
- 45 EGFR-mutated
- 96 EGFR wild-type

### Differential Expression

- 323 significant genes after FDR correction

Top differentially expressed genes included:

- EGFR
- MASP1
- TACR1
- HOXB3
- SOX9

### Functional Enrichment

Gene Ontology highlighted processes related to:

- EGFR signaling
- Lipid metabolism
- Fatty acid metabolism
- Ketone body metabolism

KEGG pathway analysis identified pathways including:

- Gap Junction
- Ferroptosis
- Fatty Acid Elongation
- Central Carbon Metabolism in Cancer

### Survival Analysis

Kaplan–Meier survival analysis showed **no statistically significant difference** in overall survival between EGFR-mutated and wild-type patients.

**Log-rank p-value = 0.7804**

---

## Repository Structure

```text
scripts/
│
├── Data loading
├── Patient matching
├── Differential expression
├── Volcano plot
├── Heatmap
├── PCA
├── GO enrichment
├── KEGG enrichment
└── Kaplan–Meier survival analysis

results/
│
├── Differential expression tables
├── GO enrichment results
└── KEGG enrichment results

figures/
│
├── Volcano plot
├── Heatmap
├── PCA
└── Kaplan–Meier survival curve
```

---

## Skills Demonstrated

- Bioinformatics
- RNA-seq analysis
- Cancer genomics
- Statistical hypothesis testing
- Multiple testing correction
- Gene set enrichment analysis
- Survival analysis
- Data visualization
- Python programming

---

## Future Improvements

- Integrate copy number variation (CNV) data
- Machine learning classification of EGFR status
- Multi-gene survival models
- External validation on independent cohorts

---

## Author

Ines Kellou

Interested in Bioinformatics • Cancer Genomics • Computational Biology
