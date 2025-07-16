import ROOT

def sum_lorentz_vectors(group, pt_col, eta_col, phi_col):
    vec = ROOT.TLorentzVector()
    for _, row in group.iterrows():
        j = ROOT.TLorentzVector()
        j.SetPtEtaPhiM(row[pt_col], row[eta_col], row[phi_col], 0)
        vec += j
    return vec

def sum_jets(group, pt_col, eta_col, phi_col):
    return (-sum_lorentz_vectors(group, pt_col, eta_col, phi_col)).Pt()

