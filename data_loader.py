import uproot
import pandas as pd

def tree_loader(file1, file2):
    tree = uproot.open(file1)["tJet"].arrays(library="pd")
    if file2:
        tree2 = uproot.open(file2)["tEvent"].arrays(library="pd")
        tree["EventID"] = tree["EventID"].astype(float)
        tree2["EventID"] = tree2["EventID"].astype(float)
        tree = pd.merge(tree, tree2, on="EventID")

    refined_df = tree[['EventID', 'RecJet_pt_Refined', 'RecJet_eta_FastSim', 'RecJet_phi_FastSim']]
    fastsim_df = tree[['EventID', 'RecJet_pt_FastSim', 'RecJet_eta_FastSim', 'RecJet_phi_FastSim']]
    fullsim_df = tree[['EventID', 'RecJet_pt_FullSim', 'RecJet_eta_FullSim', 'RecJet_phi_FullSim']]

    return refined_df, fastsim_df, fullsim_df

# event kontrolü, eksik id var mı vs vs