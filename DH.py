#create the homogenous transform
#the dh table is in format (theta_degree, d, alpha_degree, a)
import numpy as np
import sympy as sp
q1=q2=q3=q4=q5=q6=0
joint_variables = [q1, q2, q3, q4, q5, q6]
q1 = 90
DH_table = [
[q1*sp.pi/180, 324, -90*sp.pi/180, 312],
[q2*sp.pi/180, 0,    0*sp.pi/180,  1750],
[q3*sp.pi/180, -200, -90*sp.pi/180, 225],
[q4*sp.pi/180, 1280, 90*sp.pi/180,  0],
[q5*sp.pi/180, 0,    -90*sp.pi/180, 0],
[q6*sp.pi/180, 0,    0*sp.pi/180,   0]
]

#calculate the matrix from each joint to the next
#TODO Make this function takes two frames and calculate the homogenous
def homogenous (DH_table, dh_row):
    H = [
    [sp.cos(DH_table[dh_row][0]), -sp.sin(DH_table[dh_row][0])*sp.cos(DH_table[dh_row][2]), sp.sin(DH_table[dh_row][0])*sp.sin(DH_table[dh_row][2]), DH_table[dh_row][3]*sp.cos(DH_table[dh_row][0]) ],
    [sp.sin(DH_table[dh_row][0]), sp.cos(DH_table[dh_row][0])*sp.cos(DH_table[dh_row][2]), -sp.cos(DH_table[dh_row][0])*sp.sin(DH_table[dh_row][2]), DH_table[dh_row][3]*sp.sin(DH_table[dh_row][0])],
    [0, sp.sin(DH_table[dh_row][2]), sp.cos(DH_table[dh_row][2]), DH_table[dh_row][1]],
    [0,0,0,1]
    ]
    return np.array(H)

#calculate the matrix from the end effector to the base joint
def Robot_matrix() :
    R_M = np.identity(3)
    for i in range(6):
        H = homogenous(i)
        R_M = R_M.dot(H)
    return R_M


'''
#some tests
H_1=homogenous(0)
print (H_1)
col = np.array([0,0,0,1]).reshape(4,1)

print (H_1.dot(col))
'''
