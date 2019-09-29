import DH
import sympy as sp

#calculate the forward list of the joint varialbles
def forward (joint_var):
    #put the values in the DH_table
    for i in range(6):
        DH.DH_table[i][0] = joint_var[0]*sp.pi/180
    return DH.Robot_matrix()

eq = forward([30,30,30,30,30,30])
print (eq.astype(float))
