
"""
05_transform_expression.py
Normalize and scale gene expression so it's ready for ML.
"""
import numpy as np
import pandas as pd
import yaml
import argparse
import os
import sys

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt
    PLOTS_AVAILABLE = True
except ImportError:
    PLOTS_AVAILABLE = False


def load_config(path):
    with open(path) as f:
        return yaml.safe_load(f)

def normalize_library_size(df, scale_factor=1e6):
    """CPM normalization: divide each sample by its total counts, multiply by scale_factor."""
    library_sizes = df.sum(axis=1).replace(0, 1)  # replace 0 to avoid division by zero
    return df.div(library_sizes, axis=0) * scale_factor

def log1p_transform(df):
    """Apply log(1 + x) to each value."""
    return np.log1p(df)

def zscore_genes(df):
    """Z-score each gene (column) across samples, constant genes are set to 0."""
    mean = df.mean(axis=0)
    std  = df.std(axis=0).replace(0, np.nan)  # replace 0 to avoid division by zero
    return ((df - mean) / std).fillna(0.0)


def save_plots(before, after, plots_dir):
    """keep before/after expression distribution histograms."""
    if not PLOTS_AVAILABLE:
        print("  WARNING: matplotlib not installed – skipping plots")
        return
    os.makedirs(plots_dir, exist_ok=True)
    fig, axes = plt.subplots(1, 2, figsize=(12, 4))
    axes[0].hist(before.values.flatten(), bins=100, color="steelblue")
    axes[0].set_title("Before transformation")
    axes[0].set_xlabel("Expression value")
    axes[1].hist(after.values.flatten(), bins=100, color="darkorange")
    axes[1].set_title("After transformation")
    axes[1].set_xlabel("Expression value (z-scored)")
    plt.tight_layout()
    plot_path = os.path.join(plots_dir, "expr_distribution_before_after.png")
    plt.savefig(plot_path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"  Plot saved: {plot_path}")

def main():
    input_path  = "expression_filtered.csv"
    output_path = "/content/outputs/expression_transformed.csv"
    qc_dir      = "/content/outputs/qc"
    plots_dir   = "/content/outputs/plots"

    do_cpm    = True
    do_log1p  = True
    do_zscore = True
    do_plots  = False

    if not os.path.exists(input_path):
        print(f"ERROR: input file not found: {input_path}")
        sys.exit(1)

    df = pd.read_csv(input_path, index_col=0)
    print(f"Loaded: {df.shape[0]} samples × {df.shape[1]} genes")
    print(f"  Before – min: {df.values.min():.2f}  max: {df.values.max():.2f}  mean: {df.values.mean():.2f}")

    before = df.copy()

    if do_cpm:
        df = normalize_library_size(df)
        print(f"  After CPM normalization – max: {df.values.max():.2f}")

    if do_log1p:
        df = log1p_transform(df)
        print(f"  After log1p – max: {df.values.max():.4f}")

    if do_zscore:
        df = zscore_genes(df)
        print(f"  After z-score – mean: {df.values.mean():.2e}  std: {df.values.std():.4f}")

    print(f"  After – min: {df.values.min():.4f}  max: {df.values.max():.4f}")

    os.makedirs(qc_dir, exist_ok=True)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path)

    summary = (
        f"Transformation Summary\n"
        f"Steps applied:\n"
        f"  CPM normalization : {'yes' if do_cpm    else 'no'}\n"
        f"  log1p             : {'yes' if do_log1p  else 'no'}\n"
        f"  z-score           : {'yes' if do_zscore else 'no'}\n"
        f"\nOutput shape : {df.shape[0]} samples × {df.shape[1]} genes\n"
        f"Value range  : {df.values.min():.4f} to {df.values.max():.4f}\n"
        f"Gene means   : max deviation from 0 = {df.mean(axis=0).abs().max():.2e}\n"
        f"Gene stds    : max deviation from 1 = {(df.std(axis=0)[df.std(axis=0) > 1e-10] - 1).abs().max():.2e}\n"
    )
    with open(os.path.join(qc_dir, "transformation_qc.txt"), "w") as f:
        f.write(summary)
    print(summary)

    if do_plots:
        save_plots(before, df, plots_dir)

    print(f"All done. Saved to {output_path}")

if __name__ == "__main__":
    main()