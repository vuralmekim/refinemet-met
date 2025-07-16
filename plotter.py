import numpy as np
from utils import compute_ratio_and_errors
import matplotlib.pyplot as plt
import mplhep as hep

def plot_met_distribution(refined_met,fastsim_met,fullsim_met):
    hep.style.use("CMS")

    edges = np.arange(BIN_RANGE[0], BIN_RANGE[1] + BIN_WIDTH, BIN_WIDTH)

    hist_refined, _ = np.histogram(refined_met, bins=edges)
    hist_fastsim, _ = np.histogram(fastsim_met, bins=edges)
    hist_fullsim, _ = np.histogram(fullsim_met, bins=edges)

    ratio_fastsim, ratio_fastsim_errors = compute_ratio_and_errors(hist_fastsim, hist_fullsim)
    ratio_refined, ratio_refined_errors = compute_ratio_and_errors(hist_refined, hist_fullsim)

    bin_centers = 0.5 * (edges[:-1] + edges[1:])
    ax1, ax2 = plt.subplots(2, 1, figsize=(10, 8), sharex=True,
                                gridspec_kw={"height_ratios": [3, 1], "hspace": 0.05})

    ax1.step(edges[:-1], hist_fastsim, where="mid", label='FastSim', color='blue')
    ax1.step(edges[:-1], hist_fullsim, where="mid", label='FullSim', color='black')
    ax1.step(edges[:-1], hist_refined, where="mid", label='Refined', color='red')
    ax1.set_ylabel("Events")
    if IS_LOG:
        ax1.semilogy()
    ax1.set_xlim(X_LIM)
    ax1.set_title("Hard MET Distribution")
    ax1.legend(loc="center left", bbox_to_anchor=(1.0, 0.5))
    ax1.grid(IS_GRID)

    ax2.errorbar(bin_centers, ratio_fastsim, yerr=ratio_fastsim_errors, fmt='o', color='blue', label='FastSim / FullSim')
    ax2.errorbar(bin_centers, ratio_refined, yerr=ratio_refined_errors, fmt='o', color='red', label='Refined / FullSim')
    ax2.axhline(1.0, color='black', linestyle='--')
    ax2.set_xlabel("Hard MET [GeV]")
    ax2.set_ylabel("Ratio")
    ax2.set_xlim(X_LIM)
    ax2.set_ylim(Y_LIM)
    ax2.grid(IS_GRID)
    ax2.legend(loc="center left", bbox_to_anchor=(1.0, 0.5))

    plt.savefig(PLOT_NAME)

    return "200"