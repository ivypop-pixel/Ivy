
import numpy as np
import pandas as pd
import yaml
import argparse
import os
import sys

def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)

def filter_low_counts(df, threshold, max_pct):
    """Filter genes with low counts"""
    # Count values below threshold in each column
    low_frac = (df < threshold).mean(axis=0)
    # Keep columns where the percentage of low counts is less than max_pct
    return df.loc[:, low_frac <= max_pct]

def filter_by_cv(df, min_cv):
    """Keep genes whose coefficient of variation >= min_cv, and drops mean=0 genes"""
    # Calculate coefficient of variation for each gene
    cv = df.std(axis=0) / df.mean(axis=0).replace(0, np.nan)
    # Keep genes with CV above the threshold
    return df.loc[:, cv >= min_cv]

def filter_by_biotype(df, annotation_path, biotype="protein_coding"):
    """Keep only genes matching biotype. Returns df unchanged if annotation can't be read"""
    try:
        sep = "\t" if annotation_path.endswith((".tsv", ".gtf")) else ","
        annot = pd.read_csv(annotation_path, sep=sep, low_memory=False)
        coding = set(annot.loc[annot["gene_biotype"] == biotype, "gene_id"].dropna())
        return df[[c for c in df.columns if c in coding]]
    except Exception as e:
        print(f"  WARNING: biotype filter skipped – {e}")
        return df
def main():
    input_path  = "augmented_expression.csv"
    output_path = "path/outputs/expression_filtered.csv"
    qc_dir      = "/path/to/outputs/qc"
    annot_path  = ""

    threshold  = 1
    max_pct    = 0.80
    min_cv     = 0.1
    do_biotype = False
    biotype    = "protein_coding"


# def main():
#     parser = argparse.ArgumentParser()
#     parser.add_argument("--config", default="config.yaml")
#     args, _ = parser.parse_known_args()

#     cfg        = load_config(args.config)
#     paths      = cfg.get("paths", {})
#     filt       = cfg.get("gene_filtering", {})

#     input_path  = paths.get("augmented_expression",  "outputs/augmented_expression.csv")
#     output_path = paths.get("expression_filtered",   "outputs/expression_filtered.csv")
#     qc_dir      = paths.get("qc_dir",                "outputs/qc")
#     annot_path  = paths.get("gene_annotation",        "")

#     threshold   = float(filt.get("low_count_threshold",  1))
#     max_pct     = float(filt.get("low_count_max_pct",    0.80))
#     min_cv      = float(filt.get("cv_threshold",          0.1))
#     do_biotype  = bool(filt.get("apply_biotype_filter",  False))
#     biotype     = filt.get("biotype", "protein_coding")

    if not os.path.exists(input_path):
        print(f"ERROR: input file not found: {input_path}")
        sys.exit(1)

    df = pd.read_csv(input_path, index_col=0)
    n0 = df.shape[1]
    print(f"Loaded: {df.shape[0]} samples × {n0} genes")

    df = filter_low_counts(df, threshold, max_pct)
    n1 = df.shape[1]
    print(f"  After low-count filter : {n1} genes  ({n0 - n1} dropped)")

    df = filter_by_cv(df, min_cv)
    n2 = df.shape[1]
    print(f"  After CV filter        : {n2} genes  ({n1 - n2} dropped)")

    if do_biotype and annot_path and os.path.exists(annot_path): # condition : config enabled filter, path provided, file is true. If not, filter skips entirely
        df = filter_by_biotype(df, annot_path, biotype)
        n3 = df.shape[1]
        print(f"  After biotype filter   : {n3} genes  ({n2 - n3} dropped)")
    else:
        n3 = n2 #n3 is final count regardless of filter status
        if do_biotype:
            print(f"  Biotype filter SKIPPED – annotation file not found: {annot_path}")

    os.makedirs(qc_dir, exist_ok=True)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path)

    summary = (
        f"Gene Filtering Summary\n"
        f"Initial genes     : {n0}\n"
        f"After low-count   : {n1}  (dropped {n0 - n1})\n"
        f"After CV          : {n2}  (dropped {n1 - n2})\n"
        f"After biotype     : {n3}  (dropped {n2 - n3})\n"
        f"Final gene count  : {n3}\n"
    )
    with open(os.path.join(qc_dir, "gene_filtering_summary.txt"), "w") as f:
        f.write(summary)

    print(f"\nDone. {n3} genes saved to {output_path}")

if __name__ == "__main__":
    main()