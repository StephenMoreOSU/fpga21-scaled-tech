"""Generates Table 3 of the paper (Mx-Mx via resistance).
"""

import os
from inputs import *

template = "\
\\begin{table}[tb]\n\
    \\caption{Resistance of vias. The reported values correspond to the resistance of a single via connecting two neighboring layers in the \\textsf{Mx} group.}\n\
    \\begin{tabular}{"

alignment = ""
titles = ""
for node in range(0, len(node_names )):
    alignment += "c "
    titles += "& %s " % node_names[node]
alignment = alignment[:-1] + "}\n"
titles = "     " + titles[:-1] + "\\\\\n"
template += alignment + titles

# template +=\
# "         \\hline\n\
#          \\textsf{Mx-Mx} $[\\Omega]$ %s\\\\\n\
#          \\hline\n\
#     \\end{tabular}\n\
#     \\label{table:via_res}\n\
# \\end{table}"

call = "python calc_via_res.py --pitch1 %d --inc_w1 0.1 --pitch2 %d --inc_w2 0.1 --t_barrier_bottom %d --t_barrier_top %d > via_dump.txt"



# resistances = ""
for pitches, barriers, mlayer_name in zip([my_pitches, mx_pitches], [my_barriers, mx_barriers], ["My","Mx"]):
    cur_template = template + "         \\hline\n\
         \\textsf" + f"{{{mlayer_name}-{mlayer_name}}}" +"$[\\Omega]$ %s\\\\\n\
         \\hline\n\
    \\end{tabular}\n\
    \\label{table:via_res}\n\
\\end{table}"
    resistances = ""
    for node in range(0, len(node_names)):
        pitch1 = pitches[node]
        pitch2 = pitches[node]
        top_barrier = barriers[node]
        bottom_barrier = barriers[node]
        os.system(call % (pitch1, pitch2, bottom_barrier, top_barrier))
        with open("via_dump.txt", "r") as inf:
            lines = inf.readlines()
        for line in lines:
            if line.startswith("R = "):
                resistances += "& %s " % line.split()[2]
        os.system("rm -rf via_dump.txt")

    print(cur_template % resistances[:-1])

#################### ASAP7 ####################
resistances = ""

template = "\
\\begin{table}[tb]\n\
    \\caption{Resistance of vias. The reported values correspond to the resistance of a single via connecting two neighboring layers in the \\textsf{Mx} group.}\n\
    \\begin{tabular}{"

alignment = ""
titles = ""
for node in range(0, len(asap7_pitch_names )):
    alignment += "c "
    titles += "& %s " % asap7_pitch_names[node]
alignment = alignment[:-1] + "}\n"
titles = "     " + titles[:-1] + "\\\\\n"
template += alignment + titles

cur_template = template + "         \\hline\n\
         \\textsf" + f"{{{mlayer_name}-{mlayer_name}}}" +"$[\\Omega]$ %s\\\\\n\
         \\hline\n\
    \\end{tabular}\n\
    \\label{table:via_res}\n\
\\end{table}"

for node in range(0, len(asap7_pitch_names)):
    pitch1 = asap7_pitches[node]
    pitch2 = asap7_pitches[node]
    top_barrier = asap7_barriers[node]
    bottom_barrier = asap7_barriers[node]
    os.system(call % (pitch1, pitch2, bottom_barrier, top_barrier))
    with open("via_dump.txt", "r") as inf:
        lines = inf.readlines()
    for line in lines:
        if line.startswith("R = "):
            resistances += "& %s " % line.split()[2]
            print(f"RES: p1:{pitch1}, p2:{pitch2}",line.split()[2])
        elif line.startswith("H = "):
            print(f"H: p1:{pitch1}, p2:{pitch2}",line.split()[2])
    os.system("rm -rf via_dump.txt")
    if(node < len(asap7_pitch_names)-1):
        # calc resistance for vias between mlayers
        pitch1 = asap7_pitches[node]
        pitch2 = asap7_pitches[node+1]
        top_barrier = asap7_barriers[node]
        bottom_barrier = asap7_barriers[node+1]
        os.system(call % (pitch1, pitch2, bottom_barrier, top_barrier))
        with open("via_dump.txt", "r") as inf:
            lines = inf.readlines()
        for line in lines:
            if line.startswith("R = "):
                resistances += "& %s " % line.split()[2]
                print(f"RES: p1:{pitch1}, p2:{pitch2}",line.split()[2])
            elif line.startswith("H = "):
                print(f"H: p1:{pitch1} ,p2:{pitch2}",line.split()[2])
        # os.system("rm -rf via_dump.txt")
# print(asap7_pitch_names)
# print(resistances)

    # print(cur_template % resistances[:-1])