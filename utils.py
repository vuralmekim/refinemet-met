import numpy as np

def compute_ratio_and_errors(num, denom):
    ratio = np.zeros_like(num, dtype=float)
    error = np.zeros_like(num, dtype=float)
    for i in range(len(num)):
        if denom[i] > 0:
            ratio[i] = num[i] / denom[i]
            error[i] = ratio[i] * np.sqrt(1/num[i] + 1/denom[i]) if num[i] > 0 else 0
    return ratio, error

def apply_cuts(df, df_name):
    df = df[(df[f"RecJet_eta_{df_name}"].abs() < ETA_CUT) & (df[f"RecJet_pt_{df_name}"] > PT_CUT)]
    return df
