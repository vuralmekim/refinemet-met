import sys
from data_loader import tree_loader
from jet_calculations import sum_jets
from plotter import plot_met_distribution
from utils import apply_cuts

def run(file1, file2=None):
    refined_df, fastsim_df, fullsim_df = tree_loader(file1, file2)

    refined_df = apply_cuts(refined_df,"FastSim")
    fastsim_df = apply_cuts(fastsim_df,"FastSim")
    fullsim_df = apply_cuts(fullsim_df,"FastSim")

    refined_met = refined_df.groupby("EventID").apply(sum_jets, "RecJet_pt_Refined", "RecJet_eta_FastSim", "RecJet_phi_FastSim").values
    fastsim_met = fastsim_df.groupby("EventID").apply(sum_jets, "RecJet_pt_FastSim", "RecJet_eta_FastSim", "RecJet_phi_FastSim").values
    fullsim_met = fullsim_df.groupby("EventID").apply(sum_jets, "RecJet_pt_FullSim", "RecJet_eta_FullSim", "RecJet_phi_FullSim").values

    plot_met_distribution(refined_met,fastsim_met,fullsim_met)

    return "plot has been saved"

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) == 1:
        run(args[0])
    elif len(args) == 2:
        run(args[0], args[1])
    else:
        print("Usage: python script.py <file1.root> [file2.root]")

    # keyword argüman olarak alabilirsin - strategic pattern
    # main.py içinde func main olmasın
