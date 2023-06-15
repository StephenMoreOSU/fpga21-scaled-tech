"""Holds the input parameters from Section 2.2 Cross-sectional Wire Dimensions.
"""

node_names = ["F16", "F7", "F5", "F4", "F3a", "F3b"]
mx_pitches = [64, 40, 38, 26, 22, 22]
my_pitches = [80, 76, 72, 50, 48, 80]

mx_barriers = [3.0, 3.0, 3.0, 2.0, 2.0, 2.0]
my_barriers = [4.0, 4.0, 4.0, 4.0, 4.0, 4.0]

mx_ar_max = [2.0, 2.0, 2.0, 2.0, 2.0, 3.0]
my_ar_max = [2.0, 2.0, 2.0, 2.0, 2.0, 2.0]

mx_eps_rel = 2.8
my_eps_rel = 3.0


## ASAP 7 values
asap7_pitch_names = ["M1-M3","M4-M5","M6-M7","M8-M9"]
asap7_pitches = [36, 48, 64, 80]
asap7_best_ars = [2.0]*len(asap7_pitches)
asap7_barriers = [1.5]*len(asap7_pitches)
