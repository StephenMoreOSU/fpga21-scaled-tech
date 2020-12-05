"""Holds the data necessary to produce Figure 12 of the paper.
"""

#Result of: python local_wires.py --K 6 --N 8 --tech 4 --density 0.5 --all_endpoints 1
c1 = ([1.3190899999999998e-11, 1.32328e-11, 1.4328400000000001e-11, 1.585535e-11, 1.6303600000000002e-11, 1.87057e-11, 2.2634399999999997e-11, 2.278325e-11, 2.540935e-11, 3.02089e-11, 3.03761e-11, 3.333605e-11, 3.63241e-11, 3.6883400000000004e-11, 3.915515e-11, 4.0964549999999996e-11, 4.24357e-11, 4.3611e-11, 4.564025e-11, 4.5648999999999997e-11, 4.638479999999999e-11, 4.642725e-11, 4.8004499999999996e-11, 4.913035e-11], "F4 Mx")

#Result of: python local_wires.py --K 6 --N 8 --tech 4 --density 0.5 --all_endpoints 1 --insert_rep 1
c2 = ([1.2903999999999999e-11, 1.29212e-11, 1.392425e-11, 1.5182749999999997e-11, 1.5749450000000003e-11, 1.71434e-11, 1.9391249999999998e-11, 1.984485e-11, 2.01381e-11, 2.2886449999999997e-11, 2.5043099999999998e-11, 2.64785e-11, 2.836115e-11, 2.8385049999999997e-11, 2.97255e-11, 3.086275e-11, 3.182075e-11, 3.471235e-11, 3.628195e-11, 3.665055e-11, 3.682925e-11, 3.811465e-11, 3.83654e-11, 3.900065e-11], "F4 Mx with in-line repeaters")

#Result of: python local_wires.py --K 6 --N 8 --tech 4 --density 0.5 --all_endpoints 1 --insert_rep 1 --rep_at_lut_x 1
c3 = ([1.324365e-11, 1.325475e-11, 1.4328549999999999e-11, 1.54676e-11, 1.6074500000000002e-11, 1.760255e-11, 1.9607099999999997e-11, 2.00427e-11, 2.027705e-11, 2.30898e-11, 2.8817749999999997e-11, 3.0361150000000004e-11, 3.25007e-11, 3.2518e-11, 3.38095e-11, 3.479245e-11, 3.6032350000000003e-11, 4.2327599999999995e-11, 4.4016149999999994e-11, 4.4483149999999994e-11, 4.456365e-11, 4.5656650000000005e-11, 4.61059e-11, 4.681345e-11], "F4 Mx with repeaters at LUT output")

#Result of: python local_wires.py --K 6 --N 8 --tech 4 --density 0.5 --all_endpoints 1 --use_my 1
c4 = ([1.6129849999999998e-11, 1.632785e-11, 1.721935e-11, 1.7258200000000002e-11, 1.8218849999999998e-11, 1.82249e-11, 1.917335e-11, 1.957165e-11, 1.9986500000000003e-11, 2.0745550000000003e-11, 2.1263399999999998e-11, 2.15571e-11, 2.1915949999999995e-11, 2.2317499999999998e-11, 2.252525e-11, 2.2535250000000002e-11, 2.319065e-11, 2.3438e-11, 2.350095e-11, 2.3570850000000002e-11, 2.3831199999999998e-11, 2.394685e-11, 2.461875e-11, 2.520445e-11], "F4 My long vertical line")

curves = [c1, c2, c3, c4]
