import pandas as pd

def check_for_overlapping_states(starts,ends,behaviors):
    '''Looks for overlapping times in state events.'''

    violation_s = []
    violation_e = []
    violation_b = []

    for i,start in enumerate(starts.iloc[:-2]):
        if ends.iloc[i]>starts.iloc[i+1]:
            violation_s.append(start)
            violation_e.append(ends.iloc[i])
            violation_b.append(behaviors.iloc[i])

    return violation_s, violation_e, violation_b

def check_for_state_gaps(starts,ends,behaviors):
    '''Looks for gaps between state events.'''

    violation_s = []
    violation_e = []
    violation_b1 = []
    violation_b2 = []

    for i,start in enumerate(starts.iloc[:-2]):
        if round(starts.iloc[i+1]-ends.iloc[i],3)>0.001:
            violation_s.append(starts.iloc[i+1])
            violation_e.append(ends.iloc[i])
            violation_b1.append(behaviors.iloc[i])
            violation_b2.append(behaviors.iloc[i+1])

    return violation_s, violation_e, violation_b1, violation_b2

def check_for_event_interactions(scoretab,verbose):
    '''Check a table of behavioral annotations for gap and overlap violations.'''

    s = scoretab.start
    e = scoretab.end
    b = scoretab.Behavior

    mask = scoretab.behavior_type=='STATE'

    smask = s[mask]
    emask = e[mask]
    bmask = b[mask]

    overlap_s, overlap_e, overlap_b = check_for_overlapping_states(smask,emask,bmask)
    gap_s, gap_e, gap_b1, gap_b2 = check_for_state_gaps(smask,emask,bmask)

    if verbose:

        for i,ols in enumerate(overlap_s):
            print(f'Overlap violation for behavior {overlap_b[i]} starting at {ols} and ending at {overlap_e[i]}.')

        for i, gs in enumerate(gap_s):
            print(f'Gap violation for behavior {gap_b1[i]} ending at {gap_e[i]} and next behavior {gap_b2[i]} starting at {gs}.')

    return overlap_s,overlap_e,overlap_b,gap_s,gap_e,gap_b1,gap_b2
